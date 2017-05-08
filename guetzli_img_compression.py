# -*- coding:utf-8 -*-
import os
import subprocess
import sys
import imghdr

source = sys.argv[1]
print('--source: ' + source)

def convert_a_img(img_file):
	print('--img_file: '+img_file)
	print('--source: '+source)
	# filename = os.path.splitext(os.path.split(img_file)[1])[0]
	filename = os.path.split(img_file)[1]
	print('--filename: '+filename)
	# url = os.path.join(root, filename)
	# print('--url: '+url)
	url_out = os.path.join(source, '-'+filename)
	print('--url_out: '+url_out)
	print('---execute: ' + 'guetzli --quality 84 --verbose ' + img_file + ' ' + url_out)

	subprocess.call(['guetzli', '--quality', '84', '--verbose', img_file, url_out])
###########################################################################
#main

def main():
	if os.path.isdir(source):
		for root, dirs, files in os.walk(source):
			for a_file in files:
				convert_a_img(os.path.join(root, a_file))

	elif os.path.isfile(source):
		convert_a_img(source)
	
	else:
		print('Please check the input, not found any files or folders.')

main()