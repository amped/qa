import nltk
import helper


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
	{<NN.*|JJ>*<NN.*>} # Nouns and Adjectives, terminated with Nouns
	NP:
	{<NBAR>}
	{<NBAR><IN><NBAR>} # Above, connected with in/of/etc...
	"""
	sent=nltk.pos_tag(sent)
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sent)
	print sent
	print result
	print result.subtrees
	terms = helper.get_terms(result)

	for term in terms:
	    for word in term:
		print word,
	    print
	print "\n\n\n"

if __name__=="__main__":
	#sent="And now for something completely different"
	sent="can you give me a 12 month quote"
	preprocess(sent)
