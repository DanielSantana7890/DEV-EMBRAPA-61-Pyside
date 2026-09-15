#============================================================
#TASK 84 (Sprint 1) by: Victor
#============================================================

import sys, os      # Está linha deve ser removida no futuro e está aqui apenas para a reprodução do sistema
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QButtonGroup
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT_DIR = sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout_menu_lateral import btn_layout_menu_lateral_

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class menu_pesquisador(QMainWindow):
    def __init__(self):
        super().__init__()

        menu = QWidget()
        self.setCentralWidget(menu)

        main_layout = QHBoxLayout(menu)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_lateral = QFrame()
        self.menu_lateral.setObjectName("menu_lateral")
        self.menu_lateral.setFixedWidth(280)
        self.menu_lateral.setStyleSheet("background-color: #356394;")

        menu_lateral_layout = QVBoxLayout(self.menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout_menu_lateral_ (os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_acoes = btn_layout_menu_lateral_ (os.path.join(BASE, "Imagens/Ações-Icone.png"), "Minhas Ações")

        logo_label = QLabel ()
        logo = QPixmap (LOGO)
        logo_certa = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        
        menu_lateral_layout.addStretch()

        main_layout.addWidget(self.menu_lateral)

# O conteudo abaixo deve ser removida no futuro e está aqui apenas para a reprodução do sistema
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = menu_pesquisador()
    janela.show()
    sys.exit(app.exec())