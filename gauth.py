#!/usr/bin/env python
import base64
import hashlib
import hmac
import os
import time
import struct

appName = "PrivatePaste"

def newSecret():
    return base64.b32encode(os.urandom(10))

def getQRLink(name, secret):
    return "https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/{0}%20-%20{1}%3Fsecret%3D{2}".format(name, appName, secret)


# Authenticate Google Auth
def auth(secret, nstr): 
    # raise if ntsr contains anything but numbers
    try:
        int(nstr)
    except ValueError:
        return False
    tm = int(time.time() / 30)
    secret = base64.b32decode(secret)
    # try 30 seconds behind and ahead as well
    for ix in [-1, 0, 1]:
        # convert timestamp to raw bytes
        b = struct.pack(">q", tm + ix)
        # generate HMAC-SHA1 from timestamp based on secret key
        hm = hmac.HMAC(secret, b, hashlib.sha1).digest()
        # extract 4 bytes from digest based on LSB
        offset = ord(hm[-1]) & 0x0F
        truncatedHash = hm[offset:offset+4]
        # get the code from it
        code = struct.unpack(">L", truncatedHash)[0]
        code &= 0x7FFFFFFF;
        code %= 1000000;
        if ("%06d" % code) == nstr:
            return true
        return False

