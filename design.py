import os
import sys

from plyer import notification
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5 import QtGui

import generator
from PyQt5.QtCore import QUrl, QThreadPool

root = os.path.dirname(sys.argv[0])


class Ui_MainWindow(object):
    def __init__(self):
        self.outfile = ''
        self.preview_opened = False
        self.poster_path = ('', '')
        self.threadpool = QThreadPool()
        self._translate = QtCore.QCoreApplication.translate

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet("* {\n"
                                 "    font: 12pt \"Arial\";\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar {\n"
                                 "    width:  10px;\n"
                                 "    background : #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical {\n"
                                 "    margin-left: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle {\n"
                                 "    border-radius: 5px;\n"
                                 "    background : #2B2B2B;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line {\n"
                                 "height: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line {\n"
                                 "background: none;\n"
                                 "height: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page, QScrollBar::sub-page {\n"
                                 "height: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget {\n"
                                 "    background: #000000;\n"
                                 "}\n"
                                 "#scrollArea, #scrollAreaWidgetContents_3 {\n"
                                 "    border: none;\n"
                                 "    background-color: #000;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    border-radius: 10px;\n"
                                 "    background: #262626;\n"
                                 "    color: #EBEBEB;\n"
                                 "    padding: 15px 8px;\n"
                                 "}\n"
                                 "QPushButton:disabled {\n"
                                 "    background-color:#373737;\n"
                                 "    color:#6F6F6F;\n"
                                 "}\n"
                                 "QLineEdit {\n"
                                 "    border: 1px solid rgba(255, 255, 255, 0.3);\n"
                                 "    border-radius: 10px;\n"
                                 "    background: #262626;\n"
                                 "    color: #FFFFFF;\n"
                                 "    padding: 15px 16px;\n"
                                 "}\n"
                                 "#textEdit {\n"
                                 "    border: 1px solid rgba(255, 255, 255, 0.3);\n"
                                 "    border-radius: 10px;\n"
                                 "    background: #262626;\n"
                                 "    color: #FFFFFF;\n"
                                 "    padding: 15px 16px;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 377, 374))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_3.pressed.connect(self.selectFile)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(self.sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.pressed.connect(self.generate_description)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.pushButton2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.pressed.connect(self.generate)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectFile(self):
        self.poster_path = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.jpeg)")
        if self.poster_path != ('', ''):
            self.pushButton_3.setText(self.poster_path[0].split('/')[-1])
        else:
            self.pushButton_3.setText(self._translate("MainWindow", "Выбрать постер"))

    def webLoad(self):
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.webView.setSizePolicy(self.sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(410, 0))
        self.webView.setObjectName("webView")
        self.webView.setUrl(QUrl.fromLocalFile(self.outfile))
        self.horizontalLayout.addWidget(self.webView)
        self.sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.preview_opened = True

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('assets/icon.png'))
        MainWindow.setWindowTitle(
            self._translate("MainWindow", "Генератор постеров (Developed & Designed by Gleb Kiva ミ๏ｖ๏彡)"))
        self.pushButton_3.setText(self._translate("MainWindow", "Выбрать постер"))
        self.pushButton2.setText(self._translate("MainWindow", "Сгенерировать описание"))
        self.lineEdit_3.setPlaceholderText(self._translate("MainWindow", "Сезон"))
        self.lineEdit_2.setPlaceholderText(self._translate("MainWindow", "Эпизод"))
        self.lineEdit.setPlaceholderText(self._translate("MainWindow", "Название фильма"))
        self.textEdit.setPlaceholderText(self._translate("MainWindow", "Описание"))
        self.pushButton.setText(self._translate("MainWindow", "Сохранить"))

    def generate_description(self):
        if len(self.lineEdit.text()) > 5:
            self.pushButton.setDisabled(True)
            self.pushButton2.setDisabled(True)
            g = generator.DescriptionGenerator(self.lineEdit.text())
            g.signals.description_generated.connect(self.generated_description)
            g.signals.error.connect(self.error)
            self.threadpool.start(g)

    def generated_description(self, text):
        self.pushButton.setDisabled(False)
        self.pushButton2.setDisabled(False)
        self.textEdit.setText(text.replace("\n", ""))

    def generate(self):
        if self.poster_path != ('', '') and len(self.lineEdit.text().replace(' ', '')) > 5:
            self.pushButton.setDisabled(True)
            self.pushButton2.setDisabled(True)
            data = {
                'season': self.lineEdit_3.text(),
                'episode': self.lineEdit_2.text(),
                'name': self.lineEdit.text(),
                'description': self.textEdit.toPlainText(),
                'poster_path': self.poster_path,
            }
            g = generator.Generator(data)
            g.signals.file_saved_as.connect(self.generated)
            g.signals.error.connect(self.error)
            self.threadpool.start(g)

    def generated(self, outfile):
        self.pushButton.setDisabled(False)
        self.pushButton2.setDisabled(False)
        try:
            notification.notify(title="Постер сохранён!",
                                message=outfile,
                                app_icon=None,
                                timeout=10,
                                toast=False)
            self.outfile = outfile
            if self.preview_opened:
                self.horizontalLayout.removeWidget(self.webView)
            self.webLoad()
        except:
            print("error")

    def error(self, text):
        print("important error: ", text)
        self.pushButton.setDisabled(False)
        self.pushButton2.setDisabled(False)
