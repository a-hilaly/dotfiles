import os
import subprocess

ioreg_cpu_data = "ioreg -rc AppleACPICPU"

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
    data, _, _ = _spcc(ioreg_cpu_data)
    count = 1
    auth=False
    print("*********** CPU 0 ***********")
    for d in data[2:14]:
        print(d[6:])
    print("")
    for d in data[24:]:
        if "+-o" in d:
            print("*********** CPU {0} ***********".format(count))
            auth=True
            count += 1
        elif not d:
            continue
        elif d.strip(" ") in ['{', '}']:
            continue
        elif auth:
            print(d.strip(" "))
