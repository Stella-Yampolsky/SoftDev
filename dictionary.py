'''
Stella Yampolsky
Loonch
SoftDev
K04 -- Write a Python program to randomly select a "Devo" from a list in a dictionary.
2024-09-13
time spent:
'''
import random
krewes = {
           4: [
                'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVA'
                'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRI'
                'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ET'
                'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
                ],
           5: [
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT'
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONAT'
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STE'
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL>
              ]
         }
pds = krewes.keys()
pd = pds[random.randint(0, pds.length() - 1)]
devo = krewes[pd[random.randint(0, pd.length() - 1)]]
return devo         
