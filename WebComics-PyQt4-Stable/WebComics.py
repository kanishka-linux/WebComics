
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

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDateTime
import datetime
import time
import re
import sys
import urllib
import urllib3
import pycurl
from io import StringIO,BytesIO    
import subprocess
import os.path
from subprocess import check_output
from bs4 import BeautifulSoup
from PIL import Image
from os.path import expanduser

class QtGuiQWidgetScroll(QtGui.QScrollArea):
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
		super(QtGuiQWidgetScroll, self).keyPressEvent(event)

class MyWidget(QtGui.QWidget):
	def __init__(self,parent):
		super(QtGui.QWidget, self).__init__(parent)
		
	def keyPressEvent(self, event):
		
		
		if event.key() == QtCore.Qt.Key_Left:
			ui.previous()
			#ui.zoom_image()
			#ui.scrollArea.verticalScrollBar().setValue(0)
		elif event.key() == QtCore.Qt.Key_Right:
			ui.nxt()
			#ui.zoom_image()
			#ui.scrollArea.verticalScrollBar().setValue(0)
		#super(QtGui.QWidget, self).keyPressEvent(event)

class ExtendedQLabelEpn(QtGui.QLabel):

	def __init(self, parent):
		#QLabel.__init__(self, parent)
		super(ExtendedQLabelEpn, self).__init__(parent)

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Backspace:
			ui.previous()
			ui.zoom_image()
def getContentUnicode(content):
	if isinstance(content,bytes):
		print("I'm byte")
		try:
			content = str((content).decode('utf-8'))
		except:
			content = str(content)
	else:
		print(type(content))
		content = str(content)
		print("I'm unicode")
	return content

def ccurl(url):
	hdr = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0"
	c = pycurl.Curl()
	c.setopt(c.FOLLOWLOCATION, True)
	c.setopt(c.USERAGENT, hdr)
	
	url = str(url)
	c.setopt(c.URL, url)
	
	storage = BytesIO()
	c.setopt(c.WRITEFUNCTION, storage.write)
	c.perform()
	c.close()
	content = storage.getvalue()
	content = getContentUnicode(content)
	return content
      
def findimg(url):
	global name,homeComics,td,home1
	if url:
	
		t = re.sub('/','-',td)
		picn = home1+'/'+name + "-"+t+'.jpg'
		if not os.path.isfile(picn):
			subprocess.Popen(["wget",url,"-O",picn])
	return picn
def getPrevNext(content):
	global prev_date,next_date
	
	soup = BeautifulSoup(content,'lxml')
	link = soup.find('div',{'class':'feature'})
	
	linkP = link.find('ul',{'class':'feature-nav'})
	linkP1 = linkP.find('a',{'class':'prev'})
	linkP2 = linkP1['href']
	print (linkP2)
	l = linkP2.split('/')
	prev_date = datetime.date(int(l[-3]), int(l[-2]), int(l[-1]))
	print(prev_date)
	
	linkP = link.find('ul',{'class':'feature-nav'})
	linkP1 = linkP.find('a',{'class':'next'})
	linkP2 = linkP1['href']
	print (linkP2)
	l = linkP2.split('/')
	next_date = datetime.date(int(l[-3]), int(l[-2]), int(l[-1]))
	print(next_date)
	
def fetch_comics(base_url,dt):
	global picn,name,homeComics,home1,prev_date,cur_date
	t = re.sub('/','-',dt)
	picn = home1+'/'+name + "-"+t+'.jpg'
	print (picn)
	if not os.path.isfile(picn):
		url = base_url + dt
		content = ccurl(url)
		#getPrevNext(content)
		#m = re.findall('http://assets.amuniversal.com/[^]*',content)
		m = re.findall('class="strip" src="http[^"]*',content)
		print (m)
		j = 0
		for i in m:
			m[j] = re.sub('class="strip" src="',"",i)
			j = j+1
		print (m)
		try:
			url = m[1]
		except:
			url = m[0]
		
		subprocess.call(["wget",url,"-O",picn])
	#else:
		
	img = QtGui.QPixmap(picn,"1")
	ui.label.setPixmap(img)




try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		global screen_height,screen_width
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.setEnabled(True)
		MainWindow.resize(800, 400)
		MainWindow.setMinimumSize(QtCore.QSize(0, 0))
		MainWindow.setMaximumSize(QtCore.QSize(900, 400))
		icon = QtGui.QIcon.fromTheme(_fromUtf8(""))
		MainWindow.setWindowIcon(icon)
		MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		#self.tab = QtGui.QWidget()
		self.tab = MyWidget(MainWindow)
		self.tab.setObjectName(_fromUtf8("tab"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label = QtGui.QLabel(self.tab)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
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
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.verticalLayout.addWidget(self.tabWidget)
		self.frame = QtGui.QFrame(self.centralwidget)
		self.frame.setMinimumSize(QtCore.QSize(782, 60))
		self.frame.setMaximumSize(QtCore.QSize(782, 16777215))
		self.frame.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
		self.frame.setFrameShape(QtGui.QFrame.NoFrame)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setLineWidth(0)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.prev = QtGui.QPushButton(self.frame)
		self.prev.setGeometry(QtCore.QRect(340, 20, 41, 21))
		self.prev.setObjectName(_fromUtf8("prev"))
		self.next = QtGui.QPushButton(self.frame)
		self.next.setGeometry(QtCore.QRect(410, 20, 41, 20))
		self.next.setObjectName(_fromUtf8("next"))
		self.date = QtGui.QDateEdit(self.frame)
		self.date.setGeometry(QtCore.QRect(620, 20, 110, 26))
		self.date.setCalendarPopup(True)
		self.date.setObjectName(_fromUtf8("date"))
		self.go = QtGui.QPushButton(self.frame)
		self.go.setGeometry(QtCore.QRect(740, 20, 20, 20))
		self.go.setObjectName(_fromUtf8("go"))
		self.btn1 = QtGui.QComboBox(self.frame)
		self.btn1.setGeometry(QtCore.QRect(30, 15, 110, 31))
		self.btn1.setObjectName(_fromUtf8("btn1"))
		
		
		
		self.btn1.addItem(_fromUtf8(""))
		self.btn1.addItem(_fromUtf8(""))
		self.btn1.addItem(_fromUtf8(""))
		self.btn1.addItem(_fromUtf8(""))
		self.btn2 = QtGui.QPushButton(self.frame)
		self.btn2.setGeometry(QtCore.QRect(160, 20, 61, 21))
		self.btn2.setObjectName(_fromUtf8("btn2"))
		self.btnM = QtGui.QPushButton(self.frame)
		self.btnM.setGeometry(QtCore.QRect(240, 20, 51, 21))
		self.btnM.setObjectName(_fromUtf8("btnM"))
		
		self.verticalLayout.addWidget(self.frame)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		
		#self.scrollArea = QtGui.QScrollArea()
		self.scrollArea = QtGuiQWidgetScroll()
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setMaximumSize(screen_width,screen_height-60)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.vBox = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.labelExp = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelExp.setObjectName(_fromUtf8("labelExp"))
		self.labelExp.setScaledContents(True)
		self.vBox.addWidget(self.labelExp)
		
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.listComics = QtGui.QListWidget(self.tab_2)
		self.listComics.setObjectName(_fromUtf8("listComics"))
		self.horizontalLayout_2.addWidget(self.listComics)
		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QObject.connect(self.btn1, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.comics)
		QtCore.QObject.connect(self.listComics, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.addComics)
		#QtCore.QObject.connect(self.date, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.label.clear)
		QtCore.QObject.connect(self.prev, QtCore.SIGNAL(_fromUtf8("clicked()")), self.previous)
		QtCore.QObject.connect(self.next, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nxt)
		QtCore.QObject.connect(self.go, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goto_direct)
		QtCore.QObject.connect(self.btn2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.zoom_image)
		QtCore.QObject.connect(self.btnM, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loadMoreComics)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
		#self.prev.setToolTip(_translate("MainWindow", "<html><head/><body><p>Go To Previous Page</p></body></html>", None))
		#self.next.setToolTip(_translate("MainWindow", "<html><head/><body><p>Go To Next Page</p></body></html>", None))
		
	def loadMoreComics(self):
		self.tabWidget.setCurrentIndex(1)
		global homeComics
		comics_list = homeComics + '/config.txt'
		f = open(comics_list,'r')
		lines = f.readlines()
		f.close()
		for i in range(len(lines)):
			lines[i] = lines[i].replace('\n','')
		if self.listComics.count() == 0:
			url = "http://www.gocomics.com/features"
			content = ccurl(url)
			soup = BeautifulSoup(content,'lxml')
			link = soup.find('div',{'id':'content-full'})
			links = link.findAll('a')
			for i in links:
					j = i['href']
					if not j.startswith('#'):
						j = j.replace('/','')
						if j in lines:
							self.listComics.addItem('#'+j)
						else:
							self.listComics.addItem(j)
			
	def addComics(self):
		global homeComics
		comics_list = homeComics + '/config.txt'
		r = self.listComics.currentRow()
		item = self.listComics.item(r)
		if item:
			txt = item.text()
			
			if not txt.startswith('#'):
				
				if os.stat(comics_list).st_size == 0:
					f = open(comics_list,'w')
					f.write(txt)
					f.close()
					self.btn1.addItem(txt)
					self.listComics.takeItem(r)
					del item
					self.listComics.insertItem(r,'#'+txt)
					self.listComics.setCurrentRow(r)
				else:
					f = open(comics_list,'r')
					lines = f.readlines()
					f.close()
					for i in range(len(lines)):
						lines[i] = lines[i].replace('\n','')
					if txt not in lines:
						f = open(comics_list,'a')
						f.write('\n'+txt)
						f.close()
						self.btn1.addItem(txt)
					
					self.listComics.takeItem(r)
					del item
					self.listComics.insertItem(r,'#'+txt)
					self.listComics.setCurrentRow(r)
			else:
				txt = txt.replace('#','')
				f = open(comics_list,'r')
				lines = f.readlines()
				f.close()
				for i in range(len(lines)):
					lines[i] = lines[i].replace('\n','')
				for i in range(len(lines)):
					if txt == lines[i]:
						del lines[i]
						break
				f = open(comics_list,'w')
				for i in range(len(lines)):
					if i == 0:
						f.write(lines[i])
					else:
						f.write('\n'+lines[i])
				f.close()
				self.listComics.takeItem(r)
				del item
				self.listComics.insertItem(r,txt)
				self.listComics.setCurrentRow(r)
				self.btn1.clear()
				self.btn1.addItem('Select')
				self.btn1.addItem('Calvin')
				self.btn1.addItem('Garfield')
				self.btn1.addItem('OneBigHappy')
				for i in range(len(lines)):
					self.btn1.addItem(lines[i])
	def comics(self):
		global name,base_url,homeComics,home1
		name = str(self.btn1.currentText())
		if name != "Select" and name:
			self.tabWidget.setCurrentIndex(0)
			home1 = homeComics+'/'+name
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
		global picn,screen_width,screen_height
		#Image.open(picn).show()
		im = Image.open(picn)
		w, h = im.size
		
		img = QtGui.QPixmap(picn,"1")
		self.labelExp.setPixmap(img)
		QtGui.QApplication.processEvents()
		#self.labelExp.setMinimumHeight(screen_height-60)
		#self.labelExp.setMaximumHeight(10000000)
		#self.labelExp.setMinimumWidth(screen_width-100)
		#self.(screen_width-100)
		#w = self.labelExp.width()
		#h = self.labelExp.height()
		print (w,screen_width,h,screen_height)
		if w < screen_width:
			wd = w+20
		else:
			wd = screen_width
		if h < screen_height:
			ht = h + 20
		else:
			ht = screen_height - 60
		self.scrollArea.resize(wd,ht)
		self.scrollArea.show()
	def goto_direct(self):
		global td,base_url,picn,cur_date,prev_date
		
		print ("Hello")
		today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
		td = re.sub('-','/',str(today))
		print (td)
		
		fetch_comics(base_url,td)  
	def goto_page(self):
		global td,base_url,picn,cur_date,prev_date
		try:
			content = ccurl(base_url)
			soup = BeautifulSoup(content,'lxml')
			link = soup.find('div',{'class':'feature'})
			link1 = link.find('h1')
			link2 = link1.find('a')['href']
			l = link2.split('/')
			td = l[-3]+'/'+l[-2]+'/'+l[-1] 
			print(td)
			cur_date = datetime.date(int(l[-3]), int(l[-2]), int(l[-1]))
			
			
			
			#linkP = link.find('ul',{'class':'feature-nav'})
			#linkP1 = linkP.find('a',{'class':'prev'})
			#linkP2 = linkP1['href']
			#print (linkP2)
			#l = linkP2.split('/')
			#prev_date = datetime.date(int(l[-3]), int(l[-2]), int(l[-1]))
			#print(prev_date)
			
		except:
			print ("Hello")
			today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
			td = re.sub('-','/',str(today))
			print (td)
		
		fetch_comics(base_url,td)
		self.tab.setFocus()  
		#Image.open(url).show()
	
	
	
  
	def previous(self):
		global td,base_url,picn,prev_date
		today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
		day = datetime.timedelta(days=1)
		yday = today - day
		self.date.setDate(yday)
		td = re.sub('-','/',str(yday))
		print (td)
		fetch_comics(base_url,td)
	
	
	def nxt(self):
		global td,base_url,picn,cur_date,next_date
		print ("Hello")
		today = datetime.date(self.date.date().year(), self.date.date().month(), self.date.date().day())
		day = datetime.timedelta(days=1)
		tm = today + day
		
		if tm <= cur_date:
			self.date.setDate(tm)
			td = re.sub('-','/',str(tm))
			print (td)
			fetch_comics(base_url,td)
	
	
    

if __name__ == "__main__":
	import sys
	global td,base_url,picn,home,cur_date,screen_width,screen_height,homeComics
	home = expanduser("~")
	comics_list = home+"/.config/Webcomics/config.txt"
	homeComics = home+"/.config/Webcomics"
	
	if not os.path.exists(homeComics):
		os.makedirs(homeComics)
	if not os.path.exists(homeComics+'/src'):
		os.makedirs(homeComics+'/src')
		os.chdir(homeComics+'/src')
	if not os.path.exists(comics_list):
		f = open(comics_list,'w')
		f.close()
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	screen_resolution = app.desktop().screenGeometry()
	screen_width = screen_resolution.width()
	screen_height = screen_resolution.height()
	print (screen_height,screen_width)
	#MainWindow = QtGui.QWidget()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.date.setDate(QtCore.QDate.currentDate())
	cur_date = datetime.date(ui.date.date().year(), ui.date.date().month(), ui.date.date().day())
	MainWindow.show()
	if os.path.exists(comics_list):
		f = open(comics_list,'r')
		lines = f.readlines()
		f.close()
		for i in range(len(lines)):
			if not lines[i].startswith('#'):
				j = re.sub('#|\n','',lines[i])
				if j:
					ui.btn1.addItem(j)
	sys.exit(app.exec_())

