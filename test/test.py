#!/usr/bin/env python

from pypifi.pipeline import Pipeline

from filters.meta_data_filter import MetaDataFilter

from filters.user_data_filter import UserDataFilter
from filters.authorization_data_filter import AuthorizationDataFilter

from messages.meta_data_message import MetaDataMessage

from messages.user_data_message import UserDataMessage

def test1():
    print('--- starting test1:')
    pipe = Pipeline()
    pipe.connect(MetaDataFilter())
    pipe.execute(MetaDataMessage('lumannnn', 'a simple test message'))
    print('--- finished test1')

def test2():
    print('--- starting test2:')
    pipe = Pipeline()
    pipe.connect(UserDataFilter()).connect(AuthorizationDataFilter())
    pipe.execute(UserDataMessage('lumannnn', 'awesomely secure password'))
    print('--- finished test2')

test1()
test2()
