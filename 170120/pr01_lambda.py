sum = lambda x, y: x+y;

print("정수의 합 :", sum(10,20))
print("정수의 합 :", sum(20,20))

L = [ lambda x: x ** 2,
      lambda x: x ** 3,
      lambda x: x ** 4 ]

for f in L :
    print(f(3))

min = (lambda x,y: x if x < y else y )
print(min(100,200))

