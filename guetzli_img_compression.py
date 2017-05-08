# -*- coding:utf-8 -*-
import os
import subprocess
import sys
import imghdr

source = sys.argv[1]
TYPES = ('.jpeg', '.png', '.jpg')

def convert_a_img(img_file):
	filename = os.path.split(img_file)[1]
	url_out = os.path.join(source, '-'+filename)

	subprocess.call(['guetzli', '--quality', '84', '--verbose', img_file, url_out])
###########################################################################
#main

def main():
	if os.path.isdir(source):
		for root, dirs, files in os.walk(source):
			for a_file in files:
				suffix = os.path.splitext(a_file)[1]
				if suffix in TYPES:
					convert_a_img(os.path.join(root, a_file))
					pass

	elif os.path.isfile(source):
		convert_a_img(source)
	
	else:
		print('Please check the input, not found any files or folders.')

main()
