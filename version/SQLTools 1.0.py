import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, \
    QMessageBox, QSizePolicy, QHBoxLayout, QLineEdit, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pyodbc
import os
from configparser import ConfigParser
import ctypes
import datetime
import shutil


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        # Configure o estilo diretamente para a QDialog
        self.setStyleSheet("QDialog { background-color: black; color: white; }")

        # Adicione um layout QVBoxLayout para organizar os widgets
        layout = QVBoxLayout(self)

        self.user_label = QLabel("Usuário:", self)
        self.user_label.setStyleSheet("color: white;")  # Adicione esta linha para definir a cor do texto

        self.user_entry = QLineEdit(self)
        self.user_entry.setStyleSheet("background-color: black; color: white;")
        self.user_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.password_label = QLabel("Senha:", self)
        self.password_label.setStyleSheet("color: white;")  # Adicione esta linha para definir a cor do texto

        self.password_entry = QLineEdit(self)
        self.password_entry.setStyleSheet("background-color: black; color: white;")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("background-color: green; color: white;")
        self.login_button.clicked.connect(self.login)
        self.login_button.setFixedSize(300, 30)

        # Adicione os widgets ao layout
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)

        # Adicione o seguinte código para ajustar as propriedades de exibição do widget
        self.setModal(True)

        # Ajuste manual da posição da tela de login
        self.setGeometry(500, 300, 300, 200)

    def login(self):
        user = self.user_entry.text().upper()
        password = self.password_entry.text()

        # COLOCAR OS USUÁRIOS PERMITIDOS COM SUAS SENHAS
        # elif user == "USUARIO" and password == "SENHA":
        # self.accept()

        credentials = {
            "ADMIN": "DBA@@9633"
}
        if user in credentials and password == credentials[user]:
           self.accept()
        else:
           QMessageBox.critical(self, "Login Falhou", "Usuário ou senha inválidos")			
			

class SQLTerminalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Adicionar ícone à janela
        try:
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        except AttributeError:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "sql.ico")

        if not os.path.exists(icon_path):
            icon_path = os.path.join(os.path.abspath("."), "sql.ico")

        self.setWindowTitle("SQL Terminal")
        self.setGeometry(100, 100, 800, 400)
        
        # Defina o ícone diretamente no aplicativo
        app.setWindowIcon(QIcon(icon_path))

        if hasattr(sys, '_MEIPASS'):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

        self.usuarios = {
            "ADMIN": "DBA@@9633"
			
        }

        self.login_dialog = LoginDialog()

        # Movendo a chamada para centerOnScreen após exec_()
        result = self.login_dialog.exec_()

        if result != QDialog.Accepted:
            sys.exit()

        # Centralizar a janela principal após o login
        self.centerOnScreen()

        self.query_entry = QTextEdit(self)
        self.query_entry.setStyleSheet("color: green;")
        self.query_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.result_text = QTextEdit(self)
        self.result_text.setStyleSheet("color: green;")
        self.result_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.result_text.setReadOnly(True)
        
        
        self.execute_button = QPushButton("Executar", self)
        self.execute_button.setStyleSheet("background-color: green; color: white;")
        self.execute_button.clicked.connect(self.executar_consulta)
        self.execute_button.setFixedSize(100, 30)

        self.clear_button = QPushButton("Limpar", self)
        self.clear_button.setStyleSheet("background-color: green; color: white;")
        self.clear_button.clicked.connect(self.limpar_resultado)
        self.clear_button.setFixedSize(100, 30)

        self.exit_button = QPushButton("Sair", self)
        self.exit_button.setStyleSheet("background-color: red; color: white;")
        self.exit_button.clicked.connect(self.sair)
        self.exit_button.setFixedSize(100, 30)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.execute_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.exit_button)

        layout = QVBoxLayout()
        layout.addWidget(self.query_entry)
        layout.addWidget(self.result_text)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
    QMainWindow {
        background-color: black;
    }

    QLabel {
        color: black;
    }

    QLineEdit, QTextEdit {
        background-color: black;
        color: green;
    }

    QPushButton {
        background-color: green;
        color: white;
    }

    QPushButton#exitButton {
        background-color: red;
    }
""")

    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                  int((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def sair(self):
        self.close()

    def autenticar_usuario(self):
        usuario = self.login_dialog.user_entry.text().upper()
        senha = self.login_dialog.password_entry.text()

        if usuario in self.usuarios and self.usuarios[usuario] == senha:
            return True
        else:
            QMessageBox.critical(self, "Autenticação Falhou", "Usuário ou senha inválidos.")
            return False

    def registrar_log(self, usuario, comando):
        if self.autenticar_usuario():
            caminho_log = f'SQL.log'
            caminho_backup = 'C:/INFARMA/LOJA/Client/logTools'

            # Verifica se a pasta de backup existe, caso contrário, cria-a
            if not os.path.exists(caminho_backup):
                os.makedirs(caminho_backup)

            with open(caminho_log, 'a') as arquivo_log:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                arquivo_log.write(f'{timestamp}- {usuario} - {comando}\n')

            # Cria um backup do log na pasta
            caminho_backup_log = os.path.join(caminho_backup, f'SQL.log')
            shutil.copy2(caminho_log, caminho_backup_log)

        else:
            QMessageBox.critical(self, "Autenticação Falhou", "Você não está autenticado.")

    def executar_consulta(self):
        if not self.autenticar_usuario():
            return

        conn = self.conectar_bd()
        if conn:
            query = self.query_entry.toPlainText()
            cursor = conn.cursor()

            usuario = self.login_dialog.user_entry.text().upper()
            self.registrar_log(usuario, query)

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

    def limpar_resultado(self):
        self.result_text.clear()

    def ler_ou_criar_configuracoes(self):
        config = ConfigParser()

        if not os.path.exists('configTools.ini'):
            config['SQLServer'] = {
                'server': 'LOCALHOST',
                'database': 'VMD',
                'username': 'VMDApp',
                'password': 'VMD22041748'
            }

            with open('configTools.ini', 'w') as config_file:
                config.write(config_file)
        else:
            config.read('configTools.ini')

        return config['SQLServer']

    def conectar_bd(self):
        config = self.ler_ou_criar_configuracoes()

        server = config['server']
        database = config['database']
        username = config['username']
        password = config['password']

        try:
            conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
            return conn
        except pyodbc.Error as e:
            QMessageBox.critical(self, "Erro de Conexão", f"Não foi possível conectar ao banco de dados: {str(e)}")
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SQLTerminalApp()
    mainWin.show()
    sys.exit(app.exec_())
