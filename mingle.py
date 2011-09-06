#!/usr/bin/env python

def pyencode(s, codec):
    return s

filters = {
"string": lambda x, y: y,
"pyencode": pyencode,
}


description = [
	["string", "Real men don't"],
	["pyencode", "base64"], #delete end with \n
	["pydecode", "base64"],
	["pyprint", None],
	["pyexec", None],
	["pyencode", "zlib"], #make sure escaping is correct (r'' string)
	["pydecode", "zlib"],
	["pyexec", None],
	["pycmd", None],
	["pyencode", "hex_codec"],
	["echone", None],
	["pypipedecode", "hex_codec"],
	["shexec", None],
]

def main():
    s=""
    for level in description:
        if filters.has_key(level[0]):
            s = filters[level[0]](s, level[1])
        print s

if __name__ == "__main__":
    main()
