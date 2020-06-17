import base64


def square (width, height, xcode, i_begin=0, j_begin=0):
    print("Вписать квадрат в прямоугольник", width,'x',height)
    if height <= width:
        i_end = i_begin + height
        j_end = j_begin + height
        widht_1 = width - height
        height_1= height
        Sq.append(height)
    else:
        i_end = i_begin + width
        j_end = j_begin + width
        height_1 = height - width
        widht_1 = width
        Sq.append(width)
    xcode = hex(len(Sq))
    for j in range (j_begin, j_end):
      for i in range (i_begin, i_end):
            S_drow[j][i] = len(Sq)

    if height <= width:
        i_begin = i_end
    else:
        j_begin = j_end
    if width != height:
      square(widht_1, height_1, xcode, i_begin, j_begin)

w = int(input('Введите ширину прямоугольника'))
h = int(input('Введите высоту прямоугольника'))


Sq = []
i_begin = 0
j_begin = 0
xcode = hex(0)
S_drow = [[xcode for i in range(w)] for j in range(h)]
#for j in range(h):
#    for i in range(w):
#        S_drow[j][i] = hex(0)

square(w, h, xcode)
print ("В прямоугольнике", w,'x',h, 'построено', len(Sq), "квадратов со сторонами")
print (Sq)

for row in (S_drow):
       print((row))


#print (base64.b64encode(bytes(S_drow)))