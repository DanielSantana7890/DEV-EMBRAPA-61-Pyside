#=============================================================
# TASK 30 (SPRINT 1) by: Theo
#=============================================================

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication
import sys

class PopupDeAvisoDeAnoCriado(QWidget):
    def __init__(self):
        super().__init__()

        ESTILO_Geral = """
        #container {
            background-color: white;
            border-radius: 30px;
            border: 1px solid #d1d5db;
        }
        """

        ESTILO_Circulo = """
        QLabel {
            background-color: #d9ebff;
            border-radius: 105px;
            font-size: 90px;
            color: #1f2d87;
        }
        """

        ESTILO_Titulo = """
        QLabel {
            background: white;
            font-size: 30px;
            font-weight: 700;
            color: #222;
        }
        """

        ESTILO_Mensagem1 = """
        QLabel {
            background: white;
            font-size: 21px;
            color: #444;
        }
        """

        ESTILO_Mensagem2 = """
        QLabel {
            background: white;
            font-size: 18px;
            color: #777;
        }
        """

        ESTILO_Botao = """
        QPushButton {
            background-color: #1f2d87;
            color: white;
            border: none;
            border-radius: 28px;
            font-size: 18px;
        }
        QPushButton:hover {
            background-color: #2a3cb0;
        }
        """

        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Sucesso")
        self.setFixedSize(1000, 650)
        self.setStyleSheet(ESTILO_Geral)

        
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.resize(1000, 550)

        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        
        circulo = QLabel("✓")
        circulo.setFixedSize(210, 210)
        circulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        circulo.setStyleSheet(ESTILO_Circulo)

        titulo = QLabel("O ano foi criado!")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(ESTILO_Titulo)

        msg1 = QLabel("Ano adicionado ao sistema com sucesso!")
        msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg1.setStyleSheet(ESTILO_Mensagem1)

        
        botao = QPushButton("Fechar")
        botao.setFixedSize(370, 56)
        botao.setStyleSheet(ESTILO_Botao)
        botao.clicked.connect(self.close)

        
        layout.addWidget(circulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(35)
        layout.addWidget(titulo)
        layout.addSpacing(10)
        layout.addWidget(msg1)
        layout.addSpacing(5)
        layout.addSpacing(50)
        layout.addWidget(botao, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)
        
            
def main():
    app = QApplication(sys.argv)

    janela = PopupDeAvisoDeAnoCriado()
    janela.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()