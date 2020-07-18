
#p = float(0.41)
#q = float(0.59)
#za2 = float(1.96)
#e = float(0.03)

#num1 = p * q
#num2 = za2 / e
#num3 = num2 * num2
#result = num1 * num3

#print(result)


#def margin(10, 20, 30, 40, 50):

import math

a = int(10)
b = int(20)
c = int(30)
d = int(40)
e = int(50)
data = [a, b, c, d, e]

n = len(data)
stand_dev = float(11.18)
sqr_n = math.sqrt(n)
value1 = stand_dev / sqr_n
z = int(1.96)
result = int(value1 * z)

print(sqr_n)
