#!/bin/env python
# -*- coding: utf-8 -*-

import socket
import urlparse
import sys
import logging
import re

logging.basicConfig(filename=None, level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s %(filename)s %(funcName)s %(lineno)s:\r\n%(message)s')


def extract_session_id(data):
    global session_id
    # print('extract session id')
    for l in data.split('\r\n'):
        # print("line:",l)
        if l.find(':'):
            k = l.split(':')
            if k[0] == 'Session':
                # print(k[1])
                v = k[1].split(';')
                # print(v[0])
                session_id = v[0]  # int(v[0],16)
                # print(session_id)


class RTSPClient:
    def __init__(self, url, mode='UDP', regionid=None, dst='192.168.44.118', port='123456'):
        self.url = url
        self.mode = mode
        self.regionid = regionid
        self.dst_ip = dst
        self.dst_port = port
        self.sock = None
        self.socket_timeout = 3

    def connect(self):
        self.host, self.port = self.get_host_port()
        try:
            if self.sock:
                self.sock.close()
            self.sock = socket.socket()
            if self.mode == 'TCP':
                self.sock.settimeout(self.socket_timeout)
            self.sock.connect((self.host, int(self.port)))
        except Exception, e:
            logging.error(e)
            sys.exit(1)
        else:
            logging.debug('connect to %s:%s success' % (self.host, self.port))

    def get_host_port(self):
        parse = urlparse.urlparse(self.url)
        if ':' in parse[1]:
            return parse[1].split(':')
        else:
            return [parse[1], '80']

    def describe(self):
        while 1:
            msgs = ['DESCRIBE %s RTSP/1.0' % self.url,
                    'CSeq: 1',
                    'Accept: application/sdp',
                    'User-Agent: XJ RTSP 1.0']
            if self.mode == 'QAM':
                msgs.append('x-RegionID: %s' % self.regionid)
            des_msg = '\r\n'.join(msgs) + '\r\n\r\n'
            self.connect()
            logging.debug(des_msg)
            self.sock.sendall(des_msg)
            data = self.sock.recv(65535)
            logging.debug(data)
            if '302 Moved Temporarily' in data:
                self.url = re.search(r'Location: ([^\r\n]*)', data).groups()[0]
                logging.info('302 redirect %s' % self.url)
            elif '200 OK' in data:
                break
            else:
                sys.exit(1)

    def setup(self, seq=0):
        global session_id
        if self.mode == 'UDP':
            trans_mode = 'Transport: MP2T/UDP;unicast;destination=%s;client_port=%s-%s' % (
            self.dst_ip, self.dst_port, (int(self.dst_port) + 1))
        else:
            trans_mode = 'Transport: MP2T/TCP;interleaved=0-1'
        setup_msg = 'SETUP %s/trackID=%s RTSP/1.0\r\n' \
                    'CSeq: 2\r\n' \
                    '%s\r\n' \
                    'User-Agent: XJ RTSP 1.0\r\n\r\n' % (self.url, seq, trans_mode)
        logging.debug(setup_msg)
        self.sock.sendall(setup_msg)
        data = self.sock.recv(65535)
        extract_session_id(data)
        logging.debug(data)
        print (session_id)

    def play(self):
        global session_id
        play_msg = 'PLAY %s RTSP/1.0\r\n' \
                   'CSeq: 4\r\n' \
                   'Range: npt=0-\r\n' \
                   'Session: %s\r\n' \
                   'x-prebuffer: maxtime=10.00\r\n' \
                   'User-Agent: XJ RTSP 1.0\r\n\r\n' % (self.url, session_id)
        logging.debug(play_msg)
        self.sock.sendall(play_msg)
        data = self.sock.recv(65535)
        logging.debug(data)
        logging.info('Playing %s' % self.url)

    def wait_data_udp(self, timeout=86400):
        while 1:
            self.sock.settimeout(timeout)
            data = self.sock.recv(65535)
            if 'x-Reason: "END"' in data:
                logging.info('Playing end')
                # sys.exit(0)
                break
            else:
                logging.error(data)
                sys.exit(1)

    def wait_data_tcp(self):
        while 1:
            try:
                data = self.sock.recv(655350)
            except Exception, e:
                logging.debug('TCP recv data %s,Maybe end...' % e)
                break

            if not len(data):
                logging.debug('tcp rec data over')
                break
            else:
                logging.debug('recv data %d' % len(data))

    def run(self):
        self.describe()
        self.setup(0)
        self.setup(1)
        self.play()
        if self.mode == 'TCP':
            self.wait_data_tcp()
        else:
            self.wait_data_udp()


if __name__ == '__main__':
    while 1:
        try:
            url = sys.argv[1]
            if len(sys.argv) == 2:
                mode = 'TCP'
            else:
                mode = sys.argv[2]
            if mode == 'QAM':
                region = sys.argv[3]
            else:
                region = None
        except Exception, e:
            logging.error(e)
            print 'Usage:%s rtsp_url [[TCP]|UDP|(QAM 0x1)]' % sys.argv[0]
            sys.exit(1)
        c = RTSPClient(url, mode, region)
        c.run()
