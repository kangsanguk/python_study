from random import*
lst = sorted(sample(range(1,31), 6))
filter_lst = []
def filter():
    for i in lst:
        if i % 3 == 0:
            filter_lst.append(i)
    print("원 리스트:", lst)
    print("필터 리스트:", filter_lst)

filter()
