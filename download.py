
import datasets
import json
from datasets import load_dataset
from datasets import load_from_disk

#download the datasets from huggingface
#dataset = load_dataset("iwslt2017","iwslt2017-de-en")
#dataset.save_to_disk("transfromerdataset/de-en")

#get datasets form localfile
dataset=load_from_disk("transfromerdataset/de-en")

'''
#for validation dataset
vlen=len(dataset['validation'])
Vdatalist=[]
for i in range(vlen):
    Vdatalist.append(dataset['validation'][i])

print(len(Vdatalist))

vf=open('validation.json','w',encoding='utf-8')
json.dump(Vdatalist,vf)
'''
'''
#for train dataset
trlen=len(dataset['train'])
Trdatalist=[]
for i in range(trlen):
    Trdatalist.append(dataset['train'][i])

print(len(Trdatalist))

trf=open('train.json','w',encoding='utf-8')
json.dump(Trdatalist,trf)
'''
#for test dataset
telen=len(dataset['test'])
Tedatalist=[]
for i in range(telen):
    Tedatalist.append(dataset['test'][i])

print(len(Tedatalist))

tef=open('test.json','w',encoding='utf-8')
json.dump(Tedatalist,tef)

    

