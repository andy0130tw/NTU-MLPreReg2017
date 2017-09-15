import sys
from PIL import Image

if len(sys.argv) != 2:
    print('Usage: {} <image-file-path>'.format(sys.argv[0]))
    exit(1)

im = Image.open(sys.argv[1])
if im.mode not in ['RGB', 'RGBA']:
    exit(2)

w, h = im.size

mat = im.load()
for x in range(w):
    for y in range(h):
        r, g, b = mat[x, y]
        mat[x, y] = r // 2, g // 2, b // 2

im.save('Q2.jpg')

