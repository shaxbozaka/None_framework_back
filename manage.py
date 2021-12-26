#!/usr/bin/env python3
import time
import subprocess


print("session started!!!")
one = subprocess.run("python ./server.py | python ./app-server.py", shell=True)

print("session finished!!!")