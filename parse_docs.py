import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
import sys
import pickle

class doc(object):
	def __init__(self,id,title=[],text=[],kw=[],abstract=[]):
		self.id=id
		self.title_kw=title
		self.text_kw=text
		self.kw=kw
		self.abstract=abstract

def get_kw(fpath):
	#tree = ET.parse('../Geico_TREC_Documents/simple.xml')
	try:
		with open (fpath, "r") as myfile:
			data=myfile.read().replace('meta:', '').replace('key:','').replace('custom:','').replace('&','&amp;')
		print data
		root = ET.fromstring(data)
		#tree=ET.parse(fpath)
		#root = tree.getroot()
		title=root.find('title').text
		text=root.find('text').text
		child=root.find('metadata')
		stemmedTitle=child.find('stemmedTitle').text
		if(child.find('keywords') is None):
			kw=None
		else:
			kw=child.find('keywords').text

		if(child.find('abstract') is None):
			abstract=None
		else:
			abstract=child.find('abstract').text

		id=child.find('pauTid').text
		return doc(id,title,text,kw,abstract)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		print "Bad file "+fpath
		raise


def main():
	mypath='../Geico_TREC_Documents'
	filenames = ( join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) )
	for fnum,f in enumerate(filenames):
		print f
		doc_obj=get_kw(f)
		fobj=open('../docobjs/'+str(fnum),'wb')
		print fobj
		pickle.dump(doc_obj,fobj)

if __name__=="__main__":
	main()
#for child in root:
#   print child.items(),child.tag, child.attrib
#   print len(child) 
