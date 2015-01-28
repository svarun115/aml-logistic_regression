import csv
import numpy as np
import math

def sigmoid(x):
	return 1/(1+math.e**(-x))


with open("mod_cleve.txt","r") as f:
	l=f.readlines()

names=['Age', 'sex', 'chest_pain','blood_pressure','cholesteral','blood_sugar','ecg','heart_rate','eia','oldpeak','slope',
  'num_color','thal']

data=[]
for i in l:
	line=i[:-1].split()
	data.append(line)

y=[]
x=[]
data=data[:-1]

for i in data:
	temp=[]
	y.append(i[-2])
	temp.extend(list(map(eval,["1",i[0],i[3],i[4],i[7],i[9],i[11]])))
	x.append(temp)
	
for i in range(len(y)):
	if y[i]=="buff":
		y[i]=1
	else:
		y[i]=0


x_train=x[:240]
y_train=y[:240]
x_test=x[241:]
y_test=y[241:]

y_train=[y_train]


w=np.zeros(7)
x_train=np.array(x_train)
y_train=np.array(y_train)
y_train=y_train.transpose()

############################################## IMPLEMENTIING LOGISTIC REGRESSION ################################################

w=[w.tolist()]
w=np.array(w)
alpha=0.01

#print w.shape
#print x_train.shape

for i in x_train:
	i=[i]
	i=np.array(i)
	print i
	print i.shape
	print w
	print w.shape
	#print i.transpose().shape
	term = i* np.transpose(w)
	print term
	break

