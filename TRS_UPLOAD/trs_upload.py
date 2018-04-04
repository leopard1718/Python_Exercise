#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import popen, system, listdir, remove
import httplib
import xml.etree.ElementTree as ET
import cPickle

timer_list = ('tsu-record-monitor', 'tsu-record-query', 'tsu-record-start')
deploy_dir = '/opt/contex'


class Main_Upload():

    '''
    TRS升级类：
    get_channel函数：获取当前服务器收录的频道名称
    start_time_set函数：启动CCM的定时校验的任务
    st_time_set函数：停止CCM的定时校验的任务
    postman函数：接口报文的下发功能
    trs_upload函数：升级的相关操作
    control_center函数：控制中心，控制控制所有函数的执行顺序
    '''

    def __init__(self):
        self.input_type = 0
        self.cache_type = ['record', 'XSpliter', 'XEliminator']

    def get_channel(self):
        print '开始获取收录频道名: ',
        channel_list = []
        # 新建一个频道列表，用来存储获取的收录频道名
        try:
            for channel in listdir(deploy_dir):
                # 调用os.listdir方法获取变量deploy_dir目录下所有频道
                if channel.endswith(('h264', 'mpeg4')):
                    # 判断频道字符尾部是否包含h264和mpeg4
                    channel_list.append(channel)
                    # 将符合以上条件的加入列表
            return channel_list
        except:
            print '获取收录频道名遇到问题'

    def start_time_set(self):
        print '开启定时任务： ',
        for timer_id in timer_list:
            tree = ET.parse('timer_set.xml')
            for commendid in tree.findall('body')[0].findall('timer'):
                if commendid.attrib['id'] != '':
                    commendid.set("id", timer_id)
                    commendid.set('parameter', '1')
                    commendid.set('operation', '1')
                else:
                    commendid.set("id", timer_id)
                tree.write('start_timer_set.xml')
                start_xml = open('start_timer_set.xml', 'r')
                get_resopnse = self.postman(6060, start_xml)
                try:
                    _tree = ET.fromstring(get_resopnse)
                    for hearder in _tree.findall('header'):
                        component_id = hearder.attrib.get('component-id')
                        for item in _tree.findall('body')[0].findall('result'):
                            if item.attrib.get('code') == '0':
                                if item.attrib.get('description') == 'OK':
                                    print '主机', component_id, '定时任务开启成功'
                                else:
                                    print '主机', component_id, '定时任务开启失败，请检查相关配置项'
                                break
                        else:
                            print '解析XML遇错'
                except:
                    print '解析XML遇错'

    def stop_time_set(self):
        print '关闭定时任务： ',
        for timer_id in timer_list:
            tree = ET.parse('timer_set.xml')
            for commendid in tree.findall('body')[0].findall('timer'):
                if commendid.attrib['id'] != '':
                    commendid.set("id", timer_id)
                    commendid.set('parameter', '0')
                    commendid.set('operation', '0')
                else:
                    commendid.set("id", timer_id)
                tree.write('stop_timer_set.xml')
                stop_xml = open('stop_timer_set.xml', 'r')
                get_resopnse = self.postman(6060, stop_xml)
                try:
                    _tree = ET.fromstring(get_resopnse)
                    for hearder in _tree.findall('header'):
                        component_id = hearder.attrib.get('component-id')
                        for item in _tree.findall('body')[0].findall('result'):
                            if item.attrib.get('code') == '0':
                                if item.attrib.get('description') == 'OK':
                                    print '主机', component_id, '定时任务关闭成功'
                                else:
                                    print '主机', component_id, '定时任务关闭失败，请检查相关配置项'
                                break
                        else:
                            print '解析XML遇错'
                except:
                    print '解析XML遇错'

    def postman(self, port, message):
        conn = httplib.HTTPConnection('127.0.0.1', port, timeout=3)
        try:
            conn.connect()
        except Exception:
            print '试图链接127.0.0.1:%s出现异常' % port
            return 1
        else:
            conn.request('POST', '/', message)
            try:
                response = conn.getresponse().read()
            except:
                print '等待回复超时'
            else:
                return response
        finally:
            conn.close()
            # return response

    def trs_upload(self):
        cache_type = self.cache_type[self.input_type]
        channel = self.get_channel()
        if cache_type == 'record':
            try:
                system('killall {0}'.format(cache_type))
                nu = (popen('ps -ef|grep {0}|grep -v grep |wc -l'.format(cache_type)).read())
                if nu != 0:
                    print cache_type, '的进程没有完全停止，请手动处理'
                else:
                    print cache_type, '的进程已全部停止'
                    for channelname in channel:
                        remove('/{0}/{1}/{2}/{2}'.format(deploy_dir, channelname, cache_type))
                        system('cp /{0}/tmp/{2}/{2} /{0}/{1}/{2}'.format(deploy_dir, channelname, cache_type))
                        system('/{0}/{1}/{2}{2} -v  > /{0}/tmp/banben.txt'.format(deploy_dir, channelname, cache_type))
            except:
                print '命令执行错误'
        else:
            try:
                system('killall {0}'.format(cache_type))
                nu = (popen('ps -ef|grep {0}|grep -v grep |wc -l'.format(cache_type)).read())
                if nu != 0:
                    print cache_type, '的进程没有完全停止，请手动处理'
                else:
                    print cache_type, '的进程已全部停止'
                    for channelname in channel:
                        remove('/{0}/{1}/{2}/{2}'.format(deploy_dir, channelname, cache_type))
                        system('cp /{0}/tmp/{2}/{2} /{0}/{1}/{2}'.format(deploy_dir, channelname, cache_type))
                        system('/{0}/{1}/{2}/{2} -v  > /{0}/tmp/banben.txt'.format(deploy_dir, channelname, cache_type))
                        remove('/{0}/{1}/{2}/etc/{2}.conf'.format(deploy_dir, channelname, cache_type))
                        system('cp /{0}/tmp/{2}/etc/{2}.conf /{0}/{1}/{2}/etc'.format(deploy_dir, channelname, cache_type))
            except:
                print '命令执行错误'

    def control_center(self):
        while True:
            print ''
            input_type = raw_input('请输入升级哪个组件，record【0】XSpliter【1】XEliminator【2】')
            if input_type in ['0', '1', '2']:
                self.input_type = int(input_type)
                print '以CACHE类型为[%s]，开始检查\n' % self.cache_type[self.input_type]
                self.stop_time_set()
                self.trs_upload()
                self.start_time_set()
                break
            else:
                print '八戒，别闹！让你输入【1】【2】【3】。重来！！'

if __name__ == '__main__':
    app = Main_Upload()
    app.control_center()
    print '\n***********************************'
    print '* => 请手工在验证一下升级结果'
