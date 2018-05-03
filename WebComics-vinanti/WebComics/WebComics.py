
"""
This file is part of WebComics.

WebComics is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

WebComics is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with WebComics.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import datetime
import time
import re
import sys
from functools import partial
from bs4 import BeautifulSoup
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from vinanti import Vinanti

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0"

class QtGuiQWidgetScroll(QtWidgets.QScrollArea):
    def __init__(self):
        super(QtGuiQWidgetScroll, self).__init__()
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            ui.previous()
            ui.zoom_image()
            ui.scrollArea.verticalScrollBar().setValue(0)
        elif event.key() == QtCore.Qt.Key_Right:
            ui.nxt()
            ui.zoom_image()
            ui.scrollArea.verticalScrollBar().setValue(0)
        elif event.key() == QtCore.Qt.Key_Space:
            self.hide()
            ui.tab.setFocus()
        else:
            super(QtGuiQWidgetScroll, self).keyPressEvent(event)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            ui.previous()
        elif event.key() == QtCore.Qt.Key_Right:
            ui.nxt()


class ExtendedQLabelEpn(QtWidgets.QLabel):

    def __init(self, parent):
        super(ExtendedQLabelEpn, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            ui.previous()
            ui.zoom_image()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global screen_height, screen_width
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 400))
        icon = QtGui.QIcon.fromTheme(_fromUtf8(""))
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = MyWidget(MainWindow)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(900, 290))
        self.label.setText(_fromUtf8(""))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(782, 60))
        self.frame.setMaximumSize(QtCore.QSize(782, 16777215))
        self.frame.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.prev = QtWidgets.QPushButton(self.frame)
        self.prev.setGeometry(QtCore.QRect(340, 20, 41, 21))
        self.prev.setObjectName(_fromUtf8("prev"))
        self.next = QtWidgets.QPushButton(self.frame)
        self.next.setGeometry(QtCore.QRect(410, 20, 41, 20))
        self.next.setObjectName(_fromUtf8("next"))
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setGeometry(QtCore.QRect(620, 20, 110, 26))
        self.date.setCalendarPopup(True)
        self.date.setObjectName(_fromUtf8("date"))
        self.go = QtWidgets.QPushButton(self.frame)
        self.go.setGeometry(QtCore.QRect(740, 20, 20, 20))
        self.go.setObjectName(_fromUtf8("go"))
        self.btn1 = QtWidgets.QComboBox(self.frame)
        self.btn1.setGeometry(QtCore.QRect(30, 15, 110, 31))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        
        self.btn1.addItem(_fromUtf8(""))
        self.btn1.addItem(_fromUtf8(""))
        self.btn1.addItem(_fromUtf8(""))
        self.btn1.addItem(_fromUtf8(""))
        self.btn2 = QtWidgets.QPushButton(self.frame)
        self.btn2.setGeometry(QtCore.QRect(160, 20, 61, 21))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btnM = QtWidgets.QPushButton(self.frame)
        self.btnM.setGeometry(QtCore.QRect(240, 20, 51, 21))
        self.btnM.setObjectName(_fromUtf8("btnM"))
        
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.scrollArea = QtGuiQWidgetScroll()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMaximumSize(screen_width, screen_height-60)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.vBox = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labelExp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelExp.setObjectName(_fromUtf8("labelExp"))
        self.labelExp.setScaledContents(True)
        self.vBox.addWidget(self.labelExp)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listComics = QtWidgets.QListWidget(self.tab_2)
        self.listComics.setObjectName(_fromUtf8("listComics"))
        self.horizontalLayout_2.addWidget(self.listComics)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btn1.currentIndexChanged['QString'].connect(self.comics)
        self.listComics.itemDoubleClicked['QListWidgetItem*'].connect(self.addComics)
        self.prev.clicked.connect(self.previous)
        self.next.clicked.connect(self.nxt)
        self.go.clicked.connect(self.goto_direct)
        self.btn2.clicked.connect(self.zoom_image)
        self.btnM.clicked.connect(self.loadMoreComics)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.vnt = Vinanti(block=False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Read Comics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.btn1.setItemText(0, _translate("MainWindow", "Select", None))
        self.btn1.setItemText(1, _translate("MainWindow", "Calvin", None))
        self.btn1.setItemText(2, _translate("MainWindow", "Garfield", None))
        self.btn1.setItemText(3, _translate("MainWindow", "OneBigHappy", None))
        self.date.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd", None))
        self.next.setText(_translate("MainWindow", "N", None))
        self.prev.setText(_translate("MainWindow", "P", None))
        self.go.setText(_translate("MainWindow", "Go", None))
        self.btn2.setText(_translate("MainWindow", "Original", None))
        self.btnM.setText(_translate("MainWindow", "More", None))
        self.btn2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Show Original Image Size</p></body></html>", None))
        
    def loadMoreComics(self):
        global homeComics
        self.tabWidget.setCurrentIndex(1)
        comics_list = os.path.join(homeComics, 'config.txt')
        f = open(comics_list, 'r')
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
        if self.listComics.count() == 0:
            MainWindow.setWindowTitle('Wait..')
            url = "http://www.gocomics.com/comics/a-to-z"
            self.vnt.get(url, onfinished=partial(self.more_comics, lines), hdrs={"User-Agent":USER_AGENT})
            self.vnt.start()
                            
    def more_comics(self, lines, *args):
        MainWindow.setWindowTitle('Select Comics')
        content = args[-1].result().html
        soup = BeautifulSoup(content, 'lxml')
        links = soup.findAll('a')
        for i in links:
            j = i.get('href')
            if j:
                last = j.rsplit('/')[-1]
                if last.isnumeric():
                    karr = j.split('/')
                    print(karr)
                    if len(karr) > 1:
                        k = karr[1]
                    else:
                        k = None
                    if k in lines:
                        self.listComics.addItem('#'+k)
                    elif k:
                        self.listComics.addItem(k)
    
    def fetch_comics(self, base_url, dt):
        global picn, name, homeComics, home1, prev_date, cur_date, MainWindow
        t = re.sub('/', '-', dt)
        picn = os.path.join(home1, '{}-{}.jpg'.format(name, t))
        print(picn)
        if not os.path.isfile(picn):
            MainWindow.setWindowTitle('Wait..')
            url = base_url + dt
            self.vnt.get(url, onfinished=partial(self.process_page, dt), hdrs={"User-Agent":USER_AGENT})
            self.vnt.start()
            print(url)
        else:
            img = QtGui.QPixmap(picn, "1")
            self.label.setPixmap(img)
            title = '{} {}'.format(name, dt)
            MainWindow.setWindowTitle(title)
            self.scrollArea.setWindowTitle(title)
        
    def process_page(self, *args):
        content = args[-1].result().html
        m = re.findall('data-image="http[^"]*', content)
        print(m)
        dt = args[0]
        for j, i in enumerate(m):
            m[j] = re.sub('data-image="', "", i)
        print(m)
        if len(m) > 0:
            try:
                url = m[1]
            except:
                url = m[0]
            self.vnt.get(url, onfinished=partial(self.set_picture, picn, dt), hdrs={"User-Agent":USER_AGENT}, out=picn)
            self.vnt.start()
            print('processing page')
        else:
            MainWindow.setWindowTitle('Comic strip not available for this date')

    def set_picture(self, *args):
        global name
        picn = args[0]
        dt = args[1]
        if os.path.isfile(picn):
            title = '{} {}'.format(name, dt)
            self.scrollArea.setWindowTitle(title)
            MainWindow.setWindowTitle(title)
            img = QtGui.QPixmap(picn, "1")
            self.label.setPixmap(img)
        else:
            MainWindow.setWindowTitle('Comic strip not available for this date')
        print('setting-picture')
    
    def addComics(self):
        global homeComics
        comics_list = os.path.join(homeComics, 'config.txt')
        r = self.listComics.currentRow()
        item = self.listComics.item(r)
        if item:
            txt = item.text()
            if not txt.startswith('#'):
                if os.stat(comics_list).st_size == 0:
                    f = open(comics_list, 'w')
                    f.write(txt)
                    f.close()
                    self.btn1.addItem(txt)
                    self.listComics.takeItem(r)
                    del item
                    self.listComics.insertItem(r, '#'+txt)
                    self.listComics.setCurrentRow(r)
                else:
                    f = open(comics_list, 'r')
                    lines = f.readlines()
                    f.close()
                    for i in range(len(lines)):
                        lines[i] = lines[i].replace('\n', '')
                    if txt not in lines:
                        f = open(comics_list, 'a')
                        f.write('\n'+txt)
                        f.close()
                        self.btn1.addItem(txt)
                    
                    self.listComics.takeItem(r)
                    del item
                    self.listComics.insertItem(r, '#'+txt)
                    self.listComics.setCurrentRow(r)
            else:
                txt = txt.replace('#', '')
                f = open(comics_list, 'r')
                lines = f.readlines()
                f.close()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace('\n', '')
                for i in range(len(lines)):
                    if txt == lines[i]:
                        del lines[i]
                        break
                f = open(comics_list, 'w')
                for i in range(len(lines)):
                    if i == 0:
                        f.write(lines[i])
                    else:
                        f.write('\n'+lines[i])
                f.close()
                self.listComics.takeItem(r)
                del item
                self.listComics.insertItem(r, txt)
                self.listComics.setCurrentRow(r)
                self.btn1.clear()
                self.btn1.addItem('Select')
                self.btn1.addItem('Calvin')
                self.btn1.addItem('Garfield')
                self.btn1.addItem('OneBigHappy')
                for i in range(len(lines)):
                    self.btn1.addItem(lines[i])
                    
    def comics(self):
        global name, base_url, homeComics, home1
        name = str(self.btn1.currentText())
        if name != "Select" and name:
            self.tabWidget.setCurrentIndex(0)
            home1 = os.path.join(homeComics, name)
            if not os.path.exists(home1):
                os.makedirs(home1)
            if name == "Calvin":
                base_url = "http://www.gocomics.com/calvinandhobbes/"
            elif name == "Garfield":
                base_url = "http://www.gocomics.com/garfield/"
            elif name == "OneBigHappy":
                base_url = "http://www.gocomics.com/onebighappy/"
            else:
                base_url = "http://www.gocomics.com/"+name+'/'
            self.goto_page()
        
    def zoom_image(self):
        global picn, screen_width, screen_height
        try:
            im = Image.open(picn)
            w, h = im.size
            img = QtGui.QPixmap(picn, "1")
            self.labelExp.setPixmap(img)
            QtWidgets.QApplication.processEvents()
            print (w, screen_width, h, screen_height)
            if w < screen_width:
                wd = w+20
            else:
                wd = screen_width
            if h < screen_height:
                ht = h + 20
            else:
                ht = screen_height - 60
            self.scrollArea.resize(wd, ht)
            self.scrollArea.show()
        except Exception as err:
            print(err)
        
    def goto_direct(self):
        global td, base_url, picn, cur_date, prev_date
        today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
        td = re.sub('-', '/', str(today))
        print (td)
        self.fetch_comics(base_url, td)  
        
    def goto_page(self):
        global td, base_url, picn, cur_date, prev_date
        self.vnt.get(base_url, onfinished=self.process_go_page, hdrs={"User-Agent":USER_AGENT})
        self.vnt.start()
          
    def process_go_page(self, *args):
        content = args[-1].result().html
        base_url = args[-2]
        print(args[-2], args[-3])
        try:
            soup = BeautifulSoup(content, 'lxml')
            link = soup.find('div', {'class':'feature'})
            link1 = link.find('h1')
            link2 = link1.find('a')['href']
            l = link2.split('/')
            td = l[-3]+'/'+l[-2]+'/'+l[-1] 
            print(td)
            cur_date = datetime.date(int(l[-3]), int(l[-2]), int(l[-1]))
        except Exception as err:
            today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
            td = re.sub('-', '/', str(today))
            print(td)
        self.fetch_comics(base_url, td)
        self.tab.setFocus() 
        print('process_go_page')
    
    def previous(self):
        global td, base_url, picn, prev_date
        today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
        day = datetime.timedelta(days=1)
        yday = today - day
        self.date.setDate(yday)
        td = re.sub('-', '/', str(yday))
        print(td)
        self.fetch_comics(base_url, td)
    
    def nxt(self):
        global td, base_url, picn, cur_date, next_date
        today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
        day = datetime.timedelta(days=1)
        tm = today + day
        if tm <= cur_date:
            self.date.setDate(tm)
            td = re.sub('-', '/', str(tm))
            print (td)
            self.fetch_comics(base_url, td)
    

def main():
    global ui, MainWindow, td, base_url, picn, home, cur_date
    global homeComics, screen_width, screen_height
    home = os.path.expanduser("~")
    homeComics = os.path.join(home, ".config", "Webcomics")
    comics_list = os.path.join(homeComics, "config.txt")
    if not os.path.exists(homeComics):
        os.makedirs(homeComics)
    comics_src = os.path.join(homeComics, 'src')
    if not os.path.exists(comics_src):
        os.makedirs(comics_src)
        os.chdir(comics_src)
    if not os.path.exists(comics_list):
        f = open(comics_list, 'w')
        f.close()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    screen_resolution = app.desktop().screenGeometry()
    screen_width = screen_resolution.width()
    screen_height = screen_resolution.height()
    print(screen_height, screen_width)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.date.setDate(QtCore.QDate.currentDate())
    cur_date = datetime.date(ui.date.date().year(), ui.date.date().month(), ui.date.date().day())
    MainWindow.show()
    if os.path.exists(comics_list):
        f = open(comics_list, 'r')
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            if not lines[i].startswith('#'):
                j = re.sub('#|\n', '', lines[i])
                if j:
                    ui.btn1.addItem(j)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

