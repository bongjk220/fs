import mod2, mod1
from other import mod3

print(mod2.PI) # 3.141592
a = mod2.Math()
print(a.solv(2)) # 12.566368
print(mod2.add(mod2.PI,4.4)) # 7.5415920000000005

print(mod1.add(3,4))
print(mod1.sub(5,4))

print(mod3.add(3,4))
print(mod3.mul(5,4))