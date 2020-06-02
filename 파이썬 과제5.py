my_tuple = ("Wonder Woman", ('a', 'b', 'c'), [2.0, -1.2, 0, 100])
print("1번 문제:",my_tuple)
print()

print("2번 문제:", my_tuple[0:2])
print()

print("3번 과제:", my_tuple[2][2:])
print()

print("4번 과제:", sorted(my_tuple[2]))
print()

my_list = ['토끼', '거북이', '다람쥐']
my_list.extend(['하마', '호랑이'])
print("5번 과제:", my_list)
print()

my_list2 = list(my_tuple)
my_list2.append(my_list)
my_list2[2] = sorted(my_list2[2])
my_tuple = tuple(my_list2)
print("6번 문제:", my_tuple)
print()

my_tuple[3].reverse()
my_tuple[3].remove('하마')
print("7번 문제:", my_tuple)
print()

my_tuple2 = (len(my_tuple),max(my_tuple[1]),sum(my_tuple[2]))
print('8번 문제:', my_tuple2)
print()

our_tuple = my_tuple + my_tuple2
print("9번 문제:", our_tuple)
