from utils import get_path
import requests
import os
print ('Hello This is SAE News')
d = os.path.dirname(os.path.abspath(utils.__file__))
url = 'http://updateinspyre.surge.sh/hello.py'
r = requests.get(url)
f = open('updater.py','wb')
f.write(r.content)
f.close()

print ('Downloaded')

