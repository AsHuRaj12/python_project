# how_to_read_write_json_file
#This repository contains my AI and Data Science projects using Python.

#read.

import json
with open('ashu.json','r') as f:
    data = json.load(f) 
    print(data)

#upload.


import json
student={
    'Name':'Ashu',
    'Age':18,
    'Marks':99
}
with open('ashu.json','w') as f :
    json.dump(student,f)
