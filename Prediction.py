import pickle
import sys
import pandas as pd
import numpy as np
import json

kmeans = pickle.load(open("Kmeans_model.sav", 'rb'))
with open('myFile.json') as f:
    dat = json.loads(f.read())

data = pd.DataFrame(dat)
print(data)
#f = open("output.txt", "w")
daa = data["val"]
val1 = daa[0]
val2 = daa[1]
val3 = daa[2]
val4 = daa[3]

output = kmeans.predict([[val1, val2, val3, val4]])
#f.write(output.tostring())
#f.close()
np.savetxt("output.txt", output, fmt = "%2.1f")
#print(type(output))
#print(output)
