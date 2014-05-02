#! /usr/bin/python
import timeit
from math import *
import sys
import modulo
    
def error (n,m, umbral):
    s=0
    for i in range(m):   
      apr1 = modulo.aproximacion(n)
      apr2 =modulo.aproximacion(n)
      if abs(modulo.aproximacion(n))-(modulo.aproximacion(n))> umbral:
        s+=1
    porcentaje=float((float(s)/float(n))*100)
    return porcentaje
   
def eficiencia(apr1,apr2):
  if eficencia(apr1)>eficiencia(apr2):
  div=eficiencia(apr1)/eficiencia(apr2)
  eficencia=(1-div)*100
  print'La aproximacion  dos es mejor'
  
  if eficencia(apr1)<eficiencia(apr2):
  div=eficiencia(apr1)/tiempo(apr2)
  eficencia=(1-div)*100
   print'La aproximacion uno es mejor'
 if __name__ =='__main__':
  import sys
  if (len(sys.argv))==4:
    n=int(sys.argv[1])
    m=int(sys.arg[2])
    umbral=float(sys.arg[3])
    print 'El porcentaje de fallos es %f' % (error(n,m,umbral)) 
  if (len(sys.argv))<4:
    n=int(raw_input('introduzca n'))
    m=int(raw_input('introduzca m'))
    umbral=float(raw_input('introduzca el valor del umbral')
    print 'El porcentaje de fallos es %f' % (error(n,m,umbral))
  