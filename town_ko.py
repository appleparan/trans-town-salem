#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import glob, os
from google.cloud import translate

def run_translate():
    # [START translate_quickstart]
    # Instantiates a client
    translate_client = translate.Client()
     # The target language
    target = 'ko'

    # gather xml file
    xml_list = []
    os.chdir('xml')
    file = 'Mod_Korean.xml'
    for file in glob.glob("*.xml"):
        print(file)
        if not os.path.isfile(file):
            print('File not exists')
        tree = ET.parse(file)
        root = tree.getroot()

        for entry in root:
            for child in entry:
                if child.tag == 'Text' and child.text != None:
                    translation = translate_client.translate(
                        child.text,
                        target_language=target)
                    child.text = translation['translatedText']

        tree.write(file, encoding="UTF-8")

    # # The text to translate
    # text = u'Hello, world!'
    # # Translates some text into Russian
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]


if __name__ == '__main__':
    run_translate()
