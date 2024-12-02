
class contatto:
    
    def __init__ (self , nome , cognome , num_fisso  , num_mobile):
        
        self.nome = nome
        self.cognome = cognome
        self.num_fisso = num_fisso
        self.num_mobile = num_mobile
        
    def stampa_contatto (self):
        
        nome = self.nome
        cognome = self.cognome
        num_fisso = self.num_fisso
        num_mobile = self.num_mobile
        
        print ("informazioni contatto:\n")
        print ("nome: " , nome)
        print ("cognome: " , cognome)
        print ("numero fisso: " , num_fisso)
        print ("numero mobile: " , num_mobile)
        
    
    def ceck_len_num (self):
        
        num_fisso = self.num_fisso
        num_mobile = self.num_mobile
        
        if len (num_fisso) != 10:
            raise ValueError ("il numero fisso non ha 10 cifre")
        
        if len (num_mobile) != 10:
            raise ValueError ("il numero mobile non ha 10 cifre")
