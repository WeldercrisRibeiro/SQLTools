import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QVBoxLayout, QShortcut, QLineEdit
from PyQt5.QtGui import QIcon, QKeySequence
import pyodbc
import os
from configparser import ConfigParser
import ctypes
import datetime
import shutil

# Importar as classes geradas a partir dos arquivos .ui
from login_dialog_ui import Ui_LoginDialog
from main.main_window_ui import Ui_MainWindow
from main.server_config_dialog_ui import Ui_ServerConfigDialog

class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.login_button.clicked.connect(self.login)
        self.setModal(True)
        
        # Conectar sinal de mudança de texto para transformar em maiúsculas
        self.user_entry.textChanged.connect(self.on_text_changed)
        
    def on_text_changed(self, text):
        self.user_entry.setText(text.upper())
        
    def login(self):
        user = self.user_entry.text()
        password = self.password_entry.text().upper()  # Convertendo senha para maiúsculo
        credentials = self.get_credentials()
        
        if user in credentials and password == credentials[user]:
            self.accept()
        else:
            self.show_critical_message("Login Falhou", "Usuário ou senha inválidos")
            
    def get_credentials(self):
         return {
             "ADMIN": "DBA"
         }
    
    def show_critical_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QLabel{color: white;}")  # Texto da mensagem em branco
        msg.exec_()

