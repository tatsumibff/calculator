#ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QPlainTextEdit) # type: ignore
from PyQt5.QtGui import QIcon

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1 = QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭 시 핸들러 함수 연결
        self.btn2 = QPushButton('Clear', self) #버튼 2 추가
        self.btn2.clicked.connect(self.clearMessage) #버튼 2 핸들러 함수 연결

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget (self.btn1) #버튼 1 배치
        hbox.addWidget(self.btn2) #버튼 2 배치
    

        vbox=QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        #vbox.addStretch(1) #빈 공간
        #vbox.addWidget(self.btn1) #버튼 위치
        vbox.addLayout(hbox) #btn1 위치에 hbox를 배치
        vbox.addStretch(1) #빈 공간

        self.setLayout(vbox) #빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정 

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) #윈도 아이콘 추가 
        self.resize(256,256)
        self.show()

    def clearMessage(self): #버튼 2 핸들러 함수 정의
        self.te1.clear()
    
    def activateMessage(self): #버튼을 클릭할 떄 동작하는 함수 : 메시지 박스 출력
        # QMessageBox.information(self,"information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
