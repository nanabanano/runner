```
git clone https://github.com/nanabanano/runner.git
cd runner
pip install -r requirements.txt

pyinstaller app.py --collect-all dns --add-data="headers.txt:." --add-data="DRipper.py:." --onefile
```
see dist folder
