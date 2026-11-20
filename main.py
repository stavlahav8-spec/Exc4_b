import os
import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from about_window import AboutWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.temperatures = []
        self.revenues = []
        self.selected_file = ""
        self.about_window = None

        self.setWindowTitle("Ice Cream Sales Revenue")
        self.setMinimumSize(820, 600)
        self.resize(1024, 720)

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(32, 28, 32, 28)
        central_layout.setSpacing(22)

        header_layout = QHBoxLayout()
        title_block = QVBoxLayout()
        title_block.setSpacing(4)

        title = QLabel("Ice Cream Sales Revenue")
        title.setObjectName("pageTitle")
        subtitle = QLabel("Explore how temperature relates to daily sales.")
        subtitle.setObjectName("pageSubtitle")
        title_block.addWidget(title)
        title_block.addWidget(subtitle)
        header_layout.addLayout(title_block)
        header_layout.addStretch()

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.clicked.connect(self.on_about)
        header_layout.addWidget(self.about_button)
        central_layout.addLayout(header_layout)

        chart_card = QFrame()
        chart_card.setObjectName("chartCard")
        chart_layout = QVBoxLayout(chart_card)
        chart_layout.setContentsMargins(20, 18, 20, 16)
        chart_layout.setSpacing(10)

        chart_heading = QHBoxLayout()
        chart_title = QLabel("Revenue by temperature")
        chart_title.setObjectName("chartTitle")
        chart_heading.addWidget(chart_title)
        chart_heading.addStretch()

        self.load_button = QPushButton("Load CSV File")
        self.load_button.setObjectName("primaryButton")
        self.load_button.clicked.connect(self.on_load_file)
        chart_heading.addWidget(self.load_button)
        chart_layout.addLayout(chart_heading)

        self.figure = Figure(figsize=(8, 5), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        chart_layout.addWidget(self.toolbar)
        chart_layout.addWidget(self.canvas, stretch=1)
        central_layout.addWidget(chart_card, stretch=1)

        self.setCentralWidget(central_widget)
        self.plot_graph()

    def on_load_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load CSV File",
            "",
            "CSV files (*.csv)",
        )
        if file_path:
            self.selected_file = file_path
            # TODO: Read the CSV into self.temperatures and self.revenues, then call self.plot_graph().

    def on_about(self) -> None:
        self.about_window = AboutWindow(self)
        self.about_window.show()

    def plot_graph(self) -> None:
        temperatures = [10, 15, 20, 25, 30, 35]
        revenues = [120, 180, 260, 340, 430, 510]

        self.figure.clear()
        axes = self.figure.add_subplot(111)
        axes.plot(
            temperatures,
            revenues,
            color="#4b9ca8",
            linewidth=2.5,
            marker="o",
            markersize=7,
            markerfacecolor="#f4a261",
        )
        axes.set_title("Ice Cream Sales Revenue", loc="left", pad=16)
        axes.set_xlabel("Temperature (°C)")
        axes.set_ylabel("Revenue")
        axes.grid(True, color="#e5edf0", linewidth=0.8)
        axes.set_axisbelow(True)
        axes.spines["top"].set_visible(False)
        axes.spines["right"].set_visible(False)
        axes.spines["left"].set_color("#c8d6dc")
        axes.spines["bottom"].set_color("#c8d6dc")
        axes.tick_params(colors="#536872")
        self.figure.tight_layout()
        self.canvas.draw()


def main() -> None:
    app = QApplication(sys.argv)
    stylesheet_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    with open(stylesheet_path, encoding="utf-8") as stylesheet_file:
        app.setStyleSheet(stylesheet_file.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
