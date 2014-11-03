import qa
import pickle

qpath='../qs'
docpath='../docobjs'
#qfiles = ( join(qpath,f) for f in listdir(qpath) if isfile(join(qpath,f)) )
#docfiles = ( join(docpath,f) for f in listdir(docpath) if isfile(join(docpath,f)) )
qfiles=["../qs/0"]
docfiles=['../docobjs/0']

for qfile in qfiles:
  q=pickle.load(open(qfile,"rb"))
  qkws=set(q.kw)
  print qfile
  print q.id
  print q.kw

  for doc in docfiles:
    print doc
    with open('../docobjs/1.pickle','rb') as docfile:
      docobj=pickle.load(docfile)
  #  print type(docobj.title)
   # print docobj.title
   # as = set(docobj.title)
 #   doc.num_match.append(len(qkws & as)) 
