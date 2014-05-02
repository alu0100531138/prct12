#! /usr/bin/python

def aproximacion (n):
  sum=0
  if (n>0):
   for i in range (1,n+1):
     a= float(i-1)/n
     b=float (i)/n
     xi=float (i-0.5)/n
     fxi=float (4.0/(1.0 + xi*xi))
     sum+=fxi
  Pi= float (sum/n)
  print("El valor de pi aproximado es:",Pi)
  return Pi
  

if __name__=="__main__":
  l=[ ]
  import sys
  if (len(sys.argv))==1:
    m= int (raw_input ("Dame el numero de aproximaciones que desea "))
    n= int (raw_input ("Dame el numero de subintervalos para aproximar pi "))
  
  if (len(sys.argv))==3:
    m = int (sys.argv[1])
    n= int (sys.argv[2])
  if (len (sys.argv))==2:
    print ("Falta un valor tomaremos un valor por defecto")
    m=6
    n=4
    
  for i in range (1,m+1):
    print aproximacion (n*i)
    Pi=aproximacion (n*i)
    l=l+[Pi]
    print l