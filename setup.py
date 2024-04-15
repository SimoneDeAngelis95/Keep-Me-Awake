from setuptools import setup

APP = ['main.py']
DATA_FILES = ['style.css']
OPTIONS = {
    'iconfile': 'icon.png',
    'plist':{
        'CFBundleName': 'Keep Me Awake',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleExecutable': 'Keep Me Awake'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    author="Simone De Angelis",
    copyright="Simone De Angelis",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
