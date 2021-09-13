#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()
import os
import shutil

#Очистка старых файлов
directory = './uploads'
print('directory' + directory)
files = os.listdir(directory)
if(files):
	print('files' + files[0])
	os.remove(directory + "/" + files[0])
	sourcefn = files[0].split('.')[0]
	targetFolder = './' + sourcefn + '_umxl'
	print('targetFolder' + targetFolder)
	if(os.path.exists(targetFolder)):
		shutil.rmtree(targetFolder)
		print('targetFolder DELETE')

	
f = open(os.getcwd() + '/uploaded.html', 'r', encoding='UTF-8')
s = f.read()
f.close()
print('Content-type: text/html\n')

form = cgi.FieldStorage()
fn = 'fileIsNotExist'

fileitem = form["filename"]

if fileitem.filename:
	fn = os.path.basename(fileitem.filename)
	open('uploads/' + fn, 'wb').write(fileitem.file.read())
	#message = 'Sound file is uploaded successfully'
	#print(message)

else:
	message = 'Sound file was not uploaded'
	print(message)

print(s)
