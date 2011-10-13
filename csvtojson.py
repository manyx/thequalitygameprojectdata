import csv
import json
import sys
from itertools import izip
import hashlib

shared_private_key = "#TODO write private key here"

def enryptUsername(user):
    return hashlib.sha1(repr(user) + "_" + shared_private_key).hexdigest()


if (len(sys.argv) > 3):
    out = []
    keys = ("user","contest","entry")
    #users
    f = open( sys.argv[1], 'r' )
    readerUsers = csv.reader( f )
    f.closed
    keysUsers =  readerUsers.next()
    users = []
    users = [dict(zip(keysUsers, property)) for property in readerUsers]
    for user in users:
        user['username'] = enryptUsername(user['username'])
    #contests
    f = open( sys.argv[2], 'r' )
    readerContests = csv.reader( f )
    f.closed
    contestKeys =  readerContests.next()
    contests = []
    contests = [dict(zip(contestKeys, property)) for property in readerContests]
    #entries
    f = open( sys.argv[3], 'r' )
    readerEntries = csv.reader( f )
    f.closed
    entrieKeys =  readerEntries.next()
    entries = []
    entries = [dict(zip(entrieKeys, property)) for property in readerEntries]
    out = {"users" : users, "contests" : contests, "entries" : entries}
   
    with open('out.txt', 'w') as f2:
        read_data = f2.write(json.dumps(out))
        f2.closed
        
        #print json.dumps(out)
else: 
    print "Usage: csvtojson.py user.csv contest.csv entry.csv"

