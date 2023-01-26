# Pickel Module: 
# Serializing(store) and di-Serializing(read)

# Pickel with dump():    ( Put_data with binary_formate )
import pickle
l = [10,20,30,40]
file = open('writedata.txt','wb')
pickle.dump(l,file)
file.close()

# Un-Pickel with Load():    (binary to read data)
import pickle
file = open('writedata.txt','rb')
l = pickle.load(file)
print(l)
