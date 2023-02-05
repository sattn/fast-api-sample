import pickle
from mydata import MyData
 
data = MyData([1, 2, 3])
f = open("mydata.pkl", "wb")
pickle.dump(data, f)
f.close
