#!/usr/bin/env python

def pyencode(s, codec):
    enc=s.encode(codec)
    if codec == "base64":
        enc=enc[:-1] #delete end with \n
    elif codec == "zlib":
        #make sure escaping is correct (raw string)
        enc=enc.encode('string_escape')
    return '"%s"'%enc

def pydecode(s, codec):
    return '%s.decode("%s")'%(s,codec)

def pypipedecode(s, codec):
    return '%s | python -c "import sys; print sys.stdin.read().decode(\'%s\')"'%(s, codec)

def pyformat(s, format):
    if format == "print":
        return "'print %s'"%s
    elif format == "exec":
        return "exec %s"%s
    elif format == "cmd":
        return "python -c '%s'"%s
    elif format == "echone":
        return "echo -ne %s"%s
    elif format == "shexec":
        return 'sh -c "$(%s)"'%s
    else:
        return format%s

filters = {
"string": lambda x, y: y,
"pyencode": pyencode,
"pydecode": pydecode,
"pyformat": pyformat,
"pypipedecode": pypipedecode
}


description = [
	["string", "Real men don't."],
	["pyencode", "base64"],
	["pydecode", "base64"],
	["pyformat", "print"],
	["pyformat", "exec"],
	["pyencode", "zlib"],
	["pydecode", "zlib"],
	["pyformat", "exec"],
	["pyformat", "cmd"],
	["pyencode", "hex_codec"],
	["pyformat", "echone"],
	["pypipedecode", "hex_codec"],
	["pyformat", "shexec"],
    ["pyencode", "hex_codec"],
]

def main():
    s=""
    for level in description:
        if filters.has_key(level[0]):
            s = filters[level[0]](s, level[1])
    print s

if __name__ == "__main__":
    main()
