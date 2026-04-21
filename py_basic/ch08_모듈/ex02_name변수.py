# if __name__ == "__main__" :의 의미

import mod1
print(mod1.add(5, 4))
print(mod1.__name__) #mod1

print(mod1.__doc__) # doc : 모듈의 문서화
print(mod1.__file__) # :\bong\git\fs\py_basic\ch08_모듈\mod1.py
print(mod1.__package__) # None
print('__cached__ : ' + mod1.__cached__)

print(mod1.__loader__)

print(mod1.__spec__)


