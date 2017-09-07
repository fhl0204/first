#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from os import path, popen, listdir, access, R_OK, X_OK, makedirs


def get_process_stopTime(uid, p_name, time_space):
    print 'start time: ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    while popen('ps -eo user,pid,etime,comm | grep -i {0} | grep -i {1}'.format(uid, p_name)).read().strip():
        time.sleep(int(time_space))
        continue
    print 'end time: ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#print get_process_stopTime('zqinwen', 'cp', 1)