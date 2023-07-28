# Python exemples of program to print list

a = [1, 2, 3, 4, 5]

#usando for
for element in a :
    print(element)

#imprimindo a lista com os colchetes [1, 2, 3, 4, 5]
print(a)

# printing the list using * operator separated
# by comma
print(*a)

# printing the list using * and sep operator
print(*a, sep = ", ")

# print in new line
print(*a, sep = "\n")

# print the list by using list comprehension 
[print(i, end=' ') for i in a] #Com separador

[print(i) for i in a] #Sem separador

#l = [1,2,3,4,5,6]
#method 1
print(a[:])
 
#method 2
print(a[0:])
 
#method 3
print(a[0:len(a)])





