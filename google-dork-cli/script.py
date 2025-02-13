'''
    GOOGLE DORK

    1. Open Redirects

    site: example.com
'''

queries = {
    'open_redirects': '(inurl:"redir=" OR inurl:"redirect=" OR inurl:"redirecturi=" OR inurl:"redirect_uri=" OR inurl:"redirecturl=" OR inurl:"return=" OR inurl:"returnurl=" OR inurl:"relaystate=" OR inurl:"forward=" OR inurl:"forwardurl=" OR inurl:"forward_url=" OR inurl:"url=" OR inurl:"uri=" OR inurl:"dest=" OR inurl:"destination=" OR inurl:"next=" OR inurl:"n=" OR inurl:"to=" OR inurl:"go=" OR inurl:"out=") -inurl:"n-" -inurl:"to-" -inurl:"go-" -inurl:"out-" -inurl:"uri-"
}

print(queries['open_redirects'])

