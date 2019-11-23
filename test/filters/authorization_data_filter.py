#!/usr/bin/env python

from pypifi.filter import Filter

from hashlib import sha1

class AuthorizationDataFilter(Filter):

    def process(self, message):
        print("username: " + message.username)
        print("password: " + message.password)
        message.password = self.__encrypt(message.password.encode('utf-8'))
        print("password (sha1): " + message.password)

    def __encrypt(self, token):
        return sha1(token).hexdigest()
