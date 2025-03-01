# minecraft launcher interface
# Fungi minecraft launcher
# made by @blackbucket007

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from launcher import start_minecraft

class MinecraftLauncherView(QWidget):
    """Главное представление лаунчера"""
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """Инициализация UI интерфейса в лаунчере"""
        self.setWindowTitle("Fungi Minecraft launcher")
        self.setGeometry(300, 300, 300, 150)

        layout = QVBoxLayout()

        # Поле ввода никнейма
        self.label = QLabel("Введите никнейм:")
        layout.addWidget(self.label)

        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        # Кнопка запуска
        self.start_button = QPushButton("Запустить Minecraft")
        self.start_button.clicked.connect(self.run_minecraft)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        
    def run_minecraft(self):
        """Запуск minecraft c введением пользователем никнейма"""
        player_name = self.username_input.text().strip()
        result = start_minecraft(player_name)
        
        if "Ошибка" in result:
            QMessageBox.critical(self, "Ошибка", result)
        else:
            QMessageBox.information(self, "Запуск", result)
            
# Запуск UI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher_view = MinecraftLauncherView()
    launcher_view.show()
    sys.exit(app.exec())