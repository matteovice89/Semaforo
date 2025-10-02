from datetime import datetime #gestione orari
import time  
class semaforo():#classe che va a definire i semafori per iniziare nord sud est ovest
    def __init__(self, nome,verde,giallo,rosso,sensore):#colori sono true o false
        self.nome=nome
        self.verde=verde
        self.giallo=giallo
        self.rosso=rosso
        self.sensore=sensore
    
    def notturno(self):#semaforo in notturno(lampeg. giallo)
        blink = True
        print(f'Giallo {blink} ')
        time.sleep(3)
        blink = False
        print(f'Giallo {blink} ')
        blink = False
        
    def stato(self): #metodo gestisce cambio di stato delle luci
        pass

class strada():#classe per la gestione delle strade. in base a come voglio regolare il traffico
              #vado a gestire il semforo
    def __init__(self, nome, pedonale,scorre):#pedonale e scorre sono boolean
        self.nome=nome
        self.pedolale=pedonale
        self.scorre=scorre
    
semaforo_nord=semaforo('nord',False,False,False,False)
semaforo_sud=semaforo('sud',False,False,False,False)
semaforo_ovest=semaforo('ovest',False,False,False,False)
semaforo_est=semaforo('est',False,False,False,False)

