#dependency: streamlink

import os


while True:
    url = input('podaj link: ')
    
    command = 'streamlink ' + url
    
    output = os.system(command)

    jakosc = input('jakosc: ')
    
    command2 = 'streamlink ' + url + " " + jakosc
    
    os.system(command2)
    


    
