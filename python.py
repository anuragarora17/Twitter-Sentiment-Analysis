import urllib
import json

try:
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
except urllib.IOError as e:
    error = e.read()
    print error

print json.load(response)