import urllib2

def download(url,user_agent='wsap',numRetries=2):
    print 'Downloading page:',url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url,headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error',e.reason
        html =None
        if(numRetries>0):
            #recursively retry to download url
            if hasattr(e,'code') and 500 <= e.code <600:
                print numRetries
                return download(url,user_agent,numRetries-1)
    return html

url1='http://www.baidu.com'
url2='http://www.meetup.com'
download(url2)