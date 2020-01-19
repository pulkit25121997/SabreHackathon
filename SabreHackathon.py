import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv('sabre.csv', encoding = 'utf-8', index_col = ["PNR"])
#print(data.head())
from sklearn import preprocessing

#std_scale = preprocessing.StandardScaler().fit(data[['Introvert', 'Extrovert', 'Sleepy']])
#data_STD = std_scale.transform(data[['Introvert', 'Extrovert', 'Sleepy']])

#minmax_scale = preprocessing.MinMaxScaler().fit(df[['Introvert', 'Extrovert', 'Sleepy']])
#df_minmax = minmax_scale.transform(df[['Introvert', 'Extrovert', 'Sleepy']])


from sklearn.cluster import KMeans


model = KMeans(4)
model.fit(data)
cluster_labels = model.predict(data)
centroids = model.cluster_centers_


kmeans = pd.DataFrame(cluster_labels)
data.insert((data.shape[1]), 'kmeans', kmeans)


saved_model = pickle.dumps(model)
#print(data)

'''

fig = plt.figure()
ax = fig.add_subplot(111)
scatter =  ax.scatter(data['Introvert'], data['Extrovert'], c = kmeans[0], s = 50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('Introvert')
ax.set_ylabel('Extrovert')
plt.colorbar(scatter)
plt.show()

'''


print(model.predict([[5, 1, 2, 1]]))