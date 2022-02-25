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

# Docker
1. Install Docker Desktop for your plaform:
  - [Windows](https://docs.docker.com/desktop/windows/install)
  - [Linux](https://docs.docker.com/engine/install/ubuntu/)
  - [Mac](https://docs.docker.com/desktop/mac/install)
2. Run command, put your actual url instead of www.abc.com :
```
docker run --rm -it nitupkcuf/ddos-ripper:latest www.abc.com
```
# 
