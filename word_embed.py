from numpy import asarray
from numpy import zeros
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.layers import Dropout
# define documents
# tead from file store in [] after stemming ?
docs=[]
labels=[]
cls= ["greeting" ,"info" , "nfb" , "pfb", "req", "sug", "yn"]

f = open("questions.txt","r")
for line in f:
	l=line.strip().split('>')
	docs.append(l[0].lower().strip())
	labels.append(l[1].strip().lower())
# print docs
# print labels
# docs = ['Do you like Harry?',
# 		'How do you sound?',
# 		'Do you prefer ice cream or pizza?',
# 		'Alright. I see.',
# 		'No',
# 		'Tell me about your feeling.',
# 		'Would you like to meet my friend?',
# 		'My job is musician.',
# 		]

# define class labels
# labels = [1,1,1,1,1,0,0,0,0,0]
# me
# labels = [1,2,3,4,5,6,7,8] # ch
# labels=["yn-q","wh-q","choice-q","feedback-p","fedback-n","request","suggest","statement"]
encoder = LabelEncoder() # convert strings to int
encoder.fit(labels)
encoded_Y = encoder.transform(labels)
# convert integers to dummy variables (i.e. one hot encoded)
# 
dummy_y = np_utils.to_categorical(encoded_Y)
# for i in range(0,len(labels)):
# 	print labels[i],dummy_y[i]
# prepare tokenizer
# ----------------------------
t = Tokenizer()
t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1
# integer encode the documents
encoded_docs = t.texts_to_sequences(docs)
# print(encoded_docs)
# pad documents to a max length of 4 words
max_length = 15
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
# print(padded_docs)
# load the whole embedding into memory
embeddings_index = dict()
f = open('glove.6B.100d.txt')
for line in f:
	values = line.split()
	word = values[0]
	coefs = asarray(values[1:], dtype='float32')
	embeddings_index[word] = coefs
f.close()
# print('Loaded %s word vectors.' % len(embeddings_index))
# create a weight matrix for words in training docs
embedding_matrix = zeros((vocab_size, 100))
for word, i in t.word_index.items():
	embedding_vector = embeddings_index.get(word)
	if embedding_vector is not None:
		embedding_matrix[i] = embedding_vector
# define model
model = Sequential()
e = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=15, trainable=False)
model.add(e)
model.add(Dropout(0.2, input_shape=(100,)))
model.add(Flatten())


# model.add(Dense(1, activation='sigmoid'))
# model.add(Dense(16, input_dim=32, activation='relu')) # ch added hidden layer
model.add(Dense(7, activation='softmax'))
# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
# summarize the model
print(model.summary())
# fit the model
# model.fit(padded_docs, labels, epochs=50, verbose=0)
model.fit(padded_docs, dummy_y, epochs=50, verbose=0)
# evaluate the model
# loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
encoded_input = t.texts_to_sequences(['what are good shopping malls in the city'])
# print(encoded_docs)
# pad documents to a max length of 4 words
# max_length = 15
padded_input = pad_sequences(encoded_input, maxlen=max_length, padding='post')
output=model.predict(np.array(padded_input))
# [greeting info  nfb  pfb req sug yn]
print "output=",output
loss, accuracy = model.evaluate(padded_docs, dummy_y, verbose=0)
print('Accuracy: %f' % (accuracy*100))

output=output.tolist()
print cls
print output,type(output)
maxprobality=0
for i in range(1,len(cls)) :
	if output[0][i] > output[0][maxprobality] :
		maxprobality = i
print cls[maxprobality]