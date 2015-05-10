import os
import re

def filematch(f, show):
    sub = show
    output = ""
    for i in sub.split():
        output += i[0]
    if len(output) > 3:
        if re.search(output, f, re.IGNORECASE) != None:
            return True
    if re.search(show, f, re.IGNORECASE) != None:
        return True
    if show.find(' ') != -1:
        if re.search(re.sub([' '], '.', show), f, re.IGNORECASE) != None:
            return True

    return False

def sortshow(show, dfolder):
    for root, dirs, files in os.walk(dfolder):
        for f in files:
            if filematch(f, show):              
                show = show.replace(' ', '')
                s = os.path.join(dfolder, show)
                path = os.path.abspath(os.path.join(root,f))
                newpath = os.path.join(os.path.abspath(s),f)
                print(path)

                if not os.path.isdir(s):
                    os.mkdir(s)
                    os.rename(path, newpath)
                    print(newpath)
                else:
                    os.rename(path, newpath)
                    print(newpath)



#show = input('What do you feel like watching today? ')
#df = input('Where would you like to search for your shows? (type d for Downloads) \n Your search results will be stored in the folder you serched.')
#if df == 'd' or df == 'D':
#    dfolder = 'downloads'
#else:
#    dfolder = df

sortshow('dexter', 'downloads')