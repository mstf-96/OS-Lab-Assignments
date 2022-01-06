from math import *
from functools import partial
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()

        # CONNECT NUMS
        self.ui.btn_0.clicked.connect(partial(self.num_clicked, "0"))
        self.ui.btn_1.clicked.connect(partial(self.num_clicked, "1"))
        self.ui.btn_2.clicked.connect(partial(self.num_clicked, "2"))
        self.ui.btn_3.clicked.connect(partial(self.num_clicked, "3"))
        self.ui.btn_4.clicked.connect(partial(self.num_clicked, "4"))
        self.ui.btn_5.clicked.connect(partial(self.num_clicked, "5"))
        self.ui.btn_6.clicked.connect(partial(self.num_clicked, "6"))
        self.ui.btn_7.clicked.connect(partial(self.num_clicked, "7"))
        self.ui.btn_8.clicked.connect(partial(self.num_clicked, "8"))
        self.ui.btn_9.clicked.connect(partial(self.num_clicked, "9"))

        # CONNECT ONE OPERAND MATH FUNCTIONS
        self.ui.btn_sin.clicked.connect(partial(self.one_operand, "sin"))
        self.ui.btn_cos.clicked.connect(partial(self.one_operand, "cos"))
        self.ui.btn_tan.clicked.connect(partial(self.one_operand, "tan"))
        self.ui.btn_cot.clicked.connect(partial(self.one_operand, "cot"))
        self.ui.btn_sqrt.clicked.connect(partial(self.one_operand, "sqrt"))

        # CONNECT TWO OPERAND MATH FUNCTIONS
        self.ui.btn_add.clicked.connect(partial(self.two_operand, "add"))
        self.ui.btn_sub.clicked.connect(partial(self.two_operand, "sub"))
        self.ui.btn_mul.clicked.connect(partial(self.two_operand, "mul"))
        self.ui.btn_div.clicked.connect(partial(self.two_operand, "div"))
        self.ui.btn_pow.clicked.connect(partial(self.two_operand, "pow"))
        self.ui.btn_log.clicked.connect(partial(self.two_operand, "log"))
        self.ui.btn_remainder.clicked.connect(partial(self.two_operand, "remainder"))

        #########
        self.ui.btn_equal.clicked.connect(partial(self.equal))
        self.ui.btn_clear.clicked.connect(partial(self.clear))
        self.ui.btn_dot.clicked.connect(partial(self.dot))
        
        

    def num_clicked(self,num):
        self.ui.lbl_output.setText(self.ui.lbl_output.text() + num)

    def one_operand(self,func):
        if self.ui.lbl_output.text() != '':
            teta = radians(float(self.ui.lbl_output.text()))
            if func == 'sin':
                result = sin(teta)
            elif func == 'cos':
                result = cos(teta)
            elif func == 'tan':
                result = tan(teta)
            elif func == 'cot':
                result = 1 / tan(teta)
            elif func == 'sqrt':
                result = sqrt(float(self.ui.lbl_output.text()))

            result = round(result, 5)
            self.ui.lbl_output.setText(str(result))

    def two_operand(self,operator):
        if self.ui.lbl_output.text() != '':
            self.num1 = float(self.ui.lbl_output.text())
            self.ui.lbl_output.setText('')
            self.operator = operator

    def equal(self):
        if self.ui.lbl_output.text() != '':
            self.num2 = float(self.ui.lbl_output.text())

            if self.operator == 'add':
                result = self.num1 + self.num2
            
            elif self.operator == 'sub':
                result = self.num1 - self.num2
            
            elif self.operator == 'mul':
                result = self.num1 * self.num2
            
            elif self.operator == 'div':
                result = self.num1 / self.num2
            
            elif self.operator == 'pow':
                result = self.num1 ** self.num2
            
            elif self.operator == 'log':
                result = log(self.num1 , self.num2)
            
            elif self.operator == 'remainder':
                result = self.num1 % self.num2
            
            result = round(result, 5)
            self.ui.lbl_output.setText(str(result))

    def dot(self):
        if "." not in self.ui.lbl_output.text() and self.ui.lbl_output.text() != '':
            self.ui.lbl_output.setText(self.ui.lbl_output.text() + ".")

    def clear(self):
        self.ui.lbl_output.setText('')



if __name__ == "__main__":
    my_app = QApplication()
    main_window = Calculator()
    my_app.exec()
