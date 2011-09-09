#!/usr/bin/env python

def pyencode(s, codec):
    enc=s.encode(codec)
    if codec == "base64":
        enc = "".join(enc[:-1].split()) #delete end with \n and put on one line
    return "%s"%enc

def pydecode(s, codec):
    return '%s.decode(%s)'%(s,codec)

def pypipedecode(s, codec):
    return '%s | python -c "import sys; print sys.stdin.read().decode(%s)"'%(s, codec)

def pyformat(s, format):
    formats = {
            "print": "print %s",
            "exec": "exec %s",
            "cmd": "python -c %s",
            "histdisable": "set +H\n%s\nset -H", # Disable history expansion, because it's FUCKING UN-ESCAPABLE !
            "echone": "echo -ne %s",
            "shexec": 'sh -c "$(%s)"',
            "webopen": 'import webbrowser; webbrowser.open(%s)',
            }
    if format in formats:
        return formats[format]%s
    else:
        return format%s

def python_sanitize(s, _unused):
    return s.encode('string_escape')

def shell_sanitize(s, _unused):
    return s.replace('\\\\', '\\\\\\')#.replace('$', r'\$')

def escape(s, delim):
    """ Finds delim and escape it if it's not already escaped """
    i=0
    while i < len(s):
        if s[i] == delim:
            #search backwards for '\' and count them
            count=0
            for j in range(i-1, -1, -1):
                if s[j] == '\\':
                    count += 1
                else:
                    break
            if (count % 2) == 0: #escape if there's a pair number of '\' before
                s = s[:i] + '\\' + s[i:]
                i += 1
        i += 1
    return s


filters = {
"string": lambda x, y: y,
"pyencode": pyencode,
"pydecode": pydecode,
"pyformat": pyformat,
"pypipedecode": pypipedecode,
"escape": escape,
"repr": lambda x, y: repr(x), # we can use string_escape encoding for almost the same purpose (see python_sanitize filter)
"shell_clean": shell_sanitize,
}



def mingle(steps, debug=False):
    s=""
    for level in steps:
        if debug: print level
        if filters.has_key(level[0]):
            s = filters[level[0]](s, level[1])
        if debug: print "%s\n%s"%(s, len(s))
    print s

