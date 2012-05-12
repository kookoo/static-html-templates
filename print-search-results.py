#!/usr/bin/env python

import sys, os, codecs, re


"""
Print google-style search snippet for each page in the given dir
"""

def main():
    path = _get_path(sys.argv)
    base_url = _get_url(sys.argv)
    htmls = _get_all_files(path, '.html')

    for html in htmls: 
        _in = codecs.open(html, encoding='utf-8')
        page =_in.read()
        title_search = re.search('<title>(.*)</title>', page, re.IGNORECASE)
        if title_search:
            title = title_search.group(1)
            dsc_search = re.search('<meta name="description" content="(.*)"', page, re.IGNORECASE)
            print u' Title:{0:7} {1:.60}'.format('', title) + (u'...' if len(title) >= 60 else u'')
            print u' {0:13} {1}'.format('', '/'.join((base_url, '/'.join(html.split('/')[-2:]))))
            if dsc_search:
                dsc = dsc_search.group(1)
                print u' Description:{0:1} {1:.150}'.format('', dsc) + (u'...' if len(dsc) >= 150 else u'')            
                print '\n'

        _in.close()



def _get_all_files(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path): #TODO use yeld?
        fl = [ os.path.join(root, _file) for _file in files if _file.endswith(ext) ]
        file_list += fl
    print "Collecting *%s files in %s - %s found.\n" % (ext, path, len(file_list))
    return file_list

def _get_url(argv):
    """ Takes second command-line argumant as a site URL or usses .
    """
    if len(argv) > 2:
        url = argv[2]
    else:
        url = "www.your-site.com"
    return url
    

def _get_path(argv):
    """ Takes first command-line argumant as a path or usses current directory
        as a default one.
    """
    if len(argv) > 1:
        path = argv[1]
    else:
        path = '.'
    return path


if __name__ == '__main__':
    main()
