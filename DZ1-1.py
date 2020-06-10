k = int(input("Введите целое положительное число: "))
if 11 <= k <= 19:
    tail = " грибов"
elif k % 10 == 1:
    tail = " гриб"
elif 2 <= k % 10 <= 4:
    tail = " гриба"
else:
    tail = " грибов"
print ("Мы нашли в лесу " + str(k) + tail)
