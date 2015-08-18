#!/usr/bin/python
# -*- coding: utf-8 -*-
import simplejson
import urllib
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
API_KEY = 'AIzaSyBp3nFBX2qisgdWugfFwvqD_i4MHzR2t24'


def geocode(address, **geo_args):
    geo_args.update({
        'address': address
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args) + '&key=' + API_KEY + '&language=zh-CN'
    result = simplejson.load(urllib.urlopen(url))

    # print simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)
    # 以json格式打印经纬度座标
    dict = {}
    dict = result['results'][0]['geometry']['location']
    dict['locate'] = address.decode('utf-8')
    for i in dict:
        print dict[i]
#    print simplejson.dumps(dict, encoding="utf-8", indent=2)

if __name__ == '__main__':
    geocode(address='内蒙古锡林浩特查干诺尔')

#with open('locate.csv',  'rb') as csvfile:
#    for line in csv.reader(csvfile,  skipinitialspace=True):
#        if __name__  ==  '__main__':
#            geocode(address=line[0])
