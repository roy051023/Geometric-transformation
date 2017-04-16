import numpy as np
from PIL import Image
#讀檔案
im = Image.open('test.png')
#四邊的像素
locationOldX = [123, 255, 155, 288]
locationOldY = [42, 30, 344, 364]
#找最大最小
W = max(locationOldX) - min(locationOldX)
H = max(locationOldY) - min(locationOldY)
output = Image.new("RGB", (W, H))
locationNew = [(0, 0), (W, 0), (0, H), (W, H)]
#矩陣
value = np.mat([[locationNew[0][0], locationNew[0][1], locationNew[0][0] * locationNew[0][1], 1], [locationNew[1][0], locationNew[1][1], locationNew[1][0] * locationNew[1][1], 1], [locationNew[2][0], locationNew[2][1], locationNew[2][0] * locationNew[2][1], 1], [locationNew[3][0], locationNew[3][1], locationNew[3][0] * locationNew[3][1], 1]])
#value * coefX = oldX
oldX = np.mat([[locationOldX[0]], [locationOldX[1]], [locationOldX[2]], [locationOldX[3]]])
coefX = value.I * oldX
#value * coefY = oldY
oldY = np.mat([[locationOldY[0]], [locationOldY[1]], [locationOldY[2]], [locationOldY[3]]])
coefY = value.I * oldY
#帶回公式放入新圖 x'=ax+by+cxy+d
for i in range(0, W):
	for j in range(0, H):
		x = i * coefX[0, 0] + j * coefX[1, 0] + i * j * coefX[2, 0] + coefX[3, 0]
		y = i * coefY[0, 0] + j * coefY[1, 0] + i * j * coefY[2, 0] + coefY[3, 0]
		diffX = x - int(x)
		diffY = y - int(y)
		R = im.getpixel((int(x), int(y)))[0] * (1 - diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y)))[0] * (1 - diffY) * (diffX) + im.getpixel((int(x), int(y) + 1))[0] * (diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y) + 1))[0] * (diffY) * (diffX)
		G = im.getpixel((int(x), int(y)))[1] * (1 - diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y)))[1] * (1 - diffY) * (diffX) + im.getpixel((int(x), int(y) + 1))[1] * (diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y) + 1))[1] * (diffY) * (diffX)
		B = im.getpixel((int(x), int(y)))[2] * (1 - diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y)))[2] * (1 - diffY) * (diffX) + im.getpixel((int(x), int(y) + 1))[2] * (diffY) * (1 - diffX) + im.getpixel((int(x) + 1, int(y) + 1))[2] * (diffY) * (diffX)
		output.putpixel((i,j),(int(R), int(G), int(B)))
#輸出圖片
output.save("output.jpg")

#np.linalg.det(A1)