... это пока все, на что хватило фантазии. И я не могу распечатать инкапсулированные
... поля. AttributeError: 'book' object has no attribute '__author'

class Author():
    page = []

    def __init__(self, f="", i=""):
        if f == '':
            f = input("Фамилия автора")
        self.lastname = f
        if i == '':
            i = input("имя")
        self.firstname = i
        self.middlename = input("отчество")

    def setPage(self, page):  # страница автора
        self.page.append(page)


class publishHouse():
    def __init__(self, c=0, n= ''):
        self.code = max(c,1)
        if n == '':
            n = input('Название издательства')
        self.name = n
        self.city = input("город")
        self.address = input("адрес")


class Person():
    def __init__(self, f="", i=""):
        if f == '':
            f = input("Фамилия")
        self.lastname = f
        if i == '':
            i = input("имя")
            self.middlename = input("отчество")
        self.firstname = i
        self.address = input("адрес")


class printEdition:
    __author = []
    publisher = []
    genre = []
    place = []
    def __init__(self, id=1):
        self.__id = id
        self.__name = input("Название издания:")
        self.setAuthor()
        self.__year = input("год издания:")
        self.pages = int(input("количество страниц:"))
        self.publisher = defPublisher()
        self.pathFolder = input("Путь к папке:")
        self.fileName = input("имя файла:")
        self.classification = input("Классификация:")

    def setAuthor(self):
        while 1:
            f = input("Фамилия автора")
            if f == '':
                break
            self.__author.append(Author(f))

    def setState(self, state):
        self.state = state

    def setPlace(self, state):
        self.state = state

    def setPerson(self, person):
        self.person = person(f,i)

    def delPerson(self):
        self.person = ''

class magazine(printEdition):
    def __init__(self, id = 1):
        self.__id = id
        self.__name = input("Название издания:")
        self.__year = input("год издания:")
        self.number = int(input("номер журнала:"))
        self.month = input('месяц издания')
        self.genre.append(input('?Типа направление'))

class book(printEdition):
    def __init__(self, id = 1):
        printEdition.__init__(self,id)
        self.annotation = input("Аннотация:")
        self.artist = input("Иллюстратор:")
        self.genre = list(input("Жанр / жанры:"))
        self.tag =  list(input("Ключевые слова:"))
        self.sequence = input("Серия:")
        self.number = input("номер в серии:")

class learnBook(printEdition):
    def __init__(self,id = 1):
        printEdition.__init__(self,id)
        self.genre.append(input("Наука:"))
        self.kurs = int(input("курс:"))
        self.number = int(input("редакция:"))

lib = {}
pub = {}

def defPublisher(code = 0):
    if code > 0:
        if pub.get(code) == None:
            code = 0
        else:
            return pub[code]
    print('Издательства:')
    for key,value in pub.items():
        print(key, value.name)
    code = int(input('Укажите издательство (0 -  новое)'))
    if code == 0:
        code = len(pub) + 1
        newPub = publishHouse(code)
        pub[code] = newPub
    return pub[code]
id = 1
while id >= 0:
    if input('Добавить новую книгу? (да / нет') == "нет":
        id = -1
    else:
        id = len(lib) + 1
        new = int(input("Добавляем: 1 - книга, 2 - учебник, 3 - журнал"))
        if new == 1:
            newPE = book(id)
        elif new == 2:
            newPE = learnBook(id)
        else:
            newPE = magazine(id)
        lib[id] = newPE
