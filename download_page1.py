import urllib2

def download(url):
    print 'Download page:',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
    return  html

url1 = 'http://www.baidu.com'
download(url1)