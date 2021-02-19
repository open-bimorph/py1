b = True

while b == True:
   a = int(input())
   if a == 0:
       b = False
       print ('dziekuje, koniec!')
       break

   for i in range (a):
       odpowiedz = ""
       if (i+1) % 2 == 0:
           odpowiedz += "parzysta"
       else:
           odpowiedz += "nieparzysta"
       if (i+1) % 3 == 0:
           odpowiedz += ", wielokrotnosc 3"
       if (i + 1) % 5 == 0:
           odpowiedz += ", wielokrotnosc 5"
       print(f'{i + 1}, {odpowiedz}')
