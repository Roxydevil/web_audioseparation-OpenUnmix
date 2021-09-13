#!/usr/bin/env python3

import os

f = open(os.getcwd() + '/download.html', 'r', encoding='UTF-8')
s = f.read()
f.close()
print('Content-type: text/html\n')
print(s.partition('<span id="a_001"></span>')[0])

directory = './uploads'
files = os.listdir(directory)

def bashFunc():
	bashCommand = "umx ./uploads/" + files[0] + " --targets vocals --residual true"
	os.system(bashCommand)


try:
	bashFunc()
except bashFuncError:
	print(bashFuncError)

sourcefn = files[0].split('.')[0]
targetFolder = '/' + sourcefn + '_umxl/'
donloadLinks = [
	targetFolder + 'vocals.wav',
	targetFolder + 'residual.wav'
]
print('<a href="' + donloadLinks[0] + '" download class="a_mainButton"><div class="mainButton">Download vocal</div></a>')
print('<a href="' + donloadLinks[1] + '" download class="a_mainButton"><div class="mainButton">Download music</div></a>')

print(s.partition('<span id="a_002"></span>')[2])