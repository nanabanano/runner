Python 3.10

```
git clone https://github.com/nanabanano/runner.git
cd runner
pip3 install pyinstaller
pip3 install -r requirements.txt

# mac
pyinstaller app.py --collect-all dns --add-data="headers.txt:." --add-data="DRipper.py:." --onefile

# win
pyinstaller --collect-all dns --add-data "headers.txt;." --add-data "DRipper.py;." --onefile app.py

```
see dist folder
