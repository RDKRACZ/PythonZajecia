zmienna_int = 124 #zmienna całkowita
zmienna_float = 123.0 #zmienna zmiennoprzecinkowa

#print( float(zmienna_int) ) #castowanie
#print(zmienna_float)
#
#print("----wyniki----")
#
#print(int(zmienna_int/2))
#print(int(zmienna_float/2))

zmienna_str = '100' #zmienna tekstowa
zmienna_str2 = "tekst2"

#print(zmienna_str+str(zmienna_int))
#print(int(zmienna_str)+zmienna_int)

kolekcja_int = [123, 300, 400, 500]
kolekcja_str = ['123','300','400','12dsafas']

#print(int(kolekcja_str[0])+int(kolekcja_str[1]))
#print(kolekcja_int[0]+kolekcja_int[1])

slownik = {'pierwszy':'123', 'drugi':'300','trzeci':200}

slownik_zaawansowany = {'aaa':111, 'kolekcja':[10,20,30,40,50], 'slownik':{'ttt':123,'vvv':300}}

#print(slownik['pierwszy'])
#print(slownik_zaawansowany['slownik']['ttt'])

#a=20
#b=20
#c=30
#
#if a==b or a==c and b==c:
#    print("aaaa")
#else:
#    print('fałsz')

#a=1
#while a<=10:
#    print(a)
#    a+=1

#a=input('Wpisz swoje imię: ')   #wprowadzanie danych
#b=input('Wpisz jakąś liczbę: ')
#print('Witaj '+a)
#print('Twoja Liczba to: ' + b)
#print('Twoja liczba dodana do 10 to: ' +str(int(b) + 10))
#print(type(b))#

while True:
    print('Jestem w Programie')
    a=input()
    if a == 'x':
        break
    elif a== 't':
        continue
    print('dzieki za wprowadzenie danych z klawiatury')

print('Jestem poza programem')




+   #
-   #
*   #
/   #
%   #dzielenie modulo (reszta z dzielenia)
**  #potegowanie