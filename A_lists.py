my_list1 = []
my_list2 = list()
my_list4 = [9] * 4
my_list5 = [a+3 for a in my_list4]

print(my_list1)
print(my_list2)

my_list3 = ["again", "bloody", "girls"]
my_list3.append("some")
my_list3.insert(-4, "soon")
my_list1.extend(my_list3)
my_list1 = my_list3.copy()
my_list3.pop(4)
my_list3.remove("bloody")
my_list3.reverse()
my_list2 = my_list1 + my_list3

print(my_list3[0:4:2])
print(my_list3[0:2])
print(my_list3[0])
print(my_list3[-1])
print(len(my_list3))

for item in my_list3:
    print(item, end=":")
print("\n")
for item in my_list1:
    print(item, end=":")
print("\n")
for item in my_list2:
    print(item, end=":")

print("\n" + str(my_list4))
print("\n" + str(my_list5))

if "soon" in my_list3:
    print("\nJUHU")
