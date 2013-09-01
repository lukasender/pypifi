#!/usr/bin/env python

from pypifi.message import Message

class MetaDataMessage(Message):
    def __init__(self, author, message):
        self.author = author
        self.message = message
