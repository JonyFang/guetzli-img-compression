# -*- coding:utf-8 -*-
import os
import subprocess
import sys

source = sys.argv[1]
TYPES = ('.jpeg', '.png', '.jpg')

def ensure_dir(img_file):
	folder_path = os.path.split(img_file)[0]
	dir_path = os.path.join(folder_path, 'output')
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

def convert_a_img(img_file):
	file = os.path.split(img_file)[1]
	folder_path = os.path.split(img_file)[0]
	name = os.path.splitext(file)[0]
	suffix = os.path.splitext(file)[1]
	output_path = os.path.join(folder_path, 'output')
    
	url_out = os.path.join(output_path, name + '_mini' + suffix)

	subprocess.call(['guetzli', '--quality', '84', '--verbose', img_file, url_out])
###########################################################################
#main

def main():
	if os.path.isdir(source):
		for root, dirs, files in os.walk(source):
			for a_file in files:
				suffix = os.path.splitext(a_file)[1]
				if suffix in TYPES:
					ensure_dir(os.path.join(root, a_file))
					convert_a_img(os.path.join(root, a_file))
					pass

	elif os.path.isfile(source):
		ensure_dir(source)
		convert_a_img(source)
	
	else:
		print('Please check the input, not found any files or folders.')

main()
