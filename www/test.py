#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 3:44 PM
# @Author  : zzr
# @Site    : 
# @File    : test.py
# @Software: PyCharm
#
import orm,asyncio,sys
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='www-data',password='www-data',db='awesome')

    u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')

    await u.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)