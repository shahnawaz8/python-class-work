from matplotlib import pyplot as plt
x=[3,5,8,10,14]
y=[6,4,12,9,11]
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Simple Line')
plt.plot(x,y,'red',label='production')
plt.legend()
