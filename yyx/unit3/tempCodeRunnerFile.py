x = 1.0
N = eval(input())
n = N/1000
dayup = pow(x+n, 365)
daydown = pow(x-n, 365)
a = int(dayup/daydown)
print("{:.2f},{:.2f},{:}".format(dayup, daydown, a))
