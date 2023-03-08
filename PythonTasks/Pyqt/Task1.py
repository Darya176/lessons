"""
С помощью Pyqt создайте калькулятор с графическим интерфейсом.
Приложение должно выполнять: Сложение, вычитание, деление, умножение, возведение в степень, запоминание значения,
вывод значения из памяти.
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 600, 300, 100)


        self.display = QLineEdit('0')


        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_decimal = QPushButton('.')
        self.button_add = QPushButton('+')
        self.button_subtract = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_clear = QPushButton('C')
        self.button_equals = QPushButton('=')
        self.button_exponentiation = QPushButton('x^y')
        self.button_memory_recall = QPushButton('MR')
        self.button_memory_store = QPushButton('MS')



        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.display, 0, 0, 1, 4)
        grid.addWidget(self.button_clear, 1, 3)
        grid.addWidget(self.button_divide, 4, 3)
        grid.addWidget(self.button_multiply, 5, 3)
        grid.addWidget(self.button_7, 2, 0)
        grid.addWidget(self.button_8, 2, 1)
        grid.addWidget(self.button_9, 2, 2)
        grid.addWidget(self.button_subtract, 3, 3)
        grid.addWidget(self.button_4, 3, 0)
        grid.addWidget(self.button_5, 3, 1)
        grid.addWidget(self.button_6, 3, 2)
        grid.addWidget(self.button_add, 2, 3)
        grid.addWidget(self.button_1, 4, 0)
        grid.addWidget(self.button_2, 4, 1)
        grid.addWidget(self.button_3, 4, 2)
        grid.addWidget(self.button_equals, 5, 2)
        grid.addWidget(self.button_exponentiation, 1, 0)
        grid.addWidget(self.button_0, 5, 0)
        grid.addWidget(self.button_decimal, 5, 1)
        grid.addWidget(self.button_memory_store, 1, 1)
        grid.addWidget(self.button_memory_recall, 1, 2)




        self.button_0.clicked.connect(lambda: self.number_clicked('0'))
        self.button_1.clicked.connect(lambda: self.number_clicked('1'))
        self.button_2.clicked.connect(lambda: self.number_clicked('2'))
        self.button_3.clicked.connect(lambda: self.number_clicked('3'))
        self.button_4.clicked.connect(lambda: self.number_clicked('4'))
        self.button_5.clicked.connect(lambda: self.number_clicked('5'))
        self.button_6.clicked.connect(lambda: self.number_clicked('6'))
        self.button_7.clicked.connect(lambda: self.number_clicked('7'))
        self.button_8.clicked.connect(lambda: self.number_clicked('8'))
        self.button_9.clicked.connect(lambda: self.number_clicked('9'))
        self.button_decimal.clicked.connect(lambda: self.number_clicked('.'))
        self.button_add.clicked.connect(lambda: self.operation_clicked('+'))
        self.button_subtract.clicked.connect(lambda: self.operation_clicked('-'))
        self.button_multiply.clicked.connect(lambda: self.operation_clicked('*'))
        self.button_divide.clicked.connect(lambda: self.operation_clicked('/'))
        self.button_exponentiation.clicked.connect(lambda: self.operation_clicked('x^y'))
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_equals.clicked.connect(lambda: self.equals())
        self.button_memory_store.clicked.connect(lambda: self.memory_store())
        self.button_memory_recall.clicked.connect(lambda: self.memory_recall())




        self.operand1 = None
        self.operand2 = None
        self.operation = None
        self.result = None
        self.memory_value = 0


    def number_clicked(self, number):
        entered_text = self.display.text()
        if entered_text == '0':
            self.display.setText(number)
        else:
            self.display.setText(entered_text + number)

    def operation_clicked(self, operation):
        self.operation = operation
        self.operand1 = float(self.display.text())
        self.display.setText('0')

    def clear(self):
        self.operand1 = None
        self.operand2 = None
        self.operation = None
        self.result = None
        self.display.setText('0')

    def equals(self):
        self.operand2 = float(self.display.text())
        if self.operation == '+':
            self.result = self.operand1 + self.operand2
        elif self.operation == '-':
            self.result = self.operand1 - self.operand2
        elif self.operation == '*':
            self.result = self.operand1 * self.operand2
        elif self.operation == '/':
            self.result = self.operand1 / self.operand2
        elif self.operation == 'x^y':
            self.result = self.operand1 ** self.operand2
        self.display.setText(str(self.result))
        self.operand1 = self.result

    def memory_store(self):
        self.memory_value = float(self.display.text())

    def memory_recall(self):
            self.display.setText(str(self.memory_value))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())