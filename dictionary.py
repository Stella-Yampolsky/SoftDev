'''
Stella Yampolsky
JST
SoftDev
K04 -- Write a Python program to randomly select a "Devo" from a list in a dictionary.
2024-09-13
time spent:
'''
import random
krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }
#takes a random period and then a random name using random choice
def wayA():
    #picks a random key from the dictionary
    pd = random.choice(list(krewes))
    #picks a random name from the list from the random key
    devo = random.choice(krewes[pd])
    return devo


#OR
#takes a random period and then a random name using randint and indexing
def wayB():
    #makes a list of the keys for random selection
    pds = list(krewes)
    #picks a random element from the list of keys
    pd = pds[random.randint(0, len(pds) - 1)]
    #returns a random element from the list from the random key
    return krewes[pd][random.randint(0, len(pds) - 1)]

print(wayA())
print(wayB())
