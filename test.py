import example

import main
import timeit



cy = timeit.timeit('example.test(100)',setup='import example')
py = timeit.timeit('main.test_py(100)',setup='import main')
print(f'time:{cy} ---- {example.test(100)}')
print(f'time:{py} ---- {main.test_py(100)}')

print(f'cython is {py/cy}x faster than py')