from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QVBoxLayout, QShortcut, QLineEdit, QToolBar, QPushButton, QAction, QListWidget, QFormLayout, QCheckBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5 import QtGui
import sys
import os
from PyQt5.QtCore import Qt 
import ctypes
import datetime
import shutil
import base64
import pyodbc
import keyboard
from configparser import ConfigParser

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
        self.user_entry.textChanged.connect(self.on_text_changed)
        #self.setWindowIcon(QIcon("sql.ico")) 
        
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
            
        "PAIVA": "VLSSL",
            
            "MATHEUS": "@Mt.20.24",
            "KELTON": "mint@osint",
            "WLADIMIR": "",
            "VICTOR": "vilaça@victor.",
            "WELDER": "2507",
            "RODRIGO": "NRODRIGO@@2011",
            "SERGIO": "@@s.gabriel24",
            "VALDENISIA": "val@@@25"
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
        self.setWindowTitle("SQL Terminal")
        self.usuarios = self.get_users()
        self.login_dialog = LoginDialog()
        #self.setWindowIcon(QIcon("sql.ico")) 
        
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
                "password": "VLSSL"
            },
            "LEVY": {
                "password": "LevY@Nunes"
            },
            "MATHEUS": {
                "password": "@Mt.20.24"
            },
            "KELTON": {
                "password": "Mint@oSint"
            },
            "WLADIMIR": {
                "password": "Niver@@@2000"
            },
            "VICTOR": {
                "password": "Vilaça@Victor."
            },
            "WELDER": {
                "password": "2507"
            },
            "RODRIGO": {
                "password": "nRODRIGO@@2011"
            },
            "SERGIO": {
                "password": "@@S.gabriel24"
            },
            "VALDENISIA": {
                "password": "val@@@25"
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

    def registrar_log(self, usuario, comando, servidor=None, erro=None):
        caminho_log = 'TSQL.wrs'
        caminho_backup = 'C:/Program Files/TSQL/logs'

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

        caminho_backup_log = os.path.join(caminho_backup, 'TSQL.wrs')
        shutil.copy2(caminho_log, caminho_backup_log)

    def executar_consulta(self):
        
        # self.setWindowIcon(QIcon("sql.ico")) 
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
        self.setWindowIcon(QIcon("sql.ico")) 
        msg.exec_()

    def abrir_configuracao_servidor(self):
        config_dialog = ServerConfigDialog(self)
        config_dialog.setStyleSheet("color: green;")
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

