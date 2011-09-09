#!/usr/bin/env python

from mingle import mingle
import pickle


recursion = [
        ["string", None],
        ["escape", '"'],
        ["pyformat", 'r="""%s"""'],
        ["pyformat", "import pickle,urllib2,os;%s;i=pickle.loads(r);i[0][1]=r;exec urllib2.urlopen('https://raw.github.com/anisse/mingle/master/mingle.py').read();print 'Please wait...';os.execlp('sh','sh','-c',mingle(i).decode('hex'))"],
        ["pyencode", "zlib"],
        ["pyencode", "base64"],

        ["pyformat", "'%s'"],
        ["pydecode", "'base64'"],

        ["pydecode", "'zlib'"],

        ["pyformat", "exec"],

        ["pyformat", '"%s"'],
        ["pyformat", "cmd"],
        ["pyencode", "hex"],
        ]

def minglerecursion():
    rserialized = pickle.dumps(recursion)
    recursion[0][1] = rserialized
    mingle(recursion, True)

minglerecursion()
