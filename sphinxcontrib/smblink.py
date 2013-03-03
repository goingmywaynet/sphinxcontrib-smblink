# smblink role for Sphinx.

from docutils import nodes
import re
import string

def convertToWSLStyle(text):
    text = text.decode('utf-8').encode('utf-8')
    text = text.split('`')[1]
    if '<' in text and '>' in text:
        name, path = text.split('<')
        path = path.split('>')[0]
        name = re.sub(r' $','', name)     # remove space before "<"
    else:
        name = text
        path = name
    path = re.sub('\\\\', r'/', path)     # "\"  to "/"
    path = re.sub(r'\\', r'//', path, 1)  # "\\" to "//"
    path = re.sub(r' ', r'%20', path)     # " "  to "%20"
    return "<a href=\"file:" + path + "\">"+ name +"</a>"

def smblink_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Role to create link addresses.
    """
    href = convertToWSLStyle(rawtext)
    node = nodes.raw('', href, format='html')
    return [node], []

def setup(app):
    app.add_role('smblink', smblink_role)

