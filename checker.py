import sys
import io
import re

class Unmatch(Exception):
    """Exception for unmatch"""
    pass

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

    # run brute-force 2-D pattern matching
    computed = set()
    for i in range(m-1, n):
        for j in range(m-1, n):
            # try matching the pattern
            try:
                for x in range(0, m):
                    # global index for x
                    xg = i-m+1+x
                    for y in range(0, m):
                        # global index for y
                        yg = j-m+1+y
                        if t[xg][yg] != p[x][y]:
                            raise Unmatch
                computed = computed | set([(i,j)])
            except Unmatch:
                pass

    # check whether ans & computed are the same
    if ans == computed:
        return "yes"
    else:
        return "no"


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
    buf.close()
    answer.close()

    # write output files
    try:
        f = open(sys.argv[3], 'w')
        f.write(output)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        f.close()
