#ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit) # type: ignore
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

        vbox=QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        #vbox.addStretch(1) #빈 공간
        vbox.addWidget(self.btn1) #버튼 위치
        vbox.addStretch(1) #빈 공간

        self.setLayout(vbox) #빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정 

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) #윈도 아이콘 추가 
        self.resize(256,256)
        self.show()
    
    def activateMessage(self): #버튼을 클릭할 떄 동작하는 함수 : 메시지 박스 출력
        # QMessageBox.information(self,"information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
