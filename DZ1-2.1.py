import random
print ("Формируем список учеников")
print ("Для окончания - Enter ")
Spisok = dict()
name = ""
pol = 'м'
while 1:
    name = input("Введите фамилию ")
    if name == '':
        break
    pol = input("и пол (по умолчанию - м) ")
    if pol == '':
        pol = 'м'
    Spisok [name] = [pol, random.randint(15,18),random.randint(40,120), random.randint(140,210)]
for key in Spisok:
    print(key, " - ", Spisok[key])

n_boys = 0          # количество мальчиков
n_girls = 0         #       девочек
age_boys = 0        # средний возраст мальчиков
age_girls = 0       #       девочек
tall_boy = ''       # самый высокийыыы
heavy_boy = ''     # самый тяжелый
little_girl = ""    # самая маленькая (считаем по росту)
young_gerl = 20      # низший возраст

for key, value in Spisok.items():
    if value[0] == 'м':
        if tall_boy == '':
            tall_boy = key
            heavy_boy = key
        n_boys += 1
        age_boys += value[1]
        if value[2] > Spisok[heavy_boy][2]:
            heavy_boy = key
        if value[3] > Spisok[tall_boy][3]:
            tall_boy = key
    else:
        if little_girl == '':
            little_girl = key
        n_girls += 1
        age_girls += value[1]
        if value[3] < Spisok[little_girl][3]:
            little_girl = key
        if value[1] < young_gerl:
            young_gerl = value[1]

print ("Мальчиков в классе - " + str(n_boys) + ". Средний возраст - " + str(age_boys//n_boys))
if tall_boy == heavy_boy:
    print ("Самый высокий мальчик весит больше всех в классе")
    print(tall_boy, " - рост", Spisok[tall_boy][3], ", вес", Spisok[tall_boy][2])
else:
    print ("Самый высокий мальчик ", tall_boy, " - рост", Spisok[tall_boy][3])
    print ("Весит больше всех в классе ", heavy_boy, "вес", Spisok[heavy_boy][2])

print ("\nДевочек в классе - " + str(n_girls) + " Средний возраст - " + str(age_girls//n_girls))
print("Самая маленькая девочка", little_girl, 'возраст', Spisok[little_girl][1],  " - рост", Spisok[little_girl][3])
if Spisok[little_girl][1] == young_gerl:
    print("Она самая юная в классе")
else:
    print("Она не самая юная в классе. Самой юной девочке ", young_gerl)
