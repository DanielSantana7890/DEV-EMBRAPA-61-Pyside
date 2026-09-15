#=============================================================
#TASK 5 (SPRINT 1) by: Arthur Ferraz
#=============================================================

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication
import sys

class PopupAcaoAtualizada(QWidget):
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
            background-color: #C4E1FF;
            border-radius: 119px;
            font-size: 95px;
            color: #356394;
        }
        """

        ESTILO_Titulo = """
        QLabel {
            background: white;
            font-size: 34px;
            font-family: Verdana;
            font-weight: bold;
            color: black;
        }
        """

        ESTILO_Mensagem1 = """
        QLabel {
            background: white;
            font-size: 24px;
            font-family: Verdana;
            color: black;
        }
        """

        ESTILO_Botao = """
        QPushButton {
            background-color: #172b8c;
            color: white;
            border: none;
            border-radius: 28px;
            font-size: 23px;
        }
        QPushButton:hover {
            background-color: #056510;
        }
        QPushButton:pressed {
            background-color: #056510;
        }
        """

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Ação atualizada")
        self.setFixedSize(1200, 640)
        self.setStyleSheet(ESTILO_Geral)

        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.resize(1200, 640)

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        circulo = QLabel("✓")
        circulo.setFixedSize(238, 238)
        circulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        circulo.setStyleSheet(ESTILO_Circulo)

        titulo = QLabel("Sua ação foi atualizada!")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(ESTILO_Titulo)

        msg1 = QLabel("Sua ação foi reenviada para os avaliadores.")
        msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg1.setStyleSheet(ESTILO_Mensagem1)

        botao = QPushButton("Fechar")
        botao.setFixedSize(285, 56)
        botao.setStyleSheet(ESTILO_Botao)
        botao.clicked.connect(self.close)

        layout.addWidget(circulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(35)
        layout.addWidget(titulo)
        layout.addSpacing(10)
        layout.addWidget(msg1)
        layout.addSpacing(50)
        layout.addWidget(botao, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    janela = PopupAcaoAtualizada()
    janela.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()