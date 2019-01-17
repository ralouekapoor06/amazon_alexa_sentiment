from textblob import TextBlob
import pandas as pd 
import sqlite3

conn=sqlite3.connect('amazon_new.sqlite')
cur=conn.cursor()
cur.execute('''SELECT verified_reviews FROM ama1''')
row=cur.fetchall()

cur.execute('''SELECT labels FROM ama1''')
row1=cur.fetchall()

sentences=[]
for i in row:
	sentences.append(i)


labels=[]
for j in row1:
	labels.append(j)

#making sentences and labels proper lists
sentences_new=[]
for s in sentences:
	s=''.join(s)
	sentences_new.append(s)

labels_new=[]
for l in labels:
	l=''.join(l)
	labels_new.append(l)



values=[]
for sent in sentences_new:
	val=TextBlob(sent).polarity
	values.append(val)


count=0
for v in values:
	if v>=0:
		values[count]=1
	else:
		values[count]=0
	count=count+1


cor=0
for i in range(len(values)):
	test = int(labels_new[i])
	test1=values[i]
	if test != test1:
		continue
	cor=cor+1



print("training accuracy is "+str((float(cor)/len(labels_new))*100)+"%")

# ~90% accuracy
 