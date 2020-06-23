
class Airline:
    __numberFlight = 0
    __target = ""
    target = ""

    def __init__(self, n_flight, target, airplane, time, days=[]):
        self.week_days = []
        self.setNumberFlight(n_flight)
        self.setTarget(target)
        self.airplane = airplane
        self.set_week_days(days)
        self.time_flight = time

    def set_week_days(self, deys):
        if deys == 0:
            deys = input("Укажите номера дней недели (1 - понедельник,0 = ежедневно)").split(',')
        if deys [0] == 0:
            self.week_days = [1,2,3,4,5,6,7]
        else:
            for n in (deys):
                if 0 < int(n) < 8:
                    self.week_days.append(int(n))
                else:
                    print("Неверно указаны дни недели")
                    self.week_days = []
                    return

    def setTarget(self,tar):
        self.__target = tar
        self.target = tar

    def setNumberFlight(self,num):
        self.__numberFlight = num
        self.number_flight = num

    def getTarget(self):
        return self.__target
    def getNumberFlight(self):
        return self.__numberFlight

airs = []
air1 = Airline(1745,"Москва","ТУ-154",'10:20',[1,2,3,4,5,6,7])
air2 = Airline(2003,"Москва",'Boing-745','12:40',[1,3,5])
air3 = Airline(1313,"Урюпинск",'Djet-1','13:40',[2])
#air4 = Airline()
#air5 = Airline()

airs.append(air1)
airs.append(air2)
airs.append(air3)
#airs.append(air4)
#airs.append(air5)

listResult = []
for_tar = "Москва"

def forTarget(x):
    if x == for_tar:
        return 1
    else:
        return 0

for x in(airs):
    print(x.getTarget,x.airplane)
    if x.target == for_tar:
        listResult.append(x)

#listResult = list(filter(forTarget,x.target))
for air in (listResult):
    print(air.getNumberFlight, air.time_flight,air.week_days)

listResult = []
day = 2

def f(x):
    if x == day:
        return 1
    else:
        return 0

for x in(airs):
    print(x.getTarget,x.airplane)
    if len(list(filter(f, x.week_days)))>0:
        listResult.append(x)

for air in (listResult):
    print(air.getNumberFlight, air.time_flight,air.week_days)
