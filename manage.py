#!/usr/bin/env python3
import time
import subprocess, sys


print("session started!!!")
one = subprocess.run(f"python ./server.py | python ./app-server.py {sys.argv[1]}", shell=True)

print("session finished!!!")