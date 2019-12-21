# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from analyst import Analyst

def main():
   app = QApplication(sys.argv)
   chat = Analyst()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

