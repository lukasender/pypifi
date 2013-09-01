#!/usr/bin/env python

from pypifi.message import Message

class UserDataMessage(Message):

    def __init__(self, username, password):
        self.username = username
        self.password = password
