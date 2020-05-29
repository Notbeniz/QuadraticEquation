#!/usr/bin/python3
form math import*
a=int(input("Enter Your  Number A -->  :"))
b=int(input("Enter Your  Number B -->  :"))
c=int(input("Enter Your  Number C -->  :"))
#********************************************
print("********************************************")
print("             ∆=0 Moadele Yek javab darad")
print("             ∆>0 Moadele 2  javab darad")
print("             ∆<0 Moadele javab nadarad")
print("                   Formuls∆=(b^2-4ac)")
print("                  Formuls X=(-b±√∆)/2a")
print("********************************************")
delta=b*b-4*a*c
print("Delta =",delta)

#********************************************

if delta==0:
    x=(-b+sqrt(delta))/(2*a)
    print("Moadele Yek javab darad.")
    print("X=",x)

#*******************************************   

elif delta<0:
        print("Moadele javab nadarad!")

#*******************************************        
else:

        print("Moadele 2  javab darad")
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b+-math.sqrt(delta))/(2*a) 
        print("X1=",x1)
        print("X2=",x2)

#*******************************************       

#End
        
