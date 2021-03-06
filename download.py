#!/usr/bin/env python3
import os
import os.path
import requests

def download(url):

    # Download the given url and saves it to the current directory.
    
    req = requests.get(url)
    # Check for non existing files.
    if req.status_code == 404:
        print('No such file found at %s' % url)
        return
    filename = url.split('/')[-1]
    with open(filename, 'wb') as fobj:
        fobj.write(req.content)                                 # Write the contents from the upstream to a file
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL:')                         
    download(url)

