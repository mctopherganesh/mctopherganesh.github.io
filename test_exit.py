from atexit import register

def easy_funk():
    print('hello cruel world')




test_decorator=register(easy_funk)


print('test string')
