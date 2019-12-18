import sys
from PyQt5.QtWidgets import *
from initUi import Analyst

def main():
   import sys
   app = QApplication(sys.argv)
   chat = Analyst()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

