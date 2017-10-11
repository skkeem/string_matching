import sys
import io
import re

from bb import BB

def main(buf):
    # process the input
    match = re.match(r'(\d+)\s+(\d+)', buf.readline())
    m = int(match.group(1))
    n = int(match.group(2))

    p = []
    t = []
    for i in range(m):
        p.append(buf.readline().strip())
    for i in range(n):
        t.append(buf.readline().strip())

    # run Baker-Bird
    bb = BB(p)
    output = io.StringIO()
    for i, j in bb.search(t):
        output.write("{} {}\n".format(i, j))

    ret = output.getvalue()

    buf.close()
    output.close()
    return ret
    
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python run.py <input> <output>")
        exit(1)

    # read input file
    buf = None
    try:
        f = open(sys.argv[1], 'r')
        buf = io.StringIO(f.read())
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        f.close()

    output = main(buf)

    # write output files
    try:
        f = open(sys.argv[2], 'w')
        f.write(output)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        f.close()
