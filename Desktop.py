import os
#from os.path import isfile
from pathlib import Path

desktop  = str(Path.home()) + "/Desktop"
os.chdir(desktop)
for item in os.listdir(desktop):
	if os.path.isfile(item):
		print(f'FILE \t {item}')
	elif os.path.isdir(item):
		print(f'DIRECTORY \t {item}')