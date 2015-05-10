import os


def filematch(f, show):
    if f.find(show) != -1:
        return True

def sortshow(show, dfolder):
    for root, dirs, files in os.walk(dfolder):
        for f in files:
            print(f)
            if filematch(f, show):              
            #TODO: matcha f (filename) við margar útgáfur af show
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
#    dfolder = 'Downloads'
#else:
#    dfolder = df

sortshow('dexter', 'test')