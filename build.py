#!/usr/bin/env python

"""
 This script automates buld and deploy phase of static HTML site develoopment.

 1. clear i.e from ~, #, etc (find . -iname "*~" | xargs rm)

 2. verify, minify,  merge css
 3. jslint, minify,  merge js
 4. generate static HTML from .tmpl templates (mimic Server Side Includes)

 5. deploy i.e ftp upload or appcfg.py update

"""

def clean():
    pass

def build():
    pass

def deploy():
    pass


def main():
    clean()
    build()
    deploy()


if __name__ == '__main__':
    main()
