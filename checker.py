import sys
import io
import re

from bb import BB

def check(buf, answer):
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

    # process the answer
    ans = set()
    for l in answer.readlines():
        pair = re.match(r'(\d+)\s+(\d+)', l)
        i = int(pair.group(1))
        j = int(pair.group(2))
        ans = ans | set([(i, j)])

    # run Baker-Bird
    bb = BB(p)
    computed = set()
    for p in bb.search(t):
        computed = computed | set([p])

    buf.close()
    answer.close()

    if ans == computed:
        return "yes\n"
    else:
        return "no\n"
    
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : python checker.py <input> <answer> <output>")
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

    # read answer file
    answer = None
    try:
        f = open(sys.argv[2], 'r')
        answer = io.StringIO(f.read())
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        f.close()

    # check the answer
    output = check(buf, answer)

    # write output files
    try:
        f = open(sys.argv[3], 'w')
        f.write(output)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        f.close()
