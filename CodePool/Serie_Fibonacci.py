# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# #Usando end no fim pra evitar o pulo de linha 
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b