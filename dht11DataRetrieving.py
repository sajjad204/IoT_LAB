import pyrebase
import random
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn')



from datetime import datetime
# convert to date String
now = datetime.now()
date = now.strftime("%d-%m-%Y")

print('Date String:', date)

config = {
  "apiKey": "AIzaSyB-OdpfU1g1jZXj4Z1jAbl_JjM1JH7Xa0c",
  "authDomain": "python2firebase-c8466.firebaseapp.com",
  "databaseURL": "https://python2firebase-c8466-default-rtdb.firebaseio.com",
  "projectId": "python2firebase-c8466",
  "storageBucket": "python2firebase-c8466.appspot.com",
  "messagingSenderId": "818194656208",
  "appId": "1:818194656208:web:5d09d0100ac58a3eeb27d5",
  "measurementId": "G-YQGY9LCWF2"
}
i=0
a=[]
temp_array=[]
hum_array=[]
time_array=[]


firebase = pyrebase.initialize_app(config)
database = firebase.database()


### reading data of an array from firebase ###
temp = database.child("DHT_Nodemcu").child("temperature").child("11-11-2022").get()
hum = database.child("DHT_Nodemcu").child("humidity").child("11-11-2022").get()

##### Turning the firebase data into arrays #### 
i=0
j=0
k=0
var=0

for k in temp.val().keys():
    time_array.append(var)
    var+=1

for i in temp.val().values():
    temp_array.append(i)

for j in hum.val().values():
    hum_array.append(j)

'''
out_temp=[]
for i in range(len(time_array)//6):
    out_temp.append(sum(temp_array[6*i:6*i+6])//6)  

out_hum=[]
for i in range(len(time_array)//6):
    out_hum.append(sum(hum_array[6*i:6*i+6])//6)

out_time=time_array[:len(out_hum)]   '''



print("temperature array")
print()
print("hum array")
print()
print("time array")
print() 

fig, (ax1,ax2)=plt.subplots(nrows=2,ncols=1)
ax1.plot(time_array,hum_array)
ax1.set_title("HUMIDITY")
ax1.set_xlabel("Time in Min.")
ax1.set_ylabel("Humidity in %")


ax2.plot(time_array,temp_array,color='#444444' )
ax2.set_title("TEMPERATURE")
ax2.set_xlabel("Time in Min.")
ax2.set_ylabel("Temperature in °C")
plt.tight_layout();
plt .show() 
fig.savefig('pltfig.jpg')

frequencyDict = dict()
visited = set()
listLength = len(temp_array)
for i in range(listLength):
    if temp_array[i] in visited:
        continue
    else:
        count = 0
        element = temp_array[i]
        visited.add(temp_array[i])
        for j in range(listLength - i):
            if temp_array[j+i] == element:
                count += 1
        frequencyDict[element] = count

print("Input list is:", temp_array)
print("Frequency of elements is:")
print(frequencyDict)
temp_labels=[]
for j in frequencyDict.keys():
        temp_labels.append(j)


temp_labels=list(map(str,temp_labels))
temp_freq=[]
for j in frequencyDict.values():
        temp_freq.append(j)

print(temp_labels)
print(temp_freq)

plt.pie(temp_freq,labels=temp_labels,autopct='%1.1f%%')
plt.title(date+" Temperature Stats of the Day")
plt.tight_layout();
plt.show()

plt.bar(temp_labels,temp_freq)
plt.title(date+" Temperature Stats of the Day")
plt.tight_layout();
plt.show()