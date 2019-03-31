import sys
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QAction,QFileDialog,QLineEdit,QInputDialog
from PyQt5.QtWidgets import QMessageBox,QCheckBox,QProgressBar,QComboBox,QLabel,QStyleFactory,QFontDialog,QCalendarWidget,QColorDialog,QTextEdit
from PyQt5.uic.properties import QtGui

class window(QMainWindow):

    def __init__(self):
        super(window , self).__init__()  # interitance the QMainWindow method
        self.setGeometry(50, 50 ,500 , 300)  # set the deometry of our Gui
        self.setWindowTitle("my first GUI Application") # method used to set the title on Window
        extractAction = QAction("&Get to the IDle Window", self)  # defined to take Action on menu bar
        extractAction.setShortcut("Ctrl+Q") # provide short cut key for action 
        extractAction.setStatusTip('leave the App')
        extractAction.triggered.connect(self.close_application)  # use to clicked the filemenu bar

        openEditor = QAction('Editor',self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QAction('&open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QAction('&Save',self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('save File')
        saveFile.triggered.connect(self.file_save)


        self.statusBar()  #calling the method for taking action
        
        mainMenu = self.menuBar()   #methon to create menu bar on Window
        fileMenu = mainMenu.addMenu('&File')   #Adding file on the top of the Window
        EditMenu = mainMenu.addMenu('&Edit')
        editorMenu = mainMenu.addMenu('Editor')
        editorMenu.addAction(openEditor)
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        extractAction = QAction(QIcon("Tool_bar_icon.png"),'flee the scene' , self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)
        
        fontchoice = QAction('Fonts',self)
        fontchoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontchoice)

        cal = QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200 , 200)
        self.home()

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self,'Save File', options=QFileDialog.DontUseNativeDialog)
        file = open(name , 'w')
        text = self.textedit.toPlainText()
        file.write(text)
        file.close()

    def file_open(self):
        name,_ = QFileDialog.getOpenFileName(self,'open File', options=QFileDialog.DontUseNativeDialog)
        file = open(name , 'r')
        self.editor()

        with file:
            text = file.read()
            self.textedit.setText(text)

    def editor(self):
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.stylechoice.setStyleSheet('QWidget{color: %s}' % color.name())

    def font_choice(self):
        font , valid = QFontDialog.getFont()
        if valid:
            self.stylechoice.setFont(font)

    def home(self):      #method to defined to have button on home screen
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(200 ,200)
        checkBox = QCheckBox('Enlarge window' , self)
        checkBox.move(0, 50)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80 , 250 ,20)
        self.btn = QPushButton("Download", self)
        self.btn.move(200 ,120)
        self.btn.clicked.connect(self.download)
        
        self.stylechoice = QLabel('CleanLooks',self)
        comboBox = QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('Windowvista')
        comboBox.move(25,250)
        self.stylechoice.move(25,150)
        comboBox.activated[str].connect(self.style_choice)

        color = QColor(0,0,0)
        fontcolor = QAction('&Font_color',self)
        fontcolor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontcolor)
        self.show()

    def style_choice(self,text):
        self.stylechoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
        

    def download(self):
        self.comp = 0
        while self.comp<100:
            self.comp += 0.0001
            self.progress.setValue(self.comp)

    def enlarge_window(self,state):
        if state == Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def close_application(self):
        choice = QMessageBox.question(self, "Extrat",
                                      "Are you sure to Quit the Window?", QMessageBox.Yes |
                                      QMessageBox.No,QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("hello")
            sys.exit()
        else:
            pass
        #sys.exit()

if __name__ == "__main__":

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
        
        
