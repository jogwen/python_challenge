#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/channel.zip"

if __name__ == "__main__":
    import re
    import StringIO
    import zipfile

    import utils

    zip_data = utils.wget(url)
    filelike = StringIO.StringIO(zip_data)

    #print zipfile.is_zipfile(filelike)
    zf = zipfile.ZipFile(filelike, 'r')
    readme_text = zf.open('readme.txt').read()
    start_filename_pattern = re.compile(r'start from (\d+)')
    start_filename = re.search(start_filename_pattern, readme_text).group(1)

    comments = ''
    this_filename = start_filename
    count = 0
    next_filename_pattern = re.compile(r'Next nothing is (\d+)')
    while count <= len(zf.namelist()):
        comments += zf.getinfo('%s.txt' % this_filename).comment
        text = zf.open("%s.txt" % this_filename).read()
        print "%d: %s.txt: %s" % (count, this_filename, text)
        mo = re.search(next_filename_pattern, text)
        if mo:
            next_filename = mo.group(1)
        else:
            break
        this_filename = next_filename
        count += 1

    print comments
