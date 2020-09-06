import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

data=pd.read_csv("path to CSV")


plt.scatter(data["V1"], data["V2"])

km = KMeans(n_clusters=3)

y_pred = km.fit_predict(data[['V1','V2']])

data['cluster'] = y_pred

data1 = data[data.cluster == 0]
data2 = data[data.cluster == 1]
data3 = data[data.cluster == 2]

plt.scatter(data1.V1, data1['V2'], color='green')
plt.scatter(data2.V1, data2['V2'], color='red')
plt.scatter(data3.V1, data3['V2'], color='black')

plt.xlabel('V1')
plt.ylabel('V2')

possible_k = range(1,10)
sum_of_squares = []
for k in possible_k:
    km = KMeans(n_clusters=k)
    km.fit(data[['V1','V2']])
    sum_of_squares.append(km.inertia_)


plt.plot(possible_k, sum_of_squares)

