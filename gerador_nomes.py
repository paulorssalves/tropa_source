#!/usr/bin/python
import random

famosos = {
0: ('Orlando Bloom', 'M'),
1: ('Ludwig van Beethoven', 'M'),
2: ('Jason Statham', 'M'),
3: ('Katy Perry', 'F'),
4: ('Brienne de Tarth', 'F'),
5: ('Bráulio Bessa', 'M')
}

def nomes_de_pau():
    n = random.randint(0,5)
    name = famosos[n]
    string = "Meu pau parece com "
    if name[1] == "F":
        string += "a {}".format(name[0])
    else:
        string += "o {}".format(name[0]) 
        
    return string

print(nomes_de_pau())
