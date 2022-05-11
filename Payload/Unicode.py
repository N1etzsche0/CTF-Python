import json
from unicodedata import normalize

from urllib3.packages.six import unichr


def main():
    debug = False
    tables = {}
    for i in range(1, 0x10000):
        src = unichr(i)
        dst = normalize('NFKC', src)[0]
        try:
            if ord(dst) < 128 and dst != src:
                if debug:
                    print("%s (\\u%s) -- normalize --> %s (\\x%s)" % (
                        src, hex(i)[2:].rjust(4, '0'),
                        dst, hex(dst.charAt(0))[2:]
                    ))
                if dst in tables:
                    tables[dst].append(src)
                else:
                    tables[dst] = [src]
        except Exception as e:
            print(repr(e))
    with open("nfctable.txt", "wb") as fh:
        json.dump(tables, fh)


if __name__ == '__main__':
    main()