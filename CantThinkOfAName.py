import numpy as np
import matplotlib.pyplot as plt

#going to define a function for plotting, but for now will hard code
def pol2cart(rho, phi):
    x = rho * np.cos(np.deg2rad(phi))
    y = rho * np.sin(np.deg2rad(phi))
    return(x, y)


def plotLayer(numP,Pvector,PLabels,radius):
	#calculate the total and then partitions
	vSum=np.sum(Pvector)	
	angleBit=360.0/vSum

	#set the starting angle
	angle=0
	pad=radius*0.05
	for i in range(0,numP):
		x,y=pol2cart(radius-pad,angle)
		plt.plot([0,x],[0,y],'-k')
		x,y=pol2cart(radius,angle)
		if (angle>180.0):
			direction=90
		else:
			direction=-90
		plt.text(x,y,vectorLabels[i],horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'),rotation=angle+direction)	
		#plt.plot(x,y,'or')
		angle=angle+vector[i]*angleBit

#set number or partitions
numP=5
#set how many bits for each bit
vector=np.ones(numP).astype(int)
#randomly generate
for i in range(0,numP):
	print i
	vector[i]=np.random.randint(4)+1
vectorLabels=['cat','bat','mat','man','sauce']
#Set radius
radius=1

fig=plt.figure()

plotLayer(numP,vector,vectorLabels,radius)

plt.show()
