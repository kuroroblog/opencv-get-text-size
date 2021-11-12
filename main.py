import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('sample.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# 画像内へ印字する文字列
text = "Hello World"
# 画像内へ印字する文字列のフォントの種類
fontface = cv2.FONT_HERSHEY_SIMPLEX
# 画像内へ印字する文字列の大きさ。倍率指定。
fontscale = 2.0
# 画像内へ印字する文字列の太さ
thickness = 2
# 画像内へ印字する文字列を、画像のどの位置へ挿入するのか指定する。
x, y = 200, 200

# getTextSize : 画像内へ印字する文字列の、幅や高さ・ベースラインを取得できる関数

# 第一引数(必須) : 画像内へ印字する文字列
# 第二引数(必須) : 画像内へ印字する文字列の、フォントの種類を指定します。
# 第三引数(必須) : 画像内へ印字する文字列の大きさを、倍率指定する。float型。
# 第四引数(必須) : 画像内へ印字する文字列の太さを指定します。int型。

# 戻り値 ###############################
# w : 文字列の幅
# h : 文字列の高さ
# baseline : ベースライン
#####################################
(w, h), baseline = cv2.getTextSize(text, fontface, fontscale, thickness)

# 画像内へ文字列を印字する。
# puttext関数について : https://kuroro.blog/python/Omz54Dk1uR1d23yNow7e/
cv2.putText(img, text, (x, y), fontface, fontscale, (255, 255, 255), thickness)

# 画像内へ印字する文字列の周りへ、矩形を挿入する。
# rectangle関数について : https://kuroro.blog/python/ueVXVWPVfEmknnz6C8U1/
cv2.rectangle(img, (x, y), (x + w, y - h), (0, 0, 255), thickness)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)
