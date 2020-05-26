import subprocess
import collections
import xml.etree.cElementTree as ET
import pathlib
import socket

def XMLPATH(nameSSID):
    path = str(pathlib.Path(__file__).parent.absolute())
    path = path.replace('\\', '/')[1:]
    path = 'C'+path+'/wi-fi/'+str(nameSSID)+'.xml'
    return path

def is_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False
        
def is_current(id = None):
    try:
        ssid = subprocess.check_output("netsh wlan show interfaces")
        ssid = ssid.decode("ascii")
        ssid = ssid.replace("\r","")
        ssid = ssid.split("\n")[19]
        ssid = (ssid.split(": ")[1]).strip()
        if ssid == id:
            return True
        else:
            return ssid
    except:
        pass
    return False

def ARRSSID():
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    SSID = []
    for ssid in ssids:
        try:
            SSID.append(ssid.split(': ')[1])
        except:
            pass
    nSSID = []
    for id in SSID:
        if not is_current(id)==True:
            nSSID.append(id)
    return nSSID

def SSIDPASS(SSID = None):
    arr = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            arr.append("{:<}|{:<}".format(i, results[0]))
        except IndexError:
            arr.append("{:<}|{:<}".format(i, ""))
    if SSID != None:
        try:
            for a in arr:
                val = a.split(SSID+'|')[1]
                if len(val)>1:
                    return val
        except:
            return ""
    return arr

def connect_to_profile(path):
    process = subprocess.Popen(
        'netsh wlan add profile filename=' + path,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

def mkSense(string, limit=3):
    frequencies = collections.Counter(string)
    repeated = {}
    for key, value in frequencies.items():
        if value > 1:
            repeated[key] = value
    
    for attr, value in repeated.items():
        if value > limit:
            return False
    return True

def setWIFI(name, password):
    WLANProfile = ET.Element("WLANProfile", xmlns="http://www.microsoft.com/networking/WLAN/profile/v1")
    name = ET.SubElement(WLANProfile, "name").text = name
    SSIDConfig = ET.SubElement(WLANProfile, "SSIDConfig")
    SSID = ET.SubElement(SSIDConfig, "SSID")
    ET.SubElement(SSID, "hex").text = (name.encode().hex()).upper()
    ET.SubElement(SSID, "name").text = name
    connectionType = ET.SubElement(WLANProfile, "connectionType").text = "ESS"
    connectionMode = ET.SubElement(WLANProfile, "connectionMode").text = "auto"
    MSM = ET.SubElement(WLANProfile, "MSM")
    MacRandomization = ET.SubElement(WLANProfile, "MacRandomization", xmlns="http://www.microsoft.com/networking/WLAN/profile/v3")
    ET.SubElement(MacRandomization, "enableRandomization").text = "false"
    security = ET.SubElement(MSM, "security")
    authEncryption = ET.SubElement(security, "authEncryption")
    ET.SubElement(authEncryption, "authentication").text = "WPA2PSK"
    ET.SubElement(authEncryption, "encryption").text = "AES"
    ET.SubElement(authEncryption, "useOneX").text = "false"
    sharedKey = ET.SubElement(security, "sharedKey")
    ET.SubElement(sharedKey, "keyType").text = "passPhrase"
    ET.SubElement(sharedKey, "protected").text = "false"
    ET.SubElement(sharedKey, "keyMaterial").text = password
    tree = ET.ElementTree(WLANProfile)
    tree.write(XMLPATH(name))
    connect_to_profile(XMLPATH(name))