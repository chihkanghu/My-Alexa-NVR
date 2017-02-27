import httplib
import base64
import string
 
# host = "172.20.10.10"
# url = "/server"
# username = 'admin'
# password = '1111'
message = ''

class HttpClient():
    def __init__(self, username, password, host, url):    
        # base64 encode the username and password
        self.host = host
        self.username = username
        self.password = password
        self.url = url
        auth = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n', '')
        print self.host, self.url
        webservice = httplib.HTTP(self.host)
        # write your headers
        webservice.putrequest("GET", self.url)
        webservice.putheader("Host", self.host)
        webservice.putheader("User-Agent", "Python http auth")
        webservice.putheader("Content-type", "text/html; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(message))
        # write the Authorization header like: 'Basic base64encode(username + ':' + password)
        webservice.putheader("Authorization", "Basic %s" % auth)
         
        webservice.endheaders()
        webservice.send(message)
        # get the response
        statuscode, statusmessage, header = webservice.getreply()
        print "Response: ", statuscode, statusmessage
        # print "Headers: ", header
        res = webservice.getfile().read()
        # print 'Content: ', res
