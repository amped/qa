def ie_preprocess(document):
 	     sentences = nltk.sent_tokenize(document)
	     sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
	     sentences = [nltk.pos_tag(sent) for sent in sentences]
