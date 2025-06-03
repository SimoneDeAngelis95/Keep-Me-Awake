"""
Usage:
To create a macOS app bundle using py2app, run the following command in the terminal:
    - pip install py2app
    - python setup_macos.py py2app
    - This will generate a .app bundle in the 'dist' directory.
This script is used to package a Python application into a macOS app bundle using py2app.

This setup works with macOS silicon and intel architectures.
"""

from setuptools import setup
import src.globalVariables as GV


APP = ['src/main.py']
DATA_FILES = [
    GV.ICON_PATH,
    "src/" + GV.STYLE_FILE
]

OPTIONS = {
    'iconfile': GV.ICON_PATH,
    'plist':{
        'CFBundleName': GV.APP_NAME,
        'CFBundleVersion': GV.APP_VERSION,
        'CFBundleShortVersionString': GV.APP_VERSION, 
        'CFBundleExecutable': GV.APP_NAME,
        'NSHumanReadableCopyright': '© 2024-2025 Made with Love by Simone De Angelis',
        'CFBundleIdentifier': 'com.simonedeamelis.keepmeawake',                        # Unique identifier for the app
        'LSApplicationCategoryType': 'public.app-category.utilities',                  # Application category
        'NSHighResolutionCapable': True,                                               # Support for high-resolution displays
    },
    'excludes': ['tkinter'],                                                           # Exclude unnecessary modules to reduce app size
    'optimize': 2,                                                                     # Python bytecode optimization level
}

setup(
    app=APP,
    data_files=DATA_FILES,
    author=GV.APP_AUTHOR,
    copyright=GV.APP_AUTHOR,
    description="Keep Me Awake is a simple macOS app that prevents your Mac from going to sleep.",
    license="GPLv3",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)