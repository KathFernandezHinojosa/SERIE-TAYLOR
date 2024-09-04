from math import *
from sympy import *
from scipy.misc import derivative
from sympy.parsing.sympy_parser import parse_expr

print("\n               SERIE DE TAYLOR-FUNCION: EXP(X)\n")
print("----------------------------------------------------------------")
print("Digite los puntos a los cuales desea se aproxime la funcion: ")

def PolTaylor(X0=float(input("X0: ")),X1=float(input("X1: "))):
    x=symbols('x')
    f=parse_expr(input("Ingrese la función:"))
    h=X1-X0
    print("----------------------------------------------------------------")
    print("X0: "+str(X0)+" >>> f(X0): f("+str(X0)+")")
    print("X1: "+str(X1)+" >>> f(X1): f("+str(X1)+")")
    print("¿Desea iterar hasta que Rn<=tol (Opcion: 1) o ingresar cantidad (Opcion: 2)?:")
    opcion=int(input("Opcion:"))    
    if opcion==1:
        print("Elija una función(1,2,3):\n1.f(x)=exp(x)\n2.f(x)=cos(x)\n3.f(x)=sin(x)")
        opcion2=int(input("Opcion:"))
        if opcion2==1:
            fX0=exp(X0)
            fX1=exp(X1)
            print("X(0)="+str(X0)+">>> f(X0)= "+str(fX0))
            print("X(1)="+str(X1)+">>> f(X0)= "+str((fX1)))
            print("\n---------------------- TABLA ----------------------")
            print("[#| X0 | X1 | f(X0)(derivadas) | h=X1-X0 | f(X1) | Rn | Rn<=tol]")
            print("-----------------------------------------------------") 
            n=0
            i=0
            tol=0.0005
            Rn=abs((fX0/factorial(n+1))*(h**(n+1)))
            faux=fX0
            while Rn>=tol:           
                if n==0:
                    fX1=fX0
                    Rn=abs(fX0/factorial(n+1)*(h**(n+1)))
                    mi_tabla=[i,X0,X1,fX0,h,fX1,Rn,Rn<=tol]
                    print(mi_tabla)
                    n=n+1
                    i=i+1
                else:
                    fX1=faux+(fX0/factorial(n))*(h**n)
                    esp="+"
                    Rn=abs((fX0/factorial(n+1))*(h**(n+1)))
                    mi_tabla=[i,X0,X1,fX0,h,fX1,Rn,Rn<=tol]
                    print(mi_tabla)
                    faux=fX1
                    n=n+1
                    i=i+1
        elif opcion2==2:
            print("2")
        else:
            print("3")
    elif opcion==2:
        niteraciones=int(input("\n¿Cuantas iteraciones?:"))
        print("\n---------------------- TABLA ----------------------")
        print("[#| X0 | X1 | f(X0)(derivadas) | h=X1-X0 | f(X1) | Rn ]")
        print("-----------------------------------------------------")
        n=0
        i=0
        faux=str(f)
        while n<=niteraciones:           
            if n==0:
                f1=f
                Rn=str(abs((diff(f,x,n+1)/factorial(n+1)*(h**(n+1)))))
                mi_tabla=[i,X0,X1,f,h,f1,Rn]
                print(mi_tabla)
                n=n+1
                i=i+1
            else:
                f0=diff(f,x,n)
                f1=str(((diff(f,x,n))/factorial(n))*(h**n))
                esp="+"
                Rn=str(abs((diff(f,x,n+1)/factorial(n+1)*(h**(n+1)))))
                mi_tabla=[i,X0,X1,f0,h,faux+esp+f1,Rn]
                print(mi_tabla)
                faux=str(f1)
                n=n+1
                i=i+1
    else:
        print("error")
    

PolTaylor()





