# python_vba_excel_learning
Started to learn python and vba for excel data processing
# HOWTO setup python develop environment on windows 10
1) Download Python-2.7.14 and Python Python-3.6.4 from https://www.python.org/downloads/
2) Double click the Python-2.7.14 and Python-3.6.4 installer to install
     - choose to add into PATH 
     - chosse customized installation path
3) Go to the Python-2.7.14 and Python-3.6.4 installation path to copy python.exe and pythonw.ext and paste them in the same location
     - change the copied ones into python2.exe pythonw2.exe and python3.exe and pythonw3.exe respectively
     - pip2 and pip3 are also ready
4) Install the sublime text 3 editor from https://www.sublimetext.com/3
5) Install virtualenv by "pip install virtualenv"
6) Using virtualenv to create python2 and python3 virtual environment
     e.g.
     - E:\>virtualenv --python=E:\Python27\python.exe python27env
         Running virtualenv with interpreter E:\Python27\python.exe
         New python executable in E:\python27env\Scripts\python.exe
         Installing setuptools, pip, wheel...done.

     - E:\>virtualenv --python=E:\Python36\python.exe python36env
         Running virtualenv with interpreter E:\Python36\python.exe
         Using base prefix 'E:\\Python36'
         New python executable in E:\python36env\Scripts\python.exe
         Installing setuptools, pip, wheel...done.

     - E:\python27env\Scripts>activate

     - (python27env) E:\python27env\Scripts>python --version
       Python 2.7.14

     - (python27env) E:\python27env\Scripts>deactivate

     - E:\python36env\Scripts>activate

     - (python36env) E:\python36env\Scripts>python --version
       Python 3.6.4

     - (python36env) E:\python36env\Scripts>deactivate
