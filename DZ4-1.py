import os
# Исходный файл - test1.txt
filename = input("Введите имя исходного файла: ")
if not os.path.exists(filename):
    print("Указанный файл не существует")
else:
    filename1 = input("Введите имя результирующего файла: ")
    file1 = open(filename)
    file2 = open(filename1, "w")
    print("Исходный файл -", filename, "длиной", os.path.getsize(filename))
    n_line= 0
    n_word = 0
    n_letter = 0
    for line in file1:
        n_line += 1
        if n_line%2 == 0:
            file2.write(line,)
            for l in line:
                if "аоеиуыэюяё".find(l) > 0:
                    n_letter += 1
                if l == ' ':
                    n_word += 1
            if l != " ":
                n_word += 1
    file1.close()
    file2.close()
    print("Результирующий файл -", filename1, "длиной", os.path.getsize(filename1))
    print("скопировано", n_line//2, "строк. Слов в результате", n_word, "гласных букв", n_letter)
