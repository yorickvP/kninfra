from __future__ import with_statement

import random

ALPHA = 'qwertyuiopasdfghjklzxcvbnm'
NUM = '1234567890'
ALPHANUMUL = ALPHA + ALPHA.upper() + NUM

def read_ssv_file(filename):
        """ Reads values seperated by spaces in a simple one line file """
        with open(filename) as f:
                return f.readline()[:-1].split(' ')

def sesc(t):
	return t.replace('\\','\\\\').replace(' ','\\ ')

def pseudo_randstr(l=12, cs=ALPHANUMUL):
	ret = ''
	for i in xrange(l):
		ret += cs[random.randint(0, len(cs)-1)]
	return ret

DOMAIN = 'karpenoktem.nl'
LISTDOMAIN = 'lists.karpenoktem.nl'

EMAIL_ALLOWED = frozenset(
		    map(lambda x: chr(ord('a') + x), xrange(26)) +
		    map(lambda x: chr(ord('A') + x), xrange(26)) +
		    map(lambda x: chr(ord('0') + x), xrange(10)) +
		    ['.', '-'])

GALLERY_PATH = '/var/galleries/kn/'
MEMBERS_HOME = '/home/kn/'
MEMBER_PHOTO_DIR = 'fotos/'
MEMBERS_ALBUM = 'per-lid'
