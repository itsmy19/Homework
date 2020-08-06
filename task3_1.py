import timeit

code_to_test = """
tmp = []
tmp.append(True)
print(tmp[0])
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

code_to_test = """
tmp = {}
tmp[0] = True
print(tmp[0])
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


