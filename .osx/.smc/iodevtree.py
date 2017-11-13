import os
import subprocess

ioreg_dev_tree = "ioreg -p IODeviceTree"

cbts = lambda x : x.decode('utf-8')

def _cbtr(ln):
    r = []
    for i in ln.split(b'\n'):
        if i:
            r += [cbts(i)]
    return r

def _spcc(cmd):
    c = cmd.split(' ')
    p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return _cbtr(stdout), _cbtr(stderr), p.returncode

if __name__ == "__main__":
    data, _, _ = _spcc(ioreg_dev_tree)
    for d in data:
        print(d)
