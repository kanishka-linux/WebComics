"""
Copyright (C) 2017 kanishka-linux kanishka.linux@gmail.com

This file is part of WebComics.

kawaii-player is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kawaii-player is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kawaii-player.  If not, see <http://www.gnu.org/licenses/>.
"""


import os
import shutil
import platform
from setuptools import setup


"""
 GNU/Linux users should install dependencies manually using their native
 package manager
"""
if platform.system().lower() == 'linux':
    install_dependencies = []
else:
    install_dependencies = ['PyQt5', 'bs4', 'Pillow', 'lxml']
setup(
    name='WebComics', 
    version='3.0.0', 
    license='GPLv3', 
    author='kanishka-linux', 
    author_email='kanishka.linux@gmail.com', 
    url='https://github.com/kanishka-linux/WebComics', 
    long_description="README.md",
    packages=['WebComics'], 
    entry_points={
        'gui_scripts':['webcomics = WebComics.WebComics:main'], 
        'console_scripts':['webcomics-console = WebComics.WebComics:main']
        }, 
    install_requires=install_dependencies, 
    description="Desktop client for reading online comic strips", 
)
