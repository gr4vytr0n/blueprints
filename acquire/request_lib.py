'''
    using requests library to access a RESTful API
'''

import requests

def make_get_request(link):
    ''' send GET request to link '''
    return requests.get(link.encode('unicode_escape'))


for repo in make_get_request('https://api.github.com/users/gr4vytr0n/repos').json():
    print(repo['name'])
