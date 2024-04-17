import sys

from PySide6 import QtWidgets
from PyQt6 import uic
from PySide6.QtWidgets import QLabel, QLineEdit, QApplication, QPushButton, QMainWindow



from start_screen import Ui_StartWindow
from set_name_screen import Ui_SetNameWindow
from game_screen import Ui_GameScreen


# Класс начального экрана
class StartScreen(QMainWindow):
    # Конструктор
    def __init__(self):
        super(StartScreen, self).__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)

        # Поиск кнопок, чтобы задать их
        self.startButton = self.findChild(QPushButton, "startButton")
        self.exitButton = self.findChild(QPushButton, "exitButton")
        
        # Назначение функций на кнопки
        self.startButton.clicked.connect(self.gotoSetNameScreen)
        self.exitButton.clicked.connect(self.endProgram)
        
    # Метод для кнопки, выполняющий выход из программы
    def endProgram(self):
        sys.exit()
    
    # Метод для кнопки, выполняющий переход со стартового экрана на экран выбора имён
    def gotoSetNameScreen(self):
        setName = SetNameScreen()
        widget.addWidget(setName)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    

# Класс окна в котором ставятся имена и выбираются стороны
class SetNameScreen(QMainWindow):
    # Конструктор
    def __init__(self):
        super(SetNameScreen, self).__init__()
        self.ui = Ui_SetNameWindow()
        self.ui.setupUi(self)

        # Объявление переменных, в которых потом будут храниться имена игроков
        self.playerX_name = ""
        self.player0_name = ""
        
        # Поиск полей, чтобы задать их
        self.lineX = self.findChild(QLineEdit, "lineX")
        self.line0 = self.findChild(QLineEdit, "line0")

        # Поиск кнопок, чтобы задать их и присваивание функций на эти кнопки
        self.startButton = self.findChild(QPushButton, "startButton")
        self.startButton.clicked.connect(self.gotoGameScreen)
        self.enterPlayerX = self.findChild(QPushButton, "enterPlayerX")
        self.enterPlayerX.clicked.connect(self.convertPlayerX)
        self.enterPlayer0 = self.findChild(QPushButton, "enterPlayer0")
        self.enterPlayer0.clicked.connect(self.convertPlayer0)

    # Метод, выполняющий переход на игровой экран
    def gotoGameScreen(self):
        game = GameScreen(self.playerX_name, self.player0_name)
        widget.addWidget(game)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # Метод, который считывает введённое имя игрока за X
    def convertPlayerX(self):
        self.playerX_name = self.lineX.text()
        print(self.playerX_name)
        
    # Метод, который считывает введённое имя игрока за 0    
    def convertPlayer0(self):
        self.player0_name = self.line0.text()
        print(self.player0_name)
        

# Класс с игровым полем в крестики-нолики
class GameScreen(QMainWindow):
    # Конструктор
    def __init__(self, playerX_name, player0_name):
        super(GameScreen, self).__init__()
        self.ui = Ui_GameScreen()
        self.ui.setupUi(self)

        # Поиск элементов, чтобы задать их
        self.exitButton = self.findChild(QPushButton, "exitButton")
        self.exitButton.clicked.connect(self.endProgram)
        self.playerX = self.findChild(QLabel, "playerX")
        self.player0 = self.findChild(QLabel, "player0")

        self.playerX.setText(playerX_name)
        self.player0.setText(player0_name)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.gotoSetNameScreen)

        self.resetButton = self.findChild(QPushButton, "resetButton")
        self.resetButton.clicked.connect(self.resetGame)

        self.scorePlayerX = self.findChild(QLabel, "scorePlayerX")
        self.scorePlayer0 = self.findChild(QLabel, "scorePlayer0")
        self.scoreX = 0
        self.score0 = 0

        # Флаг, для определение того кто делает ход
        self.flag = 0

        # Определение кнопок, которые отвечают за поля
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")

        # Определение функций для этих кнопок
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))

    # Метод, завершающий программу
    def endProgram(self):
        sys.exit()

    # Метод, выполняющий переход на экран в котором задаются имена игроков
    def gotoSetNameScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        
    # Метод, отвечающий за отображение X или 0 на кнопке, в зависимости от хода игрока    
    def clicker(self, button):
        if (self.flag % 2 == 0):
            text = "X"
            button.setStyleSheet('QPushButton {color: blue;}')
        else:
            text = "0"
            button.setStyleSheet('QPushButton {color: red;}')

        self.flag += 1
        button.setText(text)
        button.setEnabled(False)
        self.checkWin()
        # Вызов ничьи, если количество ходов окончено
        if (self.flag == 9):
            self.draw()

    # Метод, выполняющий проверку на победу, и вызывающий соответсвующий метод в случае выполнения условия
    def checkWin(self):
        # Верхний ряд
        if (self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text()):
            self.win(self.button1, self.button4, self.button7)
        # Средний ряд
        if (self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text()):
            self.win(self.button2, self.button5, self.button8)
        # Нижний ряд
        if (self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text()):
            self.win(self.button3, self.button6, self.button9)
        # Диагональ убывающая
        if (self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text()):
            self.win(self.button1, self.button5, self.button9)
        # Диагониль возрастающая
        if (self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text()):
            self.win(self.button3, self.button5, self.button7)
        # Левый столбец
        if (self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text()):
            self.win(self.button1, self.button2, self.button3)
        # Средний столбец
        if (self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text()):
            self.win(self.button4, self.button5, self.button6)
        # Правый столбец
        if (self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text()):
            self.win(self.button7, self.button8, self.button9)
        
    # Метод, вызывающийся при победе
    def win(self, b1, b2, b3):
        b1.setStyleSheet('QPushButton {color: green;}')
        b2.setStyleSheet('QPushButton {color: green;}')
        b3.setStyleSheet('QPushButton {color: green;}')

        self.flag = 0        
        
        if (b1.text() == "X"):
            self.scoreX += 1
            self.scorePlayerX.setText(str(self.scoreX))
        else:
            self.score0 += 1
            self.scorePlayer0.setText(str(self.score0))
        
        self.disableButtons()

    # Метод, отключающий все кнопки на поле для игры
    def disableButtons(self):
        buttonArr = [self.button1, self.button2, self.button3,
                     self.button4, self.button5, self.button6,
                     self.button7, self.button8, self.button9]
        
        for b in buttonArr:
            b.setEnabled(False)

    # Метод, перезапускающий игру
    def resetGame(self):
        buttonArr = [self.button1, self.button2, self.button3,
                     self.button4, self.button5, self.button6,
                     self.button7, self.button8, self.button9]
        for b in buttonArr:
            b.setText("")
            b.setEnabled(True)
        self.flag = 0

    # Метод, вызывающийся при ничье
    def draw(self):
        self.reset()


# Функция main
if __name__ in '__main__':
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    start = StartScreen()
    
    widget.addWidget(start)
    
    widget.setFixedSize(500, 650)
    widget.setWindowTitle("Крестики-нолики")
    widget.show()
    

    app.exec()