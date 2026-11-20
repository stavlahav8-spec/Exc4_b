import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout


IMAGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "my_picture.jpeg",
)
IMAGE_DISPLAY_SIZE = 210


class AboutWindow(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("About Me")
        self.setObjectName("aboutWindow")
        self.setMinimumSize(360, 430)
        self.resize(380, 450)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(12)

        self.image_label = QLabel(self)
        pixmap = QPixmap(IMAGE_PATH)
        device_pixel_ratio = self.devicePixelRatioF()
        pixmap_size = round(IMAGE_DISPLAY_SIZE * device_pixel_ratio)
        scaled_pixmap = pixmap.scaled(
            pixmap_size,
            pixmap_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        scaled_pixmap.setDevicePixelRatio(device_pixel_ratio)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        self.name_label = QLabel("Stav Lahav")
        self.name_label.setObjectName("aboutName")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.name_label.setFont(font)
        self.name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.name_label)

        self.email_label = QLabel("Email: stav.lahav8@gmail.com")
        font_small = QFont()
        font_small.setPointSize(12)
        self.email_label.setFont(font_small)
        self.email_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.email_label)

        self.link_label = QLabel(
            '<a href="https://www.linkedin.com/in/stav-lahav">'
            "My LinkedIn Profile</a>"
        )
        self.link_label.setObjectName("aboutLink")
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setFont(font_small)
        self.link_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.link_label)

        self.github_label = QLabel(
            '<a href="https://github.com/stavlahav8-spec/Exc4_b">'
            "GitHub repository</a>"
        )
        self.github_label.setObjectName("aboutLink")
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setFont(font_small)
        self.github_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.github_label)

