'''
Python script file to remind myself to take a rest every hour
Use python GUI message box to interrupt work
Uncommet codes to switch to use web browser if you want
'''
import time
# from easygui import msgbox
import webbrowser


while True:
	time.sleep(3600)
	# msgbox('Take a five-minute rest!')
	webbrowser.open("https://makeameme.org/meme/get-your-rest-gpg45u")
