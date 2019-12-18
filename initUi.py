# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5 import QtGui, QtCore
from ApiService import ApiService

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Preferred)
        self.setText(text)
        self.resize(206,121)
        self.clicked.connect(callback)

class Label(QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)

class Text(QTextEdit):

    def __init__(self, text):
        super().__init__()
        self.append(text)
        self.setMaximumHeight(200)

class Analyst(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 500, 900)
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Preferred)
        self.setWindowTitle('Emotion Analyst')
        self.drawUi()
        self.show()


    def drawUi(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("yellow")))
        self.setPalette(palette)

        self.title = QLabel()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.v = QVBoxLayout()
        self.v.setSizeConstraint(QLayout.SetFixedSize)

        self.v.addWidget(self.title)
        self.inputText = Text('누구인가? 누가 어려운 소리를 내었는가')
        self.v.addWidget(self.inputText)
        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.addLayout(self.h3)

        img1 = QPixmap()
        img1.load("title.png")
        self.title.setPixmap(img1)

        self.btn1 = Button('감정분석', self.buttonClicked)
        self.btn1.setIcon(QtGui.QIcon("btn1.png"))
        self.btn1.setIconSize(QtCore.QSize(206, 121))

        self.btn2 = Button('감성분석', self.buttonClicked)
        self.btn2.setIcon(QtGui.QIcon("btn2.png"))
        self.btn2.setIconSize(QtCore.QSize(206, 121))

        self.h1.addStretch(1)
        self.h1.addWidget(self.btn1)
        self.h1.addWidget(self.btn2)
        self.h1.addStretch(1)

        self.info = QLabel()
        img2 = QPixmap()
        img2.load("info.png")
        self.info.setPixmap(img2)
        self.h2.addWidget(self.info)
        self.h2.addStretch(1)
        self.resultText = Label('       아직은 모르겠구나...')
        #self.h3.addStretch(1)
        self.h3.addWidget(self.resultText)
        self.setLayout(self.v)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.resultText.setFont(font)

    def buttonClicked(self):
        sender = self.sender().text()
        query = self.inputText.toPlainText()
        btn_type = {'감정분석': 0, '감성분석': 1}
        type = btn_type[sender] #btn_type = {'감정분석':0 , '감성분석':1}
        # json 응답

        result = ApiService().emotionAnalysis(type, query)
        emotion = result['emotion']
        prob = result['prob']

        self.resultText.setText("       상대방의 감정(감성)은 {0}%의 확률로 '{1}'이구나.".format(prob, emotion))
        if prob > 70:
            self.resultText.setStyleSheet("Color : blue")
            pass
        elif 50 <= prob <= 70 :
            self.resultText.setStyleSheet("Color : green")
            pass
        else:
            self.resultText.setStyleSheet("Color : red")
        self.show()

