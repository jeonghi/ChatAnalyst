import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
#from Apiservice import *
from button import *

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

class Label(QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)

class Text(QTextEdit):

    def __init__(self, text):
        super().__init__()
        self.append(text)

class Analyst(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Emotion Analyst')
        self.drawUi()
        self.show()


    def drawUi(self):
        self.display = QLineEdit()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.v = QVBoxLayout()
        self.v.addWidget(Label('Emotion Analyst'))
        self.inputText = Text('내용을 입력해주세요')
        self.v.addWidget(self.inputText)
        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.h1.addWidget(Button('감정분석', self.buttonClicked))
        self.h1.addWidget(Button('감성분석', self.buttonClicked))
        self.resultText = Label('')
        self.h2.addWidget(self.resultText)
        self.setLayout(self.v)

    def buttonClicked(self):
        sender = self.sender().text()
        query = self.inputText.toPlainText()
        type = btn_type[sender] #btn_type = {'감정분석':0 , '감성분석':1}
        try:
            # json 응답
            result = { 'emotion': '기쁨', 'prob': 98.2535 }
            emotion = result['emotion']
            prob = int(result['prob'])

            self.resultText.setText("상대방의 감정(감성)은 {0}%의 확률로 '{1}'입니다.".format(prob, emotion))

            if prob > 70:
                self.resultText.setStyleSheet("Color : blue")
                pass
            elif 50 <= prob <= 70 :
                self.resultText.setStyleSheet("Color : green")
                pass
            else:
                self.resultText.setStyleSheet("Color : red")
        except :
            pass
        finally:
            self.show()

