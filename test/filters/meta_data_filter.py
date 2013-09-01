#!/usr/bin/env python

from pypifi.filter import Filter

class MetaDataFilter(Filter):

    def process(self, message):
        """
            message should be type of MetaDataMessage.
        """
        super(MetaDataFilter, self).process(message)
        print message.author
        print message.message
