"""
Explains usage of webbrowser module for scrapping

launching python programs and creating batch files 
bat file and its contents and then ,windows+run , type program name and followed by arguments as below
e.g : mapit 870 Valencia St.
@py.exe c:\users\al\mypythonscripts\hello.py %*
@pause

"""

import webbrowser,sys,pyperclip

sys.argv  #['mapit.py','870','Valencia','St.']

if len(sys.argv) > 1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()
    
    
webbrowser.open('https://www.google.com/maps/place/'+address)


