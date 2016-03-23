#WebComics :  A GNU/Linux Desktop Application for accessing Web-Comics over the internet.

Note : This appliation fetches comic strips from 'gocomics.com'

#Screenshot
![ReadManga](/Images/sample.png)

#Dependencies and Installation:
(This Application is mainly written in pyqt4 and python3)

Note: If you've successfully installed AnimeWatch Player before, then you don't have to install any dependencies at all and can directly go to main installation process, which is same as that of 'AnimeWatch'.

python3

python-pyqt4

python-requests

python-urllib3

python-pillow

python-beautifulsoup4

python-lxml

python-pip

python-pycurl

python-psutil

curl

wget


#Dependencies installation in arch.

sudo pacman -S python python-pyqt4 python-pycurl python-requests python-urllib3 python-pillow python-beautifulsoup4 python-lxml python-psutil python-pip curl wget



#In ubuntu 14.04, default python points to python 2.7, hence for installing dependencies use following command

sudo apt-get install python3 python3-pyqt4 python3-pycurl python3-requests python3-urllib3 python3-pil python3-bs4 python3-lxml python3-psutil python3-pip curl wget



#Once Dependencies are installed Download the folder. Goto WebComics Directory containing 'install.py' file. Open Terminal in the directory and use following command:

#In Arch:

python install.py

#In Ubuntu 14.04:

python3 install.py

Application Launcher will be created as "~/.local/share/applications/WebComics.desktop"

All other configuration files will be created in "~/.config/Webcomics/" and all the comics strips that you have visited will be locally stored in this folder for later viewing.



#Uninstall

Simply remove the application launcher '~/.local/share/applications/WebComics.desktop' and clear the directory '~/.config/Webcomics/src/'. If you want to remove all configuration files also, then simply delete directory '~/.config/Webcomics/'. Once you delete the configuration directory, all the settings will be lost.

#Troubleshooting

If Application Launcher in the menu is not working or programme is crashing then directly go to "~/.config/Webcomics/src/", open terminal there and run "python3 WebComics.py" or "python WebComics.py" as per your default python setup. If there is some problem in installation, then you will get idea about it, whether it is missing dependency or something else, or you can report the error as per the message in terminal.

If you do not find application launcher in the menu then try copying manually "~/.config/ReadMangaKA/WebComics.desktop" to either "~/.local/share/applications/" or "/usr/share/applications/"

In LXDE, XFCE or Cinnamon ,any new entry of launcher in '~/.local/share/applications/' is instantly shown in Start Menu (In this case, entry will be shown either in Multimedia or Sound & Video). In Ubuntu Unity you will have to either logout and login again or reboot to see the entry in Unity dash Menu.





#Brief Documentation
Initially only three comics are provided in the list by default. You can add more, by clicking on 'More'. Once you click on 'More', wait for few seconds. A list of comics will be loaded in 'Tab 2'. Double click on any entry. If '#' is appended to the entry, then it means the comics has been added in the 'Select' combo-box, which then you have to select manually. You can double click on the '#' appended entry in the 'Tab 2' to de-hash and remove from the list of selected comics. 

Once a particular comics entry is selected, then it's latest strip is shown in the viewer.

If you click on the button 'original', then original image size will be shown as a pop-up window. You can navigate from this pop-up window itself between previous and next strip of the comics by using Right and Left key.

You can't change the size of original viewer. If you want to resize image then you can do it within pop-up window which will appear by clicking 'original' button.

Problem: Some comic strips are published weekly or monthly or without any fixed interval. In such cases, the application will only fetch latest comics strip. Previous or Next buttons won't work in this case. User can try various 'Dates' from the Calender Menu, to go to different strips of the comic directly, if previous or next buttons are not giving proper results.

#KeyBoard Shortcuts:

Right : Go to Next day strip of the comic.

Left  : Go to previous day strip of the comic.

