# -*- coding: utf-8 -*-
import Actividad23inc
from time import localtime

print "La hora local es %2d:%.2d" % (localtime().tm_hour, localtime().tm_min) #no es necesario el paquete 
c = 'N'
while c != 'S':
    Actividad23inc.printMenu() #obligatorio el nombre del paquete 
    c = raw_input("¿Opción?").upper() 
    if c!= 'S':
        op1 = raw_input("¿Primer operando?") 
        op2 = raw_input("¿Segundo operando?") 
        print Actividad23inc.calcula(c, op1, op2)
