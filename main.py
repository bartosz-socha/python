from random import *
#import math as m
#print(m.sqrt(6))


class MyRandom:

    def __init__(self, s: int, f=None):
        if f is None:
            self.f = 0
            self.s = s
        else:
            self.f = f
            self.s = s

    def show(self):
        print(randint(self.f, self.s))


MyRandom(f=10, s=2000).show()


my_dict = {
    "Fruit_name": [(1, 3, [2, 3]), "banana", "mango"]
}
#mydict["Fruit_name"][0] = "rose"
print(my_dict["Fruit_name"][0][2][1])

my_list = [
    [1, 2, 3],
    [11, 22, 33],
    [111, 222, 333]
]
print(my_list[2][0])

# quick 2D list with zeros
my_list2 = [[0] * 5, ] * 5
print(my_list2[4][4])


# adding lists
def add_lists(a: list, b: list):
    res_list = []
    i = 0
    for a in a:
        res = a + b[i]
        res_list.append(res)
        i += 1
    return res_list


print(add_lists([1, 4, 9], [12, 3, 65]))


# taking N max values
def show_maxes(a: list, b: int):
    res_list = []
    for i in range(b):
        res_list.append(max(a))
        a.remove(max(a))
    return res_list


def show_maxes2(a: list, b: int):
    a.sort()
    #start = len(a) - b
    #stop = len(a)
    return a[-b:]


print(show_maxes([12, 3, 8, 2, 0, 34, 7], 4))
print(show_maxes2([12, 3, 8, 2, 0, 34, 7], 4))


class Human:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        print("Your name is " + self.name + " and your age is " + str(self.age))


class Man(Human):

    def show(self):
        super().show()
        print("You are also a manly man")


#Human("Kalosz", 23).show()
#Man("Miłosz", 34).show()







