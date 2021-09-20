def plus(a, b):
      return int(a) + int(b)
def minus(a, b):
  return int(a) - int(b)
def times(a, b):
  return int(a) * int(b)
def division(a, b):
  return int(a)/int(b)
def reminder(a, b):
  return int(a)%int(b)
def negation(a):
  return -int(a)
def power(a, b):
  return int(a) ** int(b)

a = 3
b = "2"

print(plus(a, b))
print(minus(a, b))
print(times(a, b))
print(division(a, b))
print(reminder(a, b))
print(negation(a))
print(power(a, b))