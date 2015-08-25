#!/usr/bin/python
# -*- coding: utf-8 -*-
import simplejson
import urllib
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
API_KEY = 'AIzaSyCPMJgJ8OhTrQb95YQtvhXVXiYP8MhFr54'
headers = ['ID',  'locate', 'lat', 'lng']

with open('stocks.csv', 'wb') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()

def geocode(address, id, **geo_args):
    geo_args.update({
        'address': address
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args) + '&key=' + API_KEY + '&language=zh-CN'
    result = simplejson.load(urllib.urlopen(url))
    print result
    # print simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)
    # 以json格式打印经纬度座标
    dict = {}
    dict = result['results'][0]['geometry']['location']
    dict['locate'] = address.decode('utf-8')
    dict['ID'] = id

    with open('stocks.csv', 'a+') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerow(dict)

#    print simplejson.dumps(dict, encoding="utf-8", indent=2)

#if __name__ == '__main__':
#    geocode(address='四川双流万安乡', id=777)

with open('locate.csv') as source:
    source_csv = csv.reader(source)
    h = next(source_csv)
    for row in source_csv:
        if __name__  ==  '__main__':
            geocode(address=row[1],  id=row[0])
