import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')

        self.current_player = 'X'
        self.board = [' '] * 9

        self.buttons = []
        for i in range(9):
            button = QPushButton(self)
            button.clicked.connect(lambda _, i=i: self.buttonClicked(i))
            self.buttons.append(button)

        self.turn_label = QLabel(self)
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setFont(QFont('Arial', 16))
        self.turn_label.setText(f'Ходит игрок {self.current_player}')

        layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                layout.addWidget(self.buttons[i*3+j], i, j)

        layout.addWidget(self.turn_label, 3, 0, 1, 3)

        self.setLayout(layout)

        self.resize(350, 350)
        self.show()

    def buttonClicked(self, index):
        if self.board[index] != ' ':
            return

        self.board[index] = self.current_player
        self.buttons[index].setText(self.current_player)

        # изменяем цвет кнопки в зависимости от значения текущего игрока
        if self.current_player == 'X':
            self.buttons[index].setStyleSheet('background-color: red')
        else:
            self.buttons[index].setStyleSheet('background-color: green')

        if self.checkWin():
            QMessageBox.about(self, 'Победа!', f'Игрок {self.current_player} выиграл!')
            self.close()
        elif self.checkTie():
            QMessageBox.about(self, 'Ничья!', 'Ничья!')
            self.close()
        else:
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            self.turn_label.setText(f'Ходит игрок {self.current_player}')

    def checkWin(self):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True
        return False

    def checkTie(self):
        for i in range(9):
            if self.board[i] == ' ':
                return False
        return True

def resizeEvent(self, event):
    # вызываем метод родительского класса
    super().resizeEvent(event)

    # получаем размер виджета
    widget_size = min(event.size().width(), event.size().height())

    # проверяем, существуют ли все кнопки
    if not all(button.isVisible() for button in self.buttons):
        print('Не существуют')
        # удаляем старые кнопки
        for button in self.buttons:
            button.deleteLater()

        # создаем новые кнопки
        button_size = widget_size
        button_font_size = button_size / 2
        font = self.font()
        font.setPointSizeF(button_font_size)
        self.buttons = []
        for i in range(9):
            button = QtWidgets.QPushButton(self)
            button.setFixedSize(button_size, button_size)
            button.setFont(font)
            button.clicked.connect(lambda _, index=i: self.handleButtonClicked(index))
            self.buttons.append(button)

    # устанавливаем размер кнопок
    button_size = widget_size/10
    for i in range(9):
        self.buttons[i].setFixedSize(button_size, button_size)

    # устанавливаем размер шрифта кнопок
    button_font_size = button_size / 2
    font = self.font()
    font.setPointSizeF(button_font_size)
    for i in range(9):
        self.buttons[i].setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tictactoe = TicTacToe()
    sys.exit(app.exec_())