class ServerConfigDialog(QDialog, Ui_ServerConfigDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Configuração do Servidor")
        
        # Alterando as cores dos botões
        self.set_button_colors()
        
        # Carregar as configurações existentes ao abrir o diálogo
        self.load_configurations()
        
        # Conectar o botão de salvar
        self.save_button.clicked.connect(self.save_configurations)
        
    def set_button_colors(self):
        self.save_button.setStyleSheet("background-color: #4CAF50; color: white;")
        
    def load_configurations(self):
        config = ConfigParser()
        config.read('configTools.ini')
        
        self.server_entry.setText(config['SQLServer']['server'])
        self.database_entry.setText(config['SQLServer']['database'])
        self.username_entry.setText(config['SQLServer']['username'])
        self.password_entry.setText(config['SQLServer']['password'])
        
    def save_configurations(self):
        config = ConfigParser()
        
        config['SQLServer'] = {
            'server': self.server_entry.text(),
            'database': self.database_entry.text(),
            'username': self.username_entry.text(),
            'password': self.password_entry.text()
        }
        
        with open('configTools.ini', 'w') as configfile:
            config.write(configfile)
            
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Configurações Salvas")
        msg_box.setText("Configurações do servidor salvas com sucesso.")
        msg_box.setStyleSheet("QLabel{color: black;} QPushButton{background-color: green; color: white;}")
        
        msg_box.exec_()
        
        self.accept()

class SQLTerminalApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SQL Terminal")
        self.set_icon()
        self.usuarios = self.get_users()
        self.login_dialog = LoginDialog()
        
        if self.login_dialog.exec_() != QDialog.Accepted:
            sys.exit()
        
        self.center_on_screen()
        self.setup_connections()
        self.setup_shortcuts()

    def set_icon(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        icon_path = os.path.join(base_path, "sql.ico")
        
        if not os.path.exists(icon_path):
            icon_path = os.path.join(os.path.abspath("."), "sql.ico")
        
        app.setWindowIcon(QIcon(icon_path))
        
        if hasattr(sys, '_MEIPASS'):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        
    def get_users(self):
         return {
             "ADMIN": "DBA"
         }
    
    def setup_connections(self):
        self.execute_button.clicked.connect(self.executar_consulta)
        self.clear_button.clicked.connect(self.limpar_resultado)
        self.exit_button.clicked.connect(self.sair)
        
    def setup_shortcuts(self):
        self.shortcut_f5 = QShortcut(QKeySequence("F5"), self)
        self.shortcut_f5.activated.connect(self.executar_consulta)
        
        self.shortcut_f6 = QShortcut(QKeySequence("F6"), self)
        self.shortcut_f6.activated.connect(self.limpar_resultado)
        
        self.shortcut_esc = QShortcut(QKeySequence("ESC"), self)
        self.shortcut_esc.activated.connect(self.sair)
        
        self.shortcut_f7 = QShortcut(QKeySequence("F7"), self)
        self.shortcut_f7.activated.connect(self.abrir_configuracao_servidor)
        
    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.frameSize().width()) // 2
        y = (screen_geometry.height() - self.frameSize().height()) // 2
        self.move(x, y)
        
    def sair(self):
        self.close()
        
    def autenticar_usuario(self):
        usuario = self.login_dialog.user_entry.text().upper()
        senha = self.login_dialog.password_entry.text().upper()  # Convertendo senha para maiúsculo
        
        if usuario in self.usuarios and self.usuarios[usuario] == senha:
            return True
        else:
            self.show_critical_message("Autenticação Falhou", "Usuário ou senha inválidos.")
            return False
        
    def registrar_log(self, usuario, comando, servidor=None, erro=None):
        caminho_log = 'SQL.log'
        caminho_backup = 'C:/INFARMA/LOJA/Client/logTools'
        
        if not os.path.exists(caminho_backup):
            os.makedirs(caminho_backup)
            
        with open(caminho_log, 'a') as arquivo_log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if servidor:
                arquivo_log.write(f'{timestamp} - Conectado - {servidor}\n')
            if comando:
                arquivo_log.write(f'{timestamp} - {usuario} - {comando}\n')
            if erro:
                arquivo_log.write(f'{timestamp} - {usuario} - {erro}\n')
                
        caminho_backup_log = os.path.join(caminho_backup, 'SQL.log')
        shutil.copy2(caminho_log, caminho_backup_log)
        
    def executar_consulta(self):
        if not self.autenticar_usuario():
            return
        
        conn = self.conectar_bd()
        if conn:
            query = self.query_entry.toPlainText()
            cursor = conn.cursor()
            
            usuario = self.login_dialog.user_entry.text().upper()
            self.registrar_log(usuario, query)
            
            try:
                cursor.execute(query)
                
                if query.lower().startswith("select"):
                    self.result_text.clear()
                    for row in cursor:
                        row = [str(value) if value is not None else "NULL" for value in row]
                        self.result_text.append(str(row))
                else:
                    conn.commit()
                    QMessageBox.information(self, "Consulta Executada", "Consulta executada com sucesso.")
                    
                cursor.close()
                conn.close()
            except pyodbc.Error as e:
                self.show_critical_message("Erro na Execução", f"Erro ao executar a consulta: {e}")
                self.registrar_log(usuario, query, None, f"Erro ao executar a consulta: {e}")
        
    def limpar_resultado(self):
        self.result_text.clear()
        
    def ler_ou_criar_configuracoes(self):
        config = ConfigParser()
        
        if not os.path.exists('configTools.ini'):
            config['SQLServer'] = {
                'server': 'LOCALHOST',
                'database': 'VMD',
                'username': '',
                'password': ''
            }
            
            with open('configTools.ini', 'w') as configfile:
                config.write(configfile)
                
        else:
            config.read('configTools.ini')
            
        return config
    
    def conectar_bd(self):
        config = self.ler_ou_criar_configuracoes()
        server = config['SQLServer']['server']
        database = config['SQLServer']['database']
        username = config['SQLServer']['username']
        password = config['SQLServer']['password']
        
        usuario = self.login_dialog.user_entry.text().upper()
        self.registrar_log(usuario, None, server)  # Registra a tentativa de conexão
        
        try:
            conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
            return conn
        except pyodbc.Error as e:
            self.show_critical_message("Erro de Conexão", f"Não foi possível conectar ao banco de dados: {e}")
            self.registrar_log(usuario, None, server, f"Não foi possível conectar ao banco de dados: {e}")
            return None 
    
    def show_critical_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QLabel{color: red;}")  # Texto da mensagem em vermelho
        msg.exec_()
        
    def abrir_configuracao_servidor(self):
        config_dialog = ServerConfigDialog(self)
        
        # Alterar a cor do texto
        config_dialog.setStyleSheet("color: green;")  # Define o texto em azul
        
        
        
        config_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SQLTerminalApp()
    window.show()
    sys.exit(app.exec_())
