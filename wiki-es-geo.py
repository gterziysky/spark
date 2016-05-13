#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sudo pip install requests --upgrade
# sudo pip install socketIO_client==0.5.6
# sudo pip install pygeoip

import json
import re
import requests
import socketIO_client
import pygeoip

es = "http://54.237.243.172:9200"
ipaddr = re.compile(r'^\d+.\d+.\d+.\d+$')
gi = pygeoip.GeoIP('./GeoLiteCity.dat')

# this script depends on the wikiedits index already having been created
# in elasticsearch with the correct mapping

# requests.post(es + "/wikiedits")
# mapping = {
#     'properties': {
#         'timestamp': {'type': 'date', 'format': 'epoch_second'},
#         'ip': {'type': 'ip'},
#         'location': {'type': 'geo_point'}
#     }
# }
# requests.put(es + "/wikiedits/wikiedit/_mapping", json.dumps(mapping))

class WikiNamespace(socketIO_client.BaseNamespace):
    def on_change(self, change):
        if change is not None:
            print(change)

            # add ip address and location, if possible
            if ipaddr.match(change['user']):
                change['ip'] = change['user']
                location = gi.record_by_addr(change['ip'])
                change['location'] = str(location['latitude']) + ',' + str(location['longitude'])

            data = json.dumps(change)
            requests.post(es + "/wikiedits/wikiedit/", data)

    def on_connect(self):
        # doesn't have to be *; for example, could be en or de
        self.emit('subscribe', '*.wikipedia.org')

socketIO = socketIO_client.SocketIO('stream.wikimedia.org', 80)
socketIO.define(WikiNamespace, '/rc')

while True:
    socketIO.wait(10)
    
