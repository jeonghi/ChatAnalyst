# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5 import QtGui, QtCore
from apiservice import ApiService

class Button(QToolButton):
    def __init__(self, text, callback, img):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Preferred)
        self.resize(206,121)
        self.setText(text)
        self.clicked.connect(callback)
        self.setIcon(QtGui.QIcon(img))
        self.setIconSize(QtCore.QSize(206, 121))

class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.setFont(font)

class Analyst(QWidget):

    def __init__(self):
        super().__init__()
        self.drawUi()
        self.show()

    def drawUi(self):
        self.setGeometry(300, 300, 500, 900)
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Preferred)

        self.setWindowTitle('Emotion Analyst')
        # 배경 노란색으로 칠하기
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("yellow")))
        self.setPalette(palette)
        # 레이아웃 구성하기
        self.title = QLabel()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.v = QVBoxLayout()
        self.v.setSizeConstraint(QLayout.SetFixedSize)
        # UI틀 구성
        self.v.addWidget(self.title)
        self.inputText = QTextEdit('최소 12자에서 최대 100까지만 입력해주세요')
        self.inputText.setMaximumHeight(200)
        self.v.addWidget(self.inputText)
        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.addLayout(self.h3)
        self.setLayout(self.v)

        # UI 꾸미기
        img1 = QPixmap()
        img1.load("title.png")
        self.title.setPixmap(img1)

        # 감정(감성)분석 버튼
        self.btn1 = Button('감정분석', self.buttonClicked, "btn1.png")
        self.btn2 = Button('감성분석', self.buttonClicked, "btn2.png")
        self.h1.addStretch(1)
        self.h1.addWidget(self.btn1)
        self.h1.addStretch(1)
        self.h1.addWidget(self.btn2)
        self.h1.addStretch(1)

        self.info = QLabel()
        img2 = QPixmap()
        img2.load("info.png")
        self.info.setPixmap(img2)
        self.h2.addWidget(self.info)
        self.h2.addStretch(1)

        #h3 구성
        self.resultText = Label('아직은 모르겠구나...')
        self.h3.addWidget(self.resultText)

    def buttonClicked(self):
        # 버튼 클릭시 callback
        sender = self.sender().text()
        query = self.inputText.toPlainText().strip()

        if not 12 <= len(query) <= 100 :
            self.resultText.setText("최소 12자 최대 100자를 입력하셔야합니다.")
            self.resultText.setStyleSheet("Color : red")
            return

        btn_type = {'감정분석': 0, '감성분석': 1}
        type = btn_type[sender] #btn_type = {'감정분석':0 , '감성분석':1}
        # json 응답
        try:
            response = ApiService().emotionAnalysis(type, query)
            if response['result'] == 'success':
                emotion = response['emotion']
                prob = response['prob']

                self.resultText.setText(" 상대방의 감정(감성)은 {0}%의 확률로 '{1}'이구나.".format(prob, emotion))
                if prob > 70:
                    self.resultText.setStyleSheet("Color : blue")
                    pass
                elif 50 <= prob <= 70 :
                    self.resultText.setStyleSheet("Color : green")
                    pass
                else:
                    self.resultText.setStyleSheet("Color : red")
            else:
                self.resultText.setText(response['result'])
                self.resultText.setStyleSheet("Color : red")
        except:
            pass
        finally:
            self.show()

if __name__ == "__main__":
    pass