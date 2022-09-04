import numpy as np 
import matplotlib.pyplot as plt

#Datos 
#La malla la definimos para que dx=5 y dy=5
Lx=55
Ly=20
#Condiciones de frontera 
H49,H50,H51,H52,H53=30,30,30,30,30 #Arriba
H54,H55= 0,0 #Arriba
H56,H57,H58,H59,H60=25,25,25,25,25 #Arriba

#Discretizar
Nx=12
dx=Lx/(Nx-1)
x=np.linspace(0,Lx,Nx)

Ny=5
dy=Ly/(Ny-1)
y=np.linspace(0,Ly,Ny)

xmesh, ymesh=np.meshgrid(x,y,indexing='ij')
#plt.scatter(xmesh,ymesh)
#plt.show()

N=Nx*Ny
A=np.zeros((N,N))
b=np.zeros(N)


for i in range (Nx):
    for j in range(Ny):
        n=i+j*Nx
        #Esquina 1
        if i==0 and j==0:
            A [n] [n]=1/dx**2+1/dy**2
            A [n] [n+1]=-2/dx**2
            A [n] [n+2]=1/dx**2
            A [n] [n+Nx]=-2/dy**2
            A [n] [n+2*Nx]=1/dy**2
            b [n]=0
         #Esquina 2
        elif i==Nx-1 and j==0:
            A [n] [n]=1/dx**2+1/dy**2
            A [n] [n-1]=-2/dx**2
            A [n] [n-2]=1/dx**2
            A [n] [n+Nx]=-2/dy**2
            A [n] [n+2*Nx]=1/dy**2  
            b [n]=0
        #Esquina 3
        elif i==Nx-1 and j==Ny-1:
            A [n] [n]=1/dx**2+1/dy**2
            A [n] [n-1]=-2/dx**2
            A [n] [n-2]=1/dx**2
            A [n] [n-Nx]=-2/dy**2
            A [n] [n-2*Nx]=1/dy**2  
            b [n]=0
         #Esquina 4
        elif i==0 and j==Ny-1:
            A [n] [n]=1/dx**2+1/dy**2
            A [n] [n+1]=-2/dx**2
            A [n] [n+2]=1/dx**2
            A [n] [n-Nx]=-2/dy**2
            A [n] [n-2*Nx]=1/dy**2  
            b [n]=0
            
            
        #Lado 1
        elif 0<i<Nx-1 and j==0:
            A [n] [n] =1
            b [n]=H50
        #Lado 2
        elif i==Nx-1 and 0<j<Ny-1:
            A [n] [n] =1
            b [n]=24
        
        #Lado 3
        elif 0<i<Nx-1 and j==Ny-1:
            A [n] [n] =1
            b [n]=22
        #Lado 4
        elif i==0 and 0<j<Ny-1:
            A [n] [n] =1
            b [n]=27
        #nodos centrales
        else:
            A [n] [n]=-2/dx**2-2/dy**2
            A [n] [n+1]=1/dx**2
            A [n] [n-1]=1/dx**2
            A [n] [n+Nx]=1/dy**2
            A [n] [n-Nx]=1/dy**2
                        
H=np.dot(np.linalg.inv(A),b)
Hmesh=np.zeros((Ny,Nx))

for n in range (N):
    i=n%Nx
    j=n//Nx
    Hmesh[j][i]=H[n]
print(np.round(Hmesh,1))

plt.scatter(xmesh,ymesh)       
plt.show ()
                    









