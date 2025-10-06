from datetime import datetime  # gestione orari
import time


class semaforo:  # classe che va a definire i semafori per iniziare nord sud est ovest
    def __init__(self, nome, verde, giallo, rosso, sensore):  # colori sono true o false
        self.nome = nome
        self.verde = verde
        self.giallo = giallo
        self.rosso = rosso
        self.sensore = sensore

    def __str__(self):
        return f"SEMAFORO: {self.nome}, Verde: {self.verde}, Giallo: {self.verde}, Rosso: {self.rosso} "

    def notturno(self):  # semaforo in notturno(lampeg. giallo)
        for i in lista_semafori:
            i.giallo=True
        semaforo.stampa()
        time.sleep(3)
        for i in lista_semafori:
            i.giallo=False
        semaforo.stampa()
        time.sleep(3)   
        
    def diurno(self):  # semaforo in diurno
        pass

    def stampa(): #uso la lista dei semafori
        for i in lista_semafori:
            print(i)
        print('------------------------------------------------------------')


class strada:  # classe per la gestione delle strade. in base a come voglio regolare il traffico
    # vado a gestire il semforo
    def __init__(self, nome, pedonale, scorre):  # pedonale e scorre sono boolean
        self.nome = nome
        self.pedolale = pedonale
        self.scorre = scorre


semaforo_nord = semaforo("nord", False, False, False, False)
semaforo_sud = semaforo("sud", False, False, False, False)
semaforo_ovest = semaforo("ovest", False, False, False, False)
semaforo_est = semaforo("est", False, False, False, False)
lista_semafori=[semaforo_est,semaforo_ovest,semaforo_nord,semaforo_sud]#lita mi serve per stampare e gestire con un colpo unico lo stato

semaforo.stampa() #stampo lo stato in cui si trovano i semafori
for i in lista_semafori: #accendo tutte le luci in modo da verificarare i led
    i.verde=True
    i.Giallo=True
    i.rosso=True
semaforo.stampa() #stampo per la verifica

ora_notturno_inizio=22
orario_notturno_fine=5 #faccio il loop sulla diurno
ora_attuale=datetime.now()

while ora_attuale >= 5 or ora_attuale < 22:
