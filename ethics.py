"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x = np.random.rand(200,1)
g = np.random.randint(0,2,200)
y = (x[:,0] + g*0.5 > 0.8).astype(int)

m = LogisticRegression().fit(np.c_[x,g],y)
p = m.predict(np.c_[x,g])

r0 = p[g==0].mean()
r1 = p[g==1].mean()

plt.bar(['G0','g1'],[r0,r1])
plt.show()

EXNO 5
from rdflib import Graph, Literal, Namespace, RDF, RDFS
g =Graph()
EX =Namespace("https://ex.org/")

g.add((EX.Jobapplicant , RDF.type, RDFS.Class))
g.add((EX.Eligiblecanditate, RDFS.subClassOf , EX.Jobapplication))
g.add((EX.hasexperience, RDF.type , RDF.Property))
g.add((EX.Gender, RDF.type , RDF.Property))

g.add((EX.Alice , RDF.type, EX.Jobapplicant))
g.add((EX.Alice , EX.hasexperience, Literal(5)))

g.add((EX.Bob, RDF.type, EX.Jobapplicant))
g.add((EX.Bob , EX.hasexperience, Literal(5)))

for s in g:
    print(s)

exno 4
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
col = ['sl','sw','pl','pw','species']
df = pd.read_csv(data, names=col)

x = df.drop('species', axis=1)
y =df['species']

X_train, X_test,y_train, y_test = train_test_split(x,y,test_size =0.2, random_state = 0)

m1 = Perceptron(fit_intercept = False).fit(X_train,y_train)
print(accuracy_score(y_test, m1.predict(X_test)))

m2 = Perceptron().fit(X_train,y_train)
print(accuracy_score(y_test, m2.predict(X_test)))


exno 3
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

x=2* np.random.rand(100,1)
y=4+ 3*x + np.random.randn(100,1)

m1= LinearRegression().fit(x,y)
m2= LinearRegression(fit_intercept=False).fit(x,y)

y1 = m1.predict(x)
y2 = m2.predict(x)

plt.scatter(x,y)
plt.plot(x,y1 , label="with bias")
plt.plot(x,y2,'--', label="withour bias")
plt.show()




ex no 2
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,21)
y = 2*x +1

print(x,y)

m,c = np.polyfit(x,y,1)

print(m,c)

y_pred= m*x + c
print(y_pred)

plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()
"""
