import json
import requests

file = '../data/icd10cm_tabular_2019.json'

el_path = 'handbook'
el_type = 'icd10'

with open(file, encoding='utf-8') as f:
    elements = json.load(f)

for i, e in enumerate(elements):

    location = "http://localhost:9200/{}/{}/{}?pretty".format(el_path, el_type, i)
    headers = {'Content-Type': 'application/json'}
    r = requests.put(location, headers=headers, data=json.dumps(e))

    if 200 <= r.status_code < 300:
        print("{} OK".format(i))
    else:
        print("{} ERROR {}".format(i, r.status_code))
        print(r.content)
        break
