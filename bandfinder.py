#!usr/bin/python
#-*-coding: utf-8-*-

import requests
import time
import smtplib
import os

'''pings bandcamp.com for urls starting with word from sowpods, 
emails you a list of urls that aren't taken for band name inspiration'''

PASSWORD = os.environ.get('APP_PW')


def pop_from_file(fname, to_pop):
    with open(fname, 'r+') as f:
        wordlist = [w.strip() for w in f.readlines()]  # for sowpods.txt
        if len(wordlist) >= to_pop:
            potentials = [wordlist.pop(i) for i in range(to_pop)]
            remaining = list(set(wordlist) - set(potentials))
            f.seek(0)
            f.write('\n'.join(remaining))
        elif not wordlist:
            return "out of words!"
        else:
            potentials = wordlist
            f.seek(0)
            f.write('\n'.join(wordlist))
    return potentials


# maybe "the verb nouns" with wordnik later but for now just "word.bandcamp.com"
def ping_bandcamp(number):
    '''takes a number (int) of words to look up from sowpods.txt,
    sees if the url word.bandcamp.com is taken, adds to not_taken list'''
    potentials = pop_from_file(
        '/Users/amp/Dropbox/amanda/projects/bandcamp/bandcamp_namefinder/sowpods.txt', number)
    not_taken = []
    for p in potentials:
        url = "http://" + p + ".bandcamp.com"
        if requests.get(url).history:
            not_taken.append(p)
    if not not_taken:
        return "none today!"
    else:
        return "\n".join(not_taken)


def send_email(from_email, to_email_list, subject, content, password=PASSWORD,              smtpserver='smtp.gmail.com:587'):
    from_addr = from_email
    to_addrs = to_email_list
    msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (from_addr, ", ".join(to_addrs), subject, content)
    try:
        server = smtplib.SMTP(smtpserver)
        server.ehlo()
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_email, password)
        server.sendmail(from_addr, to_addrs, msg)
        server.close()
        print "success!"
    except:
        print "email failed :("

# edit!
if __name__ == '__main__':
    bandnames = ping_bandcamp(100)
    send_email('from email goes here', ['list recipients here'],
               'daily band names', bandnames)
