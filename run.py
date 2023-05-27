import time
import subprocess

subprocess.run(["start", "cmd", "/k", "py", "server.py"], shell=True)
subprocess.run(["start", "cmd", "/k", "py", "client.py"], shell=True)