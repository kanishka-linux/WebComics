# WebComics :  A Desktop client for accessing online comic strips.

Note : This appliation fetches comic strips from 'gocomics.com'

# Screenshot
![ReadManga](/Images/sample.png)

# Dependencies and Installation:

python3

python-pyqt5

python-pillow

python-beautifulsoup4

python-lxml


## Installation (Common for all platforms)

		$ git clone https://github.com/kanishka-linux/WebComics
		$ cd Webcomics
		$ python3 setup.py sdist (or python setup.py sdist)
		$ cd dist
		$ sudo pip3 install pkg_available_in_directory (or pip install pkg_available_in_directory) 
        {where 'pkg_available_in_directory' is the exact name of the package created in the 'dist' folder}
			
# Uninstall 
		
		uninstalling WebComics
		
		$ sudo pip3 uninstall webcomics
		
		for uninstalling dependencies
		
		$ sudo pip3 uninstall PyQt5 sip Pillow bs4 lxml

Once installed, open application using command **webcomics**

# Dependencies installation in arch.

sudo pacman -S python python-pyqt5 python-pillow python-beautifulsoup4 python-lxml

# In ubuntu 16.04+

sudo apt-get install python3 python3-pyqt5 python3-pil python3-bs4 python3-lxml


# Brief Documentation
Initially only three comics are provided in the list by default. You can add more, by clicking on 'More'. Once you click on 'More', wait for few seconds. A list of comics will be loaded in 'Tab 2'. Double click on any entry. If '#' is appended to the entry, then it means the comics has been added in the 'Select' combo-box, which then you have to select manually. You can double click on the '#' appended entry in the 'Tab 2' to de-hash and remove from the list of selected comics. 

Once a particular comics entry is selected, then it's latest strip is shown in the viewer.

If you click on the button 'original', then original image size will be shown as a pop-up window. You can navigate from this pop-up window itself between previous and next strip of the comics by using Right and Left key.

You can't change the size of original viewer. If you want to resize image then you can do it within pop-up window which will appear by clicking 'original' button.

Problem: Some comic strips are published weekly or monthly or without any fixed interval. In such cases, the application will only fetch latest comics strip. Previous or Next buttons won't work in this case. User can try various 'Dates' from the Calender Menu, to go to different strips of the comic directly, if previous or next buttons are not giving proper results.

# KeyBoard Shortcuts for pop-up window:

Right : Go to Next day strip of the comic.

Left  : Go to previous day strip of the comic.

Spacebar : Close pop-up window
