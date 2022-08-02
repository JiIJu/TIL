import glob
import json
import os

File_List = glob.glob('C:\Users\multicampus\Desktop\코드저장폴더\0722\python-master-01_python-project-project01\python-master-01_python-project-project01\01_python\project\project01\data\movies/*.json')

for i in File_List:
    f = open(i,'r')
    js = json.loads(f.read())
    print "id : %s" % (js['id'])
    f.close()
