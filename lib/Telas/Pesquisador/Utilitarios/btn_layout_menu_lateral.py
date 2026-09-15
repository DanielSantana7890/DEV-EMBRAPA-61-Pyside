#============================================================
#TASK 84 (Sprint 1) by: Victor
#============================================================

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel

class btn_layout_menu_lateral_(QPushButton):
    def __init__(self, path, texto, parent=None):
        super().__init__(parent)

        self.setStyleSheet ("""
            QPushButton {
                height: 50px;
                padding: 10px;
                border: none;
                background-color: transparent;
                border-top-left-radius: 20px;
                border-bottom-left-radius: 20px;
            }
                           
            QPushButton:hover {
                background-color: #4A7AB0;
            }
                           
            QLabel {
                background-color: transparent;
                text-align: center;
                font-family: Verdana;
                font-weight: bold;
                color: white;
                font-size: 20px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 10, 0)

        self.icone_label = QLabel()
        self.icone_label.setPixmap(QIcon(path).pixmap(QSize(23, 25)))

        self.texto_label = QLabel(texto)
        self.texto_label.setAlignment(Qt.AlignCenter)

        self.icone_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.texto_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        layout.addWidget(self.icone_label)
        layout.addStretch()
        layout.addWidget(self.texto_label)
        layout.addStretch()

    def setText(self, texto):
        super().setText(texto)
        self.texto_label.setText(texto)
        
    def setIcon(self, icone_path, size=QSize(23, 25)):
        self.icone_label.setPixmap(QIcon(icone_path).pixmap(size))