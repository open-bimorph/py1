b = True

while b == True:
   a = int(input())

   if a == 0:
       b = False
       print('dziekuje, koniec!')
       break

   for i in range(1, a + 1):
       odpowiedz = ""

       if i % 2 == 0:
           odpowiedz += "parzysta"
       else:
           odpowiedz += "nieparzysta"

       if i % 3 == 0:
           odpowiedz += ", wielokrotnosc 3"

       if i % 5 == 0:
           odpowiedz += ", wielokrotnosc 5"

       print(f'{i}, {odpowiedz}')
