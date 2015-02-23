# bandcamp_namefinder

pings bandcamp for urls from the scrabble words dictionary, and emails you a list of bandcamp urls/band names that aren't taken. WIP.

## usage
1. clone the repo
2. set your email password as an environment variable: ```export APP_PW="youremailpassword"```
(note: if you use two-factor authentication for gmail, you'll need to make an app-specific password first and use that one.)
3. edit the ```__main__``` block of the script with your email and the emails you want to send updates to, and the amount of band names you want to check for
4. run ```python bandfinder.py``` (or setup a cron job to run the script and email you once a day)

## todo
1. cron job to send 1x/day
2. prompt user for from email, to email list so they don't need to edit the script