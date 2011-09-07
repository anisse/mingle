#!/usr/bin/env python

def pyencode(s, codec):
    enc=s.encode(codec)
    if codec == "base64":
        enc = "".join(enc[:-1].split()) #delete end with \n and put on one line
    return "%s"%enc

# TODO: Allow chosing of quote type: 'codec' or "codec"
def pydecode(s, codec):
    return '%s.decode("%s")'%(s,codec)

def pypipedecode(s, codec):
    return '%s | python -c "import sys; print sys.stdin.read().decode(\'%s\')"'%(s, codec)

def pyformat(s, format):
    if format == "print":
        return "print %s"%s
    elif format == "exec":
        return "exec %s"%s
    elif format == "cmd":
        return "python -c %s"%s
    elif format == "histdisable":
        return "set +H\n%s\nset -H"%s # Disable history expansion, because it's FUCKING UN-ESCAPABLE !
    elif format == "echone":
        return "echo -ne %s"%s
    elif format == "shexec":
        return 'sh -c "$(%s)"'%s
    elif format == "webopen":
        return 'import webbrowser; webbrowser.open(%s)'%s
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


description1 = [
    ["string", "https://github.com/anisse/mingle"],
	["pyencode", "base64"],
    ["repr", None],
	["pydecode", "base64"],
	["pyformat", "webopen"],

	["pyformat", 'print "What have I done ?";%s'],
    ["repr", None],
	["pyformat", "exec"],

	["pyencode", "zlib"],
    ["repr", None],
	["pydecode", "zlib"],

	["pyformat", "exec"],

    ["escape", '"'],
    ["shell_clean", None],
    ["pyformat", '"%s"'],
	["pyformat", "cmd"],
#	["pyformat", "histdisable"], #for bash debug only

	["pyencode", "base64"],
	["pyformat", "echone"],
	["pypipedecode", "base64"],
	["pyformat", "shexec"],
    ["pyencode", "hex_codec"],
]
description2 = [
	["string", "Real men don't."],
	["pyencode", "base64"],
    ["pyformat", '"%s"'],

	["pydecode", "base64"],

	["pyformat", "print"],
    ["pyformat", "'%s'"],
	["pyformat", "exec"],

	["pyencode", "zlib"],
    ["repr", None],
	["pydecode", "zlib"],

	["pyformat", "exec"],

    ["escape", '"'],
    ["shell_clean", None],
    ["pyformat", '"%s"'],
	["pyformat", "cmd"],

	["pyencode", "hex_codec"],
	["pyformat", "echone"],
	["pypipedecode", "hex_codec"],
	["pyformat", "shexec"],
	["pyencode", "hex_codec"],
]
# Same as description2, but with base64 instead of repr (much shorter output)
description3 = [
	["string", "Real men don't."],
	["pyencode", "base64"],
    ["pyformat", '"%s"'],

	["pydecode", "base64"],

	["pyformat", "print"],
    ["pyformat", "'%s'"],
	["pyformat", "exec"],

	["pyencode", "zlib"],
	["pyencode", "base64"],
    ["pyformat", '"%s"'],
	["pydecode", "base64"],
	["pydecode", "zlib"],

	["pyformat", "exec"],

    ["escape", '"'],
    ["shell_clean", None],
    ["pyformat", '"%s"'],
	["pyformat", "cmd"],

	["pyencode", "hex_codec"],
	["pyformat", "echone"],
	["pypipedecode", "hex_codec"],
	["pyformat", "shexec"],
	["pyencode", "hex_codec"],
]
# Same as description1, but with base64 instead of repr (much shorter output)
description = [
    ["string", "https://github.com/anisse/mingle"],
	["pyencode", "base64"],
    ["repr", None],
	["pydecode", "base64"],
	["pyformat", "webopen"],

	["pyformat", 'print "What have I done ?";%s'],
    ["repr", None],
	["pyformat", "exec"],

	["pyencode", "zlib"],

	["pyencode", "base64"], #replaced repr with base64 elements, more economic
    ["pyformat", '"%s"'],
	["pydecode", "base64"],

	["pydecode", "zlib"],

	["pyformat", "exec"],

    ["escape", '"'],
    ["shell_clean", None],
    ["pyformat", '"%s"'],
	["pyformat", "cmd"],
#	["pyformat", "histdisable"], #for bash debug only

	["pyencode", "base64"],
	["pyformat", "echone"],
	["pypipedecode", "base64"],
	["pyformat", "shexec"],
    ["pyencode", "hex_codec"],
]

def mingle(steps, debug=False):
    s=""
    for level in steps:
        if debug: print level
        if filters.has_key(level[0]):
            s = filters[level[0]](s, level[1])
        if debug: print "%s\n%s"%(s, len(s))
    print s

def main():
    mingle(description)

if __name__ == "__main__":
    main()
