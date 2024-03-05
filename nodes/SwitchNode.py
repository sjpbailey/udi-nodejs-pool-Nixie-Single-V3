
import udi_interface
import json
import requests
import sys
import time
import urllib3

LOGGER = udi_interface.LOGGER


class SwitchNode(udi_interface.Node):

    def __init__(self, polyglot, primary, address, name, apiBaseUrl, api_url):

        super(SwitchNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)

        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.address = address
        LOGGER.info(self.address)
        self.name = name
        LOGGER.info(name)
        self.apiBaseUrl = apiBaseUrl
        id = address.strip('zone_')
        id1 = id
        LOGGER.info(id1)
        self.id1 = id1
        self.api_url = api_url

    def start(self):
        LOGGER.info(self.address)
        self.http = urllib3.PoolManager()
        self.allData = requests.get(
            url='{}/state/all'.format(self.apiBaseUrl))

        if self.allData.status_code == 200:
            self.setDriver('ST', 1)
        else:
            self.setDriver('ST', 0)

        self.allDataJson = self.allData.json()
        # LOGGER.info("Circuit On {}".format(
        #    self.allDataJson["circuits"][0]['isOn']))

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            LOGGER.debug('shortPoll (node)')
            self.reportDrivers()

    def cmd_on(self, command):

        json_data = {
            'id': self.id1,
            'isOn': 1,
        }

        response = requests.put(
            self.api_url + '/state/circuit/setState/',  json=json_data)

        self.setDriver('GV1', 1)

    def cmd_off(self, command):

        json_data = {
            'id': self.id1,
            'isOn': 0,
        }

        response = requests.put(
            self.api_url + '/state/circuit/setState/',  json=json_data)

        self.setDriver('GV1', 0)

    def query(self, command=None):
        self.reportDrivers()
        self.start()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 25, 'name': 'Online'},
        {'driver': 'GV1', 'value': 0, 'uom': 25, 'name': 'Enabled'}
    ]

    id = 'switchnodeid'

    commands = {
        'DON': cmd_on,
        'DOF': cmd_off,
        'QUERY': query
    }
