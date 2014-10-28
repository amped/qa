import csv
import keywords

#with open('../Geico_labeled.csv', 'rb') as csvfile:
with open('../small.csv', 'rb') as csvfile:
	qreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in qreader:
		print row
		print row[0]
		keywords.preprocess(row[0].strip('"'))

