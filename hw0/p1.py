import sys

if len(sys.argv) != 2:
    print('Usage: {} <text-file-path>'.format(sys.argv[0]))
    exit(1)

with open(sys.argv[1]) as f:
    words = f.read().strip().split(' ')
    bank = {}
    out = []
    cnt = 0
    for w in words:
        idx = bank.get(w, None)
        if idx is None:
            out.append([w, 0])
            bank[w] = cnt
            idx = cnt
            cnt += 1
        out[idx][1] += 1
    with open('Q1.txt', 'w') as of:
        of.write('\n'.join([ '{} {} {}'.format(x[0], i, x[1]) for i, x in enumerate(out) ]))
