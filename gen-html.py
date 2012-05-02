#!/usr/bin/env python

import pystache, sys, os, codecs

"""
Static HTML templating system - the purpose is to implemnt "include" directive in static plain HTML
It process all files and replaces in-place all Mustache templates found.

"""

path = None

context = {
  "name": "Willy",
  "include": lambda fileName: 
  codecs.open(os.path.join(path, fileName.strip()), encoding='utf-8').read()
}


def main():
    global path 
    path = _get_path(sys.argv)
    #print path

    # for_each(*.tmpl) file in argv[1] (default = ./src)
    templates = _get_all_templates(path, '.tmpl')
    for tmpl in templates: 
        # pystache.render it to *.html
        _in = codecs.open(tmpl, encoding='utf-8')
        #TODO catch IOError in case of include target does not exist 
        
        html_file = tmpl[:-4] + 'html'
        print "  Writing: {0:27} -> {1}".format(tmpl, html_file)
 
        _out = codecs.open(html_file, encoding='utf-8', mode='w+')
        _out.write(pystache.render(_in.read(), context))
        
        _out.close()
        _in.close()



def _get_all_templates(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path): #TODO use yeld?
        fl = [ os.path.join(root, _file) for _file in files if _file.endswith(ext) ]
        file_list += fl
    #print file_list
    print "Collecting *%s files in %s - %s found." % (ext, path, len(file_list))
    return file_list

def _get_path(argv):
    if len(argv) > 1:
        path = argv[1]
    else:
        path = './src'
    return path


if __name__ == '__main__':
    main()
