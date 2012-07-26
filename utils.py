#!/usr/bin/env python

import httplib
import os.path
import urlparse

def update_url(url, func, *args, **kwargs):
    """
    >>> def testmap(instring): return instring.replace('e', 'x')
    >>> update_url('http://example.com/root/filename.ext', testmap)
    'http://example.com/root/filxnamx.ext'
    >>> update_url('http://example.com/root/filename.ext', return_this, 'newfilename')
    'http://example.com/root/newfilename.ext'
    """
    path = urlparse.urlparse(url)[2]
    filename, ext = os.path.splitext(os.path.split(path)[1])
    return url[:-len(filename)-len(ext)] + func(filename, *args, **kwargs) + ext

def return_this(irrelevant_orig_filename, new_filename):
    """
    Simplest function for func param to update_url.
    Use when you didn't need the old filename to calculate the new one.
    """
    return new_filename


def wget(url):
    """
    """
    domain, path = urlparse.urlparse(url)[1:3]
    connection = httplib.HTTPConnection(domain)
    connection.request('GET', path)
    response = connection.getresponse()
    if response.status != 200:
        raise Exception, "Unable to wget"
    return response.read()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

