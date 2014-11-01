import nltk
import helper

def split_word(word):
	words=word.split('/')
	return words
#	results=[]
#	for word in words:
#		results.extend(word.split('-'))
#	return results
def preprocess(sent):
	sent = nltk.word_tokenize(sent)
#	grammar = r"""
#  	NP:
#	    {<.*>+}          # Chunk everything
#	    }<VBD|IN>+{      # Chink sequences of VBD and IN
#	  """
	#grammar="NP: {<DT>?<CD>*<JJ>*<CD>*<NN>+}" 


	grammar = r"""
	NBAR:
	{<NN.*|JJ|CD>*<NN.*>} # Nouns and Adjectives, terminated with Nouns
	NP:
	{<NBAR>}
	{<NBAR><IN><NBAR>} # Above, connected with in/of/etc...
	"""
	sent=nltk.pos_tag(sent)
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sent)
	#print sent
	#print result
	#print result.subtrees
	terms = helper.get_terms(result)

	kw=[]
	for term in terms:
	    for word in term:
		print word,
		ws=split_word(word)
		for w in ws:
			kw.append(w)
	    print

	return kw

if __name__=="__main__":
	#sent="And now for something completely different"
	sent="can you give me a 12 month quote"
	print preprocess(sent)
