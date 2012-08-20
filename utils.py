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
    >>> update_url('http://example.com/root/filename.ext?getparam1=abc', return_this, 'newfilename.xxx')
    'http://example.com/root/newfilename.xxx'
    """
    scheme, netloc, path, params, query, fragment = urlparse.urlparse(url)
    path_head, path_tail = os.path.split(path)
    filename, ext = os.path.splitext(path_tail)

    url_root = "%s://%s%s/" % (scheme, netloc, path_head)
    new_filename = func(filename, *args, **kwargs)
    if new_filename.find('.') >= 0:
        return url_root + new_filename
    else:
        return url_root + new_filename + ext

def return_this(irrelevant_orig_filename, new_filename):
    """
    Simplest function for func param to update_url.
    Use when you didn't need the old filename to calculate the new one.
    """
    return new_filename


def wget(url):
    domain, path, x, query = urlparse.urlparse(url)[1:5]
    path = '%s?%s' %(path, query)
    connection = httplib.HTTPConnection(domain)
    connection.request('GET', path)
    response = connection.getresponse()
    if response.status != 200:
        raise Exception, "Unable to wget"
    return response.read()


def plot(pix, x, y, colour):
    pix[x, y-1] = pix[x-1, y] = pix[x, y] = pix[x+1, y] = pix[x, y+1] = colour

def plot_points(pix, sequence, colour=(255,0,0)):
    while len(sequence) > 0:
        x = sequence.pop(0)
        y = sequence.pop(0)
        plot(pix, x, y, colour)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

