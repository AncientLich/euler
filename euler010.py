# il crivello di Eratostane serve per determinare i numeri primi.
# per prima cosa stabilisco un limite (per risolvere euler 10 stabilisco il limite a 2.000.000)
# primes contiene all'inizio tutti i numeri da 2 al limite (setaccio)
# al setaccio tolgo tutti i numeri multipli di 2 all'interno del limite fissato (il valore di iniziale di seeker è 2)
# il primo numero successivo non settacciato (3) sarà determinante a filtrare ulteriormente il setaccio 
#          (il valore di seeker sarà il primo valore del setaccio superiore al valore attuale di seeker)
# il successivo seeker (3) verrà usato per stabilire tutti i multipli entro il limite fissato
# tutto ciò fino a che il quadrato di seeker (seeker * seeker) non sia superiore al limite fissato. In tal caso non occorrerà più settacciare valori
# quando si è finito di settacciare, primes conterrà effettivamente solo i numeri primi

import math


limit=2000000
slim = math.sqrt(limit)

primes=set()
seeker=2



for a in range(2,limit):
    primes.add(a)


while (seeker < slim):
    mul = 2
    smul = seeker * mul
    while (smul < limit):
        try:
            primes.remove(smul)
        except KeyError:
            pass
        mul += 1
    for a in sorted(primes):
        if a > seeker:
            seeker = a
            break

# e ora si passa a calcolare la somma di tutti i numeri primi così ottenuti

result = 0

for a in primes:
    result = result + a
    
print(result)



# with open('./primes', 'w', encoding='utf-8') as fo:
#     for a in sorted(primes):
#         print(a, file=fo)

