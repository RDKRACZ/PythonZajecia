import os

class Uczen:
	oceny_z_matematyki = []
	oceny_z_informatyki = []
	oceny_z_histori = []
	
	def __init__(self,imie,nazwisko):
		self.imie=imie
		self.nazwisko=nazwisko
	
	def srednia(self):
		suma=0
		for i in self.oceny_z_matematyki:
			suma+=i
		return suma/len(self.oceny_z_matematyki)

	def najwiekszaOcena(self):
		return max(self.oceny_z_matematyki)

	def iloscPiatek(self):
		liczbaPiatek=0
		for ocena in self.oceny_z_matematyki:
			if ocena==5:
				liczbaPiatek+=1
		return liczbaPiatek

	def informacje(self):
		print(self.imie+" "+self.nazwisko)
		print("Matematyka: "+str(self.oceny_z_matematyki)[1:-1]+",")
		print("Informatyka: "+str(self.oceny_z_informatyki)[1:-1]+",")
		print("Historia: "+str(self.oceny_z_histori)[1:-1]+",")


#deklaracje uczniów
os.system('cls')
print("Jak ma się nazywać Uczeń?")

uczen1=Uczen(input("Imie: "),input("Nazwisko: "))
uczen1.oceny_z_matematyki=[1,2,3,4,5]
uczen1.oceny_z_informatyki=[1,2,3,4,5]
uczen1.oceny_z_histori=[1,2,3,4,5]

while(True):
	os.system('cls')
	print("|i-informacje       |")
	print("|x-wyjscie          |")
	print("|p-ilosc piatek     |")
	print("|n-najwieksza ocena |")
	a = input("Twoje działanie: ")
	if a == 'i':
		uczen1.informacje()
	if a == 'x':
		break
	if a == 'p':
		print(uczen1.iloscPiatek())
	if a == 'n':
		print(uczen1.najwiekszaOcena())
	input()
	


