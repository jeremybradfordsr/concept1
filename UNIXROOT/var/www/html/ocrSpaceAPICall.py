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
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

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
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

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
print(searchPDFURL)
pdfURL = (searchPDFURL['SearchablePDFURL'])
print(pdfURL)
pdf = requests.get(pdfURL, allow_redirects=True)
print(pdf.content)
chunk_size  = 200
with open('/var/www/html/stash/' + sys.argv[1] + '.pdf', 'wb') as fd:
    for chunk in pdf.iter_content(chunk_size):
        fd.write(chunk)

#print (test_file.encode('utf-8'))
