from machine import mem32
import uctypes
import array

P0 = array.array("l", [0,0])
P1 = array.array("l", [1,2])
P2 = array.array("l", S[3,3])
P3 = array.array("l", [4,0])
n = array.array("l", [4])
LR=[]

dir_P0 = uctypes.addressof(P0)
dir_P1 = uctypes.addressof(P1)
dir_P2 = uctypes.addressof(P2)
dir_P3 = uctypes.addressof(P3)
dir_n = uctypes.addressof(n)

def Bezier(dir_P0,dir_P1,dir_P2,dir_P3,dir_n):
    LR=[]
    LR_x=[]
    LR_y=[]
    t=0
    
    for i in range(0,4):
        t = i/mem32[dir_n]
        LR_x[i] = (((1-t)**3)*mem32[dir_P0])+(3*((1-t)**2)*t*mem32[dir_P1])+
        (3*(1-t)*(t**2)*mem32[dir_P2])+((t**3)*(mem32[dir_P3]))
        LR_y[i] = (((1-t)**3)*mem32[dir_P0+4])+(3*((1-t)**2)*t*mem32[dir_P1+4])+
        (3*(1-t)*(t**2)*mem32[dir_P2+4])+((t**3)*(mem32[dir_P3+4]))
        
    LR = LR_x + LR_y
    return LR

LR = Bezier(dir_P0,dir_P1,dir_P2,dir_P3,dir_n)

print("Lista retornada:")
for i in range(0,4):
    print("Punto P",i,": (",LR[i],",",LR[i+5],")")