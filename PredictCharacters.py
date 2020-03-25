import SegmentCharacters
import pickle
from pickle import load, dump
import os
import time 
import pandas as pd
print("Loading model")
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

print('Model loaded. Predicting characters of number plate')
classification_result = []
for each_character in SegmentCharacters.characters:
    
    each_character = each_character.reshape(1, -1);
    result = model.predict(each_character)
    classification_result.append(result)

print('Classification result')
print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]

print('Predicted license plate')
print(plate_string)


column_list_copy = SegmentCharacters.column_list[:]
SegmentCharacters.column_list.sort()
rightplate_string = ''
for each in SegmentCharacters.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]

print('License plate')
cobj=open("File.txt",'ab+')
clist=[]
clist.append(rightplate_string)
#print(clist)
dump(clist, cobj)
cobj.close

raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
        'number plate': [rightplate_string]}

df = pd.DataFrame(raw_data, columns = ['date', 'number plate'])

df.to_csv('data.csv')

#print(rightplate_string)