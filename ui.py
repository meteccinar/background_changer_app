import sys
import os
from PIL import Image as im
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu , QVBoxLayout ,QHBoxLayout , QAction , QFileDialog
from PyQt5.QtGui import QIcon, QPixmap , QPainter, QBrush, QPen
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer , Qt
class Main(QMainWindow):
    # Methods start
    flag1 = False
    flag2 = False
    path1 = ""
    path2 = ""
    def setBackground(self):

        import bg
        global path1
        global path2
        print("Image Path : ",path1)
        print("Background Path : ",path2)
        picture = bg.applyBackground(path1,path2)
        data = im.fromarray(picture)
        data.save('image.png')
        pixmap = QPixmap("image.png")
        self.placeHolder.setPixmap(pixmap)

    def exitButton(self):
        self.close()

    def openPhoto(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        photo, _ = QFileDialog.getOpenFileName(self,"Choose a photo", "","All Files (*);;Image Files (*.jpg)", options=options)
        if photo:
            pixmap = QPixmap(photo)
            yellow = QPixmap('ico/orange.png')
            self.placeHolder.setPixmap(pixmap)
            self.header.setPixmap(yellow)

            flag1 = True
            print(photo)
            global path1
            path1 = photo
            return photo

    def openBackground(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        bg, _ = QFileDialog.getOpenFileName(self,"Choose a photo", "","All Files (*);;Image Files (*.jpg)", options=options)
        if bg:
            pixmap = QPixmap(bg)
            green = QPixmap('ico/green.png')
            self.placeHolder.setPixmap(pixmap)
            self.header.setPixmap(green)

            flag2 = True
            print(bg)
            global path2
            path2 = bg
            return bg



    # Methods finish

    def __init__(self, parent=None):


        super(Main, self).__init__(parent)
        self.setWindowTitle("Background Changer")
        self.setGeometry(100, 100,700,600)

        #Menubar Start
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        config = QAction('Config (Developer Mode)', self)
        exit = QAction('Exit',self)
        save = QAction('Save',self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(config)
        fileMenu.addAction(save)
        fileMenu.addAction(exit)
        #Menubar Finish



        #Main Frame start
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet('* {background: white;}')
        self.vLayout = QVBoxLayout(self.centralWidget)
        #Main Frame finish

        #Mini start
        self.buttonsWidget2 = QWidget()
        self.buttonsWidgetLayout2 = QHBoxLayout(self.buttonsWidget2)
        button = QPushButton("Change Background")

        self.buttonsWidgetLayout2.addWidget(button)

        self.buttonsWidget2.setStyleSheet('* {background: #BFBEB0;}')
        self.buttonsWidget2.setMinimumWidth(25)
        self.buttonsWidget2.setMinimumHeight(50)
        #Mini finish

        #Buttons start
        self.buttonsWidget = QWidget()
        self.buttonsWidgetLayout = QHBoxLayout(self.buttonsWidget)
        button1 = QPushButton("Add your photo")
        button2 = QPushButton("Add any background")
        self.buttonsWidgetLayout.addWidget(button1)
        self.buttonsWidgetLayout.addWidget(button2)
        self.buttonsWidget.setStyleSheet('* {background: gray;}')
        #Buttons finish

        #PlaceHolder start
        self.placeHolder = QLabel()
        self.placeHolder.setMinimumWidth(700)
        self.placeHolder.setMinimumHeight(600)
        self.placeHolder.setStyleSheet('* {background: white; qproperty-alignment:AlignCenter;}')
        #PlaceHolder finish

        #Header start
        self.header = QLabel()
        self.headerWidgetLayout = QHBoxLayout(self.header)

        isOK = QPixmap('ico/red.png')
        smaller_OK = isOK.scaled(64, 64, Qt.KeepAspectRatio, Qt.FastTransformation)



        self.header.setPixmap(smaller_OK)


        self.show()


        self.header.setMinimumWidth(300)
        self.header.setMinimumHeight(100)
        self.header.setStyleSheet('* {background: gray; qproperty-alignment:AlignCenter;}')
        #Header finish

        #Button Events start
        exit.triggered.connect(self.exitButton)
        button1.clicked.connect(self.openPhoto)
        button2.clicked.connect(self.openBackground)
        button.clicked.connect(self.setBackground)
        #Button Events finish



        self.vLayout.addWidget(self.header)
        self.vLayout.addWidget(self.buttonsWidget2)

        self.vLayout.addWidget(self.placeHolder)
        self.vLayout.addWidget(self.buttonsWidget)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Main()
    mainWin.show()
    sys.exit(app.exec_())
