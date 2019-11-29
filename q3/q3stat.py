#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import re, socket

class Q3PlayerInfo:
    __slots__ = ('score', 'ping', 'captures', 'name')
    def __init__(self, score, ping, captures, name):
        self.score, self.ping, self.captures, self.name = (score, ping, captures, name)

'''
ServerInfo.status = {
    'game':             'CTF',
    'maxPing':          '550',
    'voip':             '1',
    'g_humanplayers':   '8',
    'g_needpass':       '0',
    'pure':             '1',
    'gametype':         '4',
    'sv_maxclients':    '25',
    'clients':          '9',
    'mapname':          'oasago2',
    'hostname':         '  ^1:F ^7normal ctf for stupids',
    'protocol':         '71'
  }
'''

# TODO
# 76 50 "^31 ^7bARB"
# 4 36 "^00^20.6 ^7^1PRO^7fessorOf^4CAMPING"
# 79 48 "^30 ^7^0CK-^4cheers"

class Q3ServerInfo:
    PREAMBLE  = bytes([0xFF]*4)
    GETINFO   = PREAMBLE + 'getinfo\n'.encode('ASCII')
    GETSTATUS = PREAMBLE + 'getstatus\n'.encode('ASCII')

    __slots__ = ('ip', 'port', 'info', 'status', 'players')
    def __init__(self, ip, port):
        self.ip, self.port = ip, port
        self.info    = {}
        self.status  = {}
        self.players = []

    def query(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            s.settimeout(10)
            s.connect((self.ip, self.port))
            s.send(Q3ServerInfo.GETINFO)
            getinfo_response = s.recv(8192)
            s.send(Q3ServerInfo.GETSTATUS)
            getstatus_response = s.recv(8192)
            s.shutdown(socket.SHUT_RDWR)

            self.decodeInfo(getinfo_response)
            self.decodeStatus(getstatus_response)
            print(getinfo_response)
            #print(getstatus_response)
        except Exception as e:
            print(self.ip, self.port, e)

    def decodeInfo(self, data):
        if data[:4] != Q3ServerInfo.PREAMBLE:
            raise Exception('decodeInfo: Invalid preamble')
        info = data[4:].decode('ASCII')
        info = info.replace('infoResponse\n\\', '')
        info = info.split('\\')
        result = {}
        for i in range(0, len(info), 2):
            result[info[i]] = info[i+1]
        self.info = result
        print(self.info)

    def decodeStatus(self, data):
        if data[:4] != Q3ServerInfo.PREAMBLE:
            raise Exception('decodeStatus: Invalid preamble')
        status = data[4:].decode('ASCII')
        status = status.replace('statusResponse\n\\', '')
        status, playerstatus = status.split('\n', 1)
        status = status.split('\\')
        print(repr(playerstatus))

        result = {}
        for i in range(0, len(status), 2):
            result[status[i]] = status[i+1]
        self.status = result

        self.players = []
        for p in playerstatus.split('\n'):
            if p:
                print(p)
                score, ping, captures_and_name = p.split(' ', 2)
                captures_and_name = captures_and_name.strip('"')
                captures, name = captures_and_name.split(' ', 1)
                captures = re.sub(r'\^.', '', captures)
                self.players.append(Q3PlayerInfo(score, ping, captures, name))


