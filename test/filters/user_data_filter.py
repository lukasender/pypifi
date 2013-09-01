#!/usr/bin/env python

from pypifi.filter import Filter

class UserDataFilter(Filter):

    def process(self, message):
        """
            type(message) should be type of UserDataMessage
        """
        if message.username is None:
            print "error: no username provided"
        else:
            print "success: username provided"

        if message.password is None:
            print "error: no password provided"
        else:
            print "success: password provided"
