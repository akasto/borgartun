import urllib
import json
import hmac
import hashlib
import base64
import urllib2
import re

class Base(object):
    def __init__(self, url, apiKey, secret):
        self.url = url
        self.apiKey = apiKey
        self.secret = secret

    def sign_string(self, s, key):
        return urllib.quote(base64.b64encode(
            hmac.new(str(key),
            msg=s,
            digestmod=hashlib.sha1).digest()))

    def call(self, command, args):
        params = ''
        args['command'] = command
        args['apikey'] = self.apiKey
        args['response'] = 'json'
        for key, value in sorted(args.iteritems()):
            if key != "signature":
                params += "%s=%s&" % (key, urllib.quote(value))

        _sign = ''
        if params:
            _sign += ('%s' % params.rstrip("&"))

        signature = urllib.unquote(self.sign_string(_sign.lower(), self.secret))
        params += 'signature=%s' % (urllib.quote_plus(signature))
        url = self.url + '?' + params
        response = urllib2.urlopen(url)
        decoded = json.loads(response.read())
        return decoded
