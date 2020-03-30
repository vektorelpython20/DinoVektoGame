#Araba 


class Kedi:
    tur = "Felis" #class attribute
    def __init__(self,adi,yas):
        self.adi = adi
        self.yas = yas
    
    def Miyavla(self):
        print(self.adi," Miyavladi")


melek = Kedi("Melek",5)
tekir = Kedi("Tekir",3)
melek.Miyavla()
tekir.Miyavla()
melek.adi = "MELEEEEEK"
melek.Miyavla()