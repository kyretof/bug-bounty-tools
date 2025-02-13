'''
    GOOGLE DORK

    1. Open Redirects

    site: example.com
'''

queries = {
    'open_redirects':'inurl:"next=" | inurl:"redirect=" | inurl:"url=" | inurl:"uri=" | inurl:"return=" -inurl:next- -inurl:redirect- -inurl:url- -inurl:uri- -inurl:return-'
}

print(queries["open_redirects"])
