import os

def sortshow(show, dfolder):
    for root, dirs, files in os.walk(dfolder):
        for f in files:
            print(f)
            if f == 'testgaur.txt':
                print("wooo")
            #TODO 1): finna nafnið í strengnum, há og lágstafa kombó, engin bil               
                show = show.replace(' ', '')
                s = os.path.join(dfolder, show)
            
                path = os.path.abspath(os.path.join(root,f))
                newpath = os.path.join(os.path.abspath(s),f)

                if not os.path.isdir(s):
                    os.mkdir(s)
                    os.rename(path, newpath)
                    print(newpath)
                else:
                    os.rename(path, newpath)
                    print(newpath)
                
                #Setja allar skrár sem þetta passar við í eina möppu
                #print(f)




#show = input('What do you feel like watching today? ')
#df = input('Where would you like to search for your shows? (type d for Downloads) \n Your search results will be stored in the folder you serched.')
#if df == 'd' or df == 'D':
#    dfolder = 'Downloads'
#else:
#    dfolder = df

sortshow('house of cards', 'test')