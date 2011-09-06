#!/usr/bin/env python

def pyencode(s, codec):
    enc=s.encode(codec)
    if codec == "base64":
        enc=enc[:-1]
    elif codec == "zlib":
        enc=enc.encode('string_escape')
    return '"%s"'%enc

def pydecode(s, codec):
    return '%s.decode("%s")'%(s,codec)

def pyformat(s, format):
    if format == "print":
        return "'print %s'"%s
    elif format == "exec":
        return "exec %s"%s
    elif format == "cmd":
        return "python -c '%s'"%s
    else:
        return format%s

filters = {
"string": lambda x, y: y,
"pyencode": pyencode,
"pydecode": pydecode,
"pyformat": pyformat,
}


description = [
	["string", "Real men don't."],
	["pyencode", "base64"], #delete end with \n
	["pydecode", "base64"],
	["pyformat", "print"],
	["pyformat", "exec"],
	["pyencode", "zlib"], #make sure escaping is correct (r'' string)
	["pydecode", "zlib"],
	["pyformat", "exec"],
	["pyformat", "cmd"],
	["pyencode", "hex_codec"],
	["echone", None],
	["pypipedecode", "hex_codec"],
	["shexec", None],
]

def main():
    s=""
    for level in description:
        print level
        if filters.has_key(level[0]):
            s = filters[level[0]](s, level[1])
        print s

if __name__ == "__main__":
    main()
