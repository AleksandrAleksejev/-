#1
n = int(input("Введите число скворечников от 1 до 9: "))
for i in range(n):
   ckv= [" ----- ",
        "|  O  |",
        "!  -  !",
         " ----- "]
   if n>9:
       break
for i in ckv:
    print(i * n)
#2
#n = int(input("Введите число: "))
#b = int(input("Введите показатель чисел: "))
#for l in range(1,n+1):
#   print(l**b,end=" ")
#3

#4

#5
#n = int(input('Введите количество чисел Фиббоначи: '))
#e, k, l = 1, 1, 1
#while k != n :
#    k += 1
#    print(l, end = ' ')
#    l += e 
#    e, l = l, e
