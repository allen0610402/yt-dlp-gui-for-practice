import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class DownloadGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Download Video")
        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit()
        self.path_label = QLabel("Save Path:")
        self.path_input = QLineEdit()
        self.path_button = QPushButton("Choose Path")
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download)
        self.path_button.clicked.connect(self.choose_path)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.url_label)
        vbox1.addWidget(self.url_input)
        vbox1.addWidget(self.path_label)
        vbox1.addWidget(self.path_input)
        vbox1.addWidget(self.path_button)
        vbox1.addWidget(self.download_button)
        self.setLayout(vbox1)

    def choose_path(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        if file_dialog.exec_():
            directory = file_dialog.selectedFiles()[0]
            self.path_input.setText(directory)

    def download(self):
        cmd = f"yt-dlp -o {self.path_input.text()}/download {self.url_input.text()}"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloadGUI()
    window.show()
    sys.exit(app.exec_())
