# GitC2
C2 that pulls instructions from GitHub

Disclaimer: This is built only for the purposes of research only use on systems you own or have express permission. 

This is based on some reading around APT40 who avoid detection by looking like normal traffic. This script is obvioulsy the simplest form and nothing compared to what they would use but I wanted to get the concept down before I went any further. 

usage: python3 gitc2.py

script will pull from instructions page on this repo every minute searching for abc prefix

it well then decode the base64 encoded command and execute whatever it gets back

to add further instructions simply change url to point to your own git hub and add a base64 encoded command with abc= before it and it will find it and execute.

Code can also be added to instructions.txt in order to paste the contents of docs to github or pastebin for exfil.

This script has zero hits on VirusTotal and would hopefully just look like users connecting to github in any logs.
