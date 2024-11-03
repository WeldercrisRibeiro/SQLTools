from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QVBoxLayout, QShortcut, QLineEdit, QToolBar, QPushButton, QAction, QListWidget, QFormLayout, QCheckBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5 import QtGui
import sys
import os
from PyQt5.QtCore import Qt 
#import ctypes
import datetime
import shutil
import base64
import pyodbc
#import keyboard
from configparser import ConfigParser
from login_dialog_ui import Ui_LoginDialog
from main_window_ui import Ui_MainWindow
from server_config_dialog_ui import Ui_ServerConfigDialog


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.login_button.clicked.connect(self.login)
        self.setModal(True)
        self.user_entry.textChanged.connect(self.on_text_changed)
        #self.setWindowIcon(QIcon("sqlIco.ico")) 
        
        icon_base64 = """
        
        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
        
        
        """
        
        icon_data = base64.b64decode(icon_base64)
        self.icon_pixmap = QtGui.QPixmap()
        self.icon_pixmap.loadFromData(icon_data)
        self.setWindowIcon(QIcon(self.icon_pixmap))

    def on_text_changed(self, text):
        self.user_entry.setText(text.upper())

    def login(self):
        user = self.user_entry.text()
        password = self.password_entry.text()
        credentials = self.get_credentials()

        if user in credentials and password == credentials[user]:
            self.accept()
        else:
            self.show_critical_message("Login Falhou", "Usuário ou senha inválidos")

    def get_credentials(self):
        return {
            
    "PAIVA": "PVA",
    "MATHEUS": "MTH",
    "KELTON": "KLT",
    "WLADIMIR": "WLD",
    "VICTOR": "VTR",
    "WELDER": "2507",
    "RODRIGO": "RDO",
    "SERGIO": "SGO"
    
        }

    def show_critical_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QLabel{color: red;}")
        msg.exec_()

class ServerConfigDialog(QDialog, Ui_ServerConfigDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Configuração do Servidor")
        self.set_button_colors()
        self.load_configurations()
        #self.shorcut_pgdwn = QShortcut(QKeySequence("PageDown"),self)
        #self.save_button.clicked.connect(self.save_configurations)


        self.shortcut_pgdwn = QShortcut(QKeySequence("F8"), self)
        self.shortcut_pgdwn.activated.connect(self.save_configurations)

        self.save_button.clicked.connect(self.save_configurations)

        #keyboard.add_hotkey("PageDown", self.save_configurations)


    def set_button_colors(self):
        self.save_button.setStyleSheet("background-color: #4CAF50; color: white;")

    def load_configurations(self):
        config = ConfigParser()
        config.read('TSQL.ini')

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

        with open('TSQL.ini', 'w') as configfile:
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
        self.setWindowTitle("SQLTools")
        self.usuarios = self.get_users()
        self.login_dialog = LoginDialog()
        #self.setWindowIcon(QIcon("sqlIco.ico")) 
        
        icon_base64 = """
        
        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
        
        
        """
        
        icon_data = base64.b64decode(icon_base64)
        self.icon_pixmap = QtGui.QPixmap()
        self.icon_pixmap.loadFromData(icon_data)
        self.setWindowIcon(QIcon(self.icon_pixmap))   
        

        if self.login_dialog.exec_() != QDialog.Accepted:
            sys.exit()

        self.center_on_screen()
        self.setup_connections()
        self.setup_shortcuts()

     
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        
        self.setFixedSize(self.size())
        

        self.set_styles()
        
    def logout(self):
       
        self.login_dialog = LoginDialog()
        if self.login_dialog.exec_() == QDialog.Accepted:
            
            self.clear_main_window()

    def clear_main_window(self):
        
        self.query_entry.clear()
        self.result_text.clear()
    
        
    def set_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000000;
                color: white;
                font-family: Arial;
                font-size: 14px;
            }
            QToolBar {
                background-color: #000000;
                color: white;
            }
            QPushButton {
                background-color: green;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: red;
            }
            QLineEdit, QPlainTextEdit, QComboBox, QListWidget {
                background-color: #000000;
                color: white;
                border: 1px solid #555;
            border-radius: 4px;
                padding: 5px;
            }
            QLabel {
            color: red;
        }
        """)

    def get_users(self):
        return {
            
            
            "PAIVA": {
        "password": "PVA"
    },
    "MATHEUS": {
        "password": "MTH"
    },
    "KELTON": {
        "password": "KTL"
    },
    "WLADIMIR": {
        "password": "WLD"
    },
    "VICTOR": {
        "password": "VTR"
    },
    "WELDER": {
        "password": "2507"
    },
    "RODRIGO": {
        "password": "RDO"
    },
    "SERGIO": {
        "password": "GwTQ"
    }
        }

    def setup_connections(self):
        self.execute_button.clicked.connect(self.executar_consulta)
        self.clear_button.clicked.connect(self.limpar_resultado)
        self.exit_button.clicked.connect(self.sair)
        self.config_button.clicked.connect(self.abrir_configuracao_servidor)

    def setup_shortcuts(self):
        self.shortcut_f5 = QShortcut(QKeySequence("F5"), self)
        self.shortcut_f5.activated.connect(self.executar_consulta)

        self.shortcut_f6 = QShortcut(QKeySequence("F6"), self)
        self.shortcut_f6.activated.connect(self.limpar_resultado)

        self.shortcut_esc = QShortcut(QKeySequence("F10"), self)
        self.shortcut_esc.activated.connect(self.sair)

        self.shortcut_f7 = QShortcut(QKeySequence("F7"), self)
        self.shortcut_f7.activated.connect(self.abrir_configuracao_servidor)

        self.shortcut_pgdwn = QShortcut(QKeySequence("PageDown"),self)
        #self.save_button.clicked.connect(self.save_configurations)
        
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
        senha = self.login_dialog.password_entry.text()

        
        usuarios = self.get_users()
        
        if usuario in usuarios and usuarios[usuario]['password'] == senha:
            return True
        else:
            self.show_critical_message("Autenticação Falhou", "Usuário ou senha inválidos.")
            return False

    def registrar_log(self, usuario,comando, servidor=None, erro=None):
        caminho_log = 'TSQL.wrs'
        caminho_backup = 'C:/Program Files/TSQL/logs'

        if not os.path.exists(caminho_backup):
            os.makedirs(caminho_backup)

        with open(caminho_log, 'a') as arquivo_log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if servidor:
                arquivo_log.write(f'{timestamp} - Conectado - {servidor} -\n')
            if comando:
                arquivo_log.write(f'{timestamp} - {usuario} - {comando}\n')
            if erro:
                arquivo_log.write(f'{timestamp} - {usuario} - {erro}\n')

        caminho_backup_log = os.path.join(caminho_backup, 'TSQL.wrs')
        shutil.copy2(caminho_log, caminho_backup_log)

    def executar_consulta(self):
        
        # self.setWindowIcon(QIcon("sqlIco.ico")) 
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

        if not os.path.exists('TSQL.ini'):
            config['SQLServer'] = {
                'server': '',
                'database': '',
                'username': '',
                'password': ''
            }

            with open('TSQL.ini', 'w') as configfile:
                config.write(configfile)
        else:
            config.read('TSQL.ini')

        return config

    def conectar_bd(self):
        config = self.ler_ou_criar_configuracoes()
        server = config['SQLServer']['server']
        database = config['SQLServer']['database']
        username = config['SQLServer']['username']
        password = config['SQLServer']['password']

        usuario = self.login_dialog.user_entry.text().upper()
        self.registrar_log(usuario, None, server)

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
        msg.setStyleSheet("QLabel{color: red;}")
        self.setWindowIcon(QIcon("src/icons/sqlIco.ico")) 
        msg.exec_()

    def abrir_configuracao_servidor(self):
        config_dialog = ServerConfigDialog(self)
        #config_dialog.setStyleSheet("color: white;")
        config_dialog.exec_()

    
    def closeEvent(self, event):
    
      msg_box = QMessageBox(self)
      msg_box.setWindowTitle("Fechar Aplicação")
      msg_box.setText("Tem certeza que deseja sair?")

    
      btn_sim = msg_box.addButton("Sim", QMessageBox.YesRole)
      btn_nao = msg_box.addButton("Não", QMessageBox.NoRole)

    
      btn_sim.setStyleSheet("background-color: blue; color: white; padding: 5px 10px; font-size: 14px;")
      btn_nao.setStyleSheet("background-color: red; color: white; padding: 5px 10px; font-size: 14px;")

    
      msg_box.exec_()

      if msg_box.clickedButton() == btn_sim:
        event.accept()
      else:
        event.ignore()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SQLTerminalApp()
    window.show()
    sys.exit(app.exec_())

