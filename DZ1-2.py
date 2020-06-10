nl = int(input("За сколько лет проводить расчет?"))
p = float(input("Введите процент амортизации"))
if 11 <= nl <= 19:
    tail = " лет "
elif nl % 10 == 1:
    tail = " год "
elif 2 <= nl % 10 <= 4:
    tail = " года "
else:
    tail = " лет "

end_year = 2020
begin_year = end_year - int(nl) + 1
S = [0]
n = 1
while begin_year <= end_year:
    s = input("Введите сумму закупки за год " + str(begin_year))
    S.append(float(s))
    for i in range(n): # если текущий год участвует в расчете амортизации, то n+1
        S[i] = S[i] / 100 * (100 - p)
    begin_year += 1
    n += 1
s = sum(S)
print ("За " + str(nl) + tail + "накоплено оборудования на сумму " + str(s) + " руб.")
s= int(s*100)      # так красивше
print ("За " + str(nl) + tail + "накоплено оборудования на сумму " + str(s/100) + " руб.")



