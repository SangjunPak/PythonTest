from functools import reduce
import math

def check(num):
    a = range(1, math.ceil(math.sqrt(num)))
    f = list(filter(lambda x : num % x == 0, a))
    t = list(map(lambda x : int(num / x), f))
    asum = sum(f+t) 
    return "perfect" if asum == num*2 else "abundant" if asum > num*2 else "deficient"

for i in range(2,21):
    print("%d:%s" % (i,check(i)))

print(list(filter(lambda i : check(i) == 'perfect', range(1,10001))))


d = ["quite", "a", "good", "thing", "to", "do", "now", "is", "to", "play", "together"]
print(reduce(lambda x,y:x if len(x) > len(y) else y, d))

