import requests
import json
import sys
import os
#import MySQLdb

#db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                     user="root",         # your username
#                     passwd="password",  # your password
#                     db="rfaxx")        # name of the data base


def ocr_space_file(filename, overlay=False, api_key='3c37bc8dde88957', language='eng'):


    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isCreateSearchablePdf': 'true'
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):


    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


# Use examples:
file = ocr_space_file(filename=sys.argv[1], overlay='false', language='eng')

searchPDFURL = json.loads(file)
#print(searchPDFURL)
pdfURL = (searchPDFURL['SearchablePDFURL'])
print(pdfURL)
pdf = requests.get(pdfURL, allow_redirects=True)
print(pdf.content)
chunk_size  = 200
pdfFilePath = sys.argv[1]
pdfFileName = pdfFilePath[22:]
with open('/var/www/html/stash/' + pdfFileName + '.pdf', 'wb') as fd:
    for chunk in pdf.iter_content(chunk_size):
        fd.write(chunk)

#print (test_file.encode('utf-8'))
