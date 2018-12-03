#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 4:19 PM
# @Author  : zzr
# @Site    : 
# @File    : app.py
# @Software: PyCharm
import asyncio
import threading
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()