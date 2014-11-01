import csv
import keywords
import qa
import pickle

with open('../Geico_labeled.csv', 'rb') as csvfile:
#with open('../small.csv', 'rb') as csvfile:
	qreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for rownum,row in enumerate(qreader):
		print row
		print row[0]
		kw=keywords.preprocess(row[0].strip('"'))
		qobj = qa.question(rownum,kw)
		pickle.dump(qobj,open('../qs/'+str(rownum),"wb"))
