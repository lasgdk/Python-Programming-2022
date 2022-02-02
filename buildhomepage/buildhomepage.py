
# Get data from folder, and build pages containing:
# Header information
# Menu
# Content
# Footer information

# Header and footer should be the same for each generated page
# Menu also, but menu must be build dynamically based on the files and folders

# Two main folders? Source and Published? 
# Use CSS to place content nicely, but it must be working fine without as well.

INPUTFOLDER="source"
OUTPUTFOLDER="published"
PAGETITLE='Testside'
CSSFILE='' #can be omitted

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
        </div>
        <div class="menu">
            <h2>Menu</h2>
            <p>Menupunkter...</p>
        </div>
        <div class="main">
'''

footerdata='''
        </div>
        <div class="footer">
            <p>Footertekst</p>
        </div>
    </body>
</html>
'''

import os
# rootdir = 'C:/Users/Admin/Desktop/'

for subdir, dirs, files in os.walk(INPUTFOLDER):
    for file in files:
        # print(os.path.join(subdir, file))
        if file.endswith((".html",".htm")):
            print ("The file: "+os.path.join(subdir, file)+" is a HTML file to be computed")
            data = headerdata
            inputfile=INPUTFOLDER+'/'+file
            with open(inputfile) as fp:
                data += fp.read()
            data += footerdata
            outputfile=OUTPUTFOLDER+'/'+file
            print("Saving file to: "+outputfile)
            with open (outputfile, 'w') as fp:
                fp.write(data)

