import os
import sys

list = os.listdir()

for i in range(len(list)):
	if list[i].endswith(".py"):
		None
	else:
		os.system(list[i])