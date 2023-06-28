"""
Level 36
by 43r04

Scrambled captcha

This captcha generation was scrambled slightly to much.

Each line in this captcha originally started with a grey pixel, e.g.: '|0123456789' was scrambled to '789|0123456'.
The pipe ('|') represents the grey dot, the numbers (0-9) represent the remaining pixels in each line.

Unscramble the word and you will get the result.

You have 10 seconds.
"""

from PIL import Image
im = Image.open("Untitled.png")
im = im.convert('RGB')
px = im.load()

marker = (40,40,40) # grey

def find_colidx(row):
	for idx in range(400):
		if px[idx,row] == marker:
			return idx
	return 0
	idx = 0

rotated = Image.new('RGB', (400,60))
rotpx   = rotated.load()

for z in range(60):
	offset = find_colidx(z)
	for j in range(400):
		rotpx[j,z] = px[(offset+j)%400,z]

rotated.show()
