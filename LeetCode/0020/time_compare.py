import timeit

if __name__ == "__main__":
    print(timeit.timeit(stmt='1 in test_list', setup="test_list = [1,3,5,7,9,10,8,6,4,2]", number=1000000))
    print(timeit.timeit(stmt='1 in test_set', setup="test_set = {1,3,5,7,9,10,8,6,4,2}", number=1000000))
