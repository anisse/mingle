#!/usr/bin/env python

from mingle import mingle

message1 = [
        ["string", "Mingle boggles your mind."],
        ["pyencode", "base64"],
        ["pyformat", '"%s"'],

        ["pydecode", '"base64"'],

        ["pyformat", "print"],
        ["pyformat", "'%s'"],
        ["pyformat", "exec"],

        ["pyencode", "zlib"],
        ["repr", None],
        ["pydecode", '"zlib"'],

        ["pyformat", "exec"],

        ["escape", '"'],
        ["shell_clean", None],
        ["pyformat", '"%s"'],
        ["pyformat", "cmd"],

        ["pyencode", "hex_codec"],
        ["pyformat", "echone"],
        ["pypipedecode", "'hex_codec'"],
        ["pyformat", "shexec"],
        ["pyencode", "hex_codec"],
        ]
# Same as message1, but with base64 instead of repr (much shorter output)
message2 = [
        ["string", "Mingle is quite useless, too."],
        ["pyencode", "base64"],
        ["pyformat", '"%s"'],

        ["pydecode", '"base64"'],

        ["pyformat", "print"],
        ["pyformat", "'%s'"],
        ["pyformat", "exec"],

        ["pyencode", "zlib"],
        ["pyencode", "base64"],
        ["pyformat", '"%s"'],
        ["pydecode", '"base64"'],
        ["pydecode", '"zlib"'],

        ["pyformat", "exec"],

        ["escape", '"'],
        ["shell_clean", None],
        ["pyformat", '"%s"'],
        ["pyformat", "cmd"],

        ["pyencode", "hex_codec"],
        ["pyformat", "echone"],
        ["pypipedecode", "'hex_codec'"],
        ["pyformat", "shexec"],
        ["pyencode", "hex_codec"],
        ]

# Show a message and open a webpage
web = [
        ["string", "https://github.com/anisse/mingle"],
        ["pyencode", "base64"],
        ["repr", None],
        ["pydecode", '"base64"'],
        ["pyformat", "webopen"],

        ["pyformat", 'print "What have I done ?";%s'],
        ["repr", None],
        ["pyformat", "exec"],

        ["pyencode", "zlib"],

        ["pyencode", "base64"],
        ["pyformat", '"%s"'],
        ["pydecode", '"base64"'],

        ["pydecode", '"zlib"'],

        ["pyformat", "exec"],

        ["escape", '"'],
        ["shell_clean", None],
        ["pyformat", '"%s"'],
        ["pyformat", "cmd"],
        #["pyformat", "histdisable"], #for bash debug only

        ["pyencode", "base64"],
        ["pyformat", "echone"],
        ["pypipedecode", "'base64'"],
        ["pyformat", "shexec"],
        ["pyencode", "hex_codec"],
        ]

def main():
    print mingle(web, True)

if __name__ == "__main__":
    main()
