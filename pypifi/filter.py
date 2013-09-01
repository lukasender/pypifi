#!/usr/bin/env python

class Filter(object):
    """
        Base filter class which can take a message and alter the message appropriately.
        You define what happens with the message.
    """

    def __init__(self):
        print "Filter created."

    def process(self, message):
        print "Filter.process()"
