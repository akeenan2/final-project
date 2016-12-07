import os
import sys
# add src to python path
sys.path.insert(0, 'src')
import db # from db.py

for name,url in db.urls.iteritems():
    print url
    os.system('python src/mapper.py -u {} -f data/{}-map.txt'.format(url,name))
