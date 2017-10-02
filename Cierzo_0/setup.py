import sys
from cx_Freeze import setup, Executable


excludes = ['tkinter']
packages = ['os', 'docx', 'lxml']

build_exe_options = {
    'excludes': excludes,
    'packages': packages,
    'build_exe': r'.\cierzo.0.0.170808'
    }

exe = Executable(
    script='cierzo_0_0_170808.pyw',
    base='Win32GUI',
    targetName='cierzo_0_0_170808.exe',
    icon='.\icon\Air.ico'
    )

setup(
    name='cierzo',
    version='0.0',
    description='Wind action according to FEM 2131/2132',
    author='P. Biel',
    author_email='structural.eng.biel@gmail.com',
    options={'build_exe': build_exe_options},
    executables=[exe]
    )

# Desde la cónsola: 'python setup.py build'
