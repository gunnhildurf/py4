import os

def sortshow(show, dfolder, target):
    for root, dirs, files in os.walk(dfolder):
        for f in files:
            if f == show:
                print(f)


sortshow('www.Torrentday.com.txt', 'downloads', 'c')