
# Get data from folder, and build pages containing:
# Header information
# Menu
# Content
# Footer information

# Header and footer should be the same for each generated page
# Menu also, but menu must be build dynamically based on the files and folders

# Two main folders? Source and Published? 
# Use CSS to place content nicely, but it must be working fine without as well.

import os
from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, '')

INPUTFOLDER="source"
OUTPUTFOLDER="published"
PAGETITLE='Testside'
CSSFILE='stil.css' #can be omitted
BASEURL='https://lasg.dk/'  #can be omitted, but folders wont work. Should be like https://lasg.dk/

now = datetime.now()
buildtime=now.strftime("%A d.%d. %B, %Y klokken %H:%M")
buildnotice='Hjemmesiden er tilset '+buildtime

headerdata='''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>'''+PAGETITLE+'''</title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="stylesheet" href="'''+CSSFILE+'''">
    </head>
    <body>
        <div class="header">
            <h1>Overskrift</h1>
            <p>Headertekst</p>
            <hr />
        </div>     
'''

footerdata='''
        </div>
        <div class="footer">
            <hr />
            <p>'''+buildnotice+'''</p>
            <p>Footertekst: Copyright xyz, Kontaktinfo: 123@123.123</p>
        </div>
    </body>
</html>
'''

# Iterate though source files to generate the menu
print("Starting generating the menu...")
menudata='<div class="menu"><h2>Menu:</h2><ul>'    
for subdir, dirs, files in os.walk(INPUTFOLDER):
    for file in files:
        if file.endswith((".html",".htm")):
            print("Current subdir for input is: "+subdir)
            outdir=subdir.replace(INPUTFOLDER, '')
            print("Current subdir for output is: "+outdir)
            menubullet=outdir+'/'+file
            menubullet=menubullet[1:]   #Remove first char which is either \ or /
            url=BASEURL+menubullet
            # menutitle=' '.join(menubullet.split('.')[:-1])
            menutitle=menubullet[:menubullet.rfind(".")]    #Remove trailing file extension (from last . and out)
            menutitle=menutitle.replace('/', ': ')
            menutitle=str.title(menutitle)  #Make Titles Nicer With Large First Letter
            print("Adding the following file to the menu: "+menubullet)
            menudata+='<li><a href="'+url+'">'+menutitle+'</a></li>'
menudata+='</ul></div><br /><div class="main"><hr />'
print("Complete menu looks like: "+menudata)
print("Stopped generating the menu.")


# Iterate though source files to generate the published files
for subdir, dirs, files in os.walk(INPUTFOLDER):
    for file in files:
        
        if file.endswith((".html",".htm")):
            print ("The file: "+os.path.join(subdir, file)+" is a HTML file to be computed")
            
            # Collect the part of the page, and concatenate them all
            data = headerdata
            data += menudata
            inputfile=subdir+'/'+file
            with open(inputfile) as fp:
                data += fp.read()
            data += footerdata

            print("Current subdir for input is: "+subdir)
            outdir=subdir.replace(INPUTFOLDER, OUTPUTFOLDER)
            print("Current subdir for output is: "+outdir)

            # Write the output file
            outputfile=outdir+'/'+file
            print("Saving file to: "+outputfile)
            with open (outputfile, 'w') as fp:
                fp.write(data)

