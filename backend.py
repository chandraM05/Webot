import sys

from select import select

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

from parse import extract_info,get_vendor
from response import generate_response,response_manager
from spell import spell_check
from context_handling import context_manager,incomplete
import time


msg = ""

last_query_time=time.time()
cls= ["greeting" ,"info" , "nfb" , "pfb", "req", "sug", "yn"]

global_event=""
global_service=""
events_dic={"reception":0,"sangeet":0,"mehendi":0,"engagement":0,"wedding":0,"haldi":0}

# def fire_ini( threadName,delay):
# 	current_time=time.time()
# 	elapsed = current_time - last_query_time 
# 	print last_query_time,current_time,elapsed
# 	if elapsed > 15 :
# 		get_question()
#       # print "%s: %s" % ( threadName, time.ctime(time.time()) )

selected_vendors=""

def end_plan() :
	for key,value in events_dic.iteritems():
		if value!=0:
			print key
			for key1,value1 in events_dic[key].services.iteritems():
				if value1==1 or value1==2:
					k=events_dic[key]
					for attr, value2 in k.__dict__.iteritems():
						if attr == key1:
							print attr
							if value2[0]!="":
								print value2[0]
							if value2[1]!="":
								print value2[1]

						# print attr,value2
	print selected_vendors



if __name__ == "__main__":


	#  Train Dialogue actions 
	docs=[]
	labels=[]

	f = open("questions.txt","r")
	for line in f:
		l=line.strip().split('>')
		docs.append(l[0].lower().strip())
		labels.append(l[1].strip().lower())

	encoder = LabelEncoder() # convert strings to int
	encoder.fit(labels)
	encoded_Y = encoder.transform(labels)

	dummy_y = np_utils.to_categorical(encoded_Y)

	t = Tokenizer()
	t.fit_on_texts(docs)
	vocab_size = len(t.word_index) + 1
	encoded_docs = t.texts_to_sequences(docs)
	max_length = 15
	padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
	embeddings_index = dict()
	f = open('glove.6B.100d.txt')
	for line in f:
		values = line.split()
		word = values[0]
		coefs = asarray(values[1:], dtype='float32')
		embeddings_index[word] = coefs
	f.close()
	embedding_matrix = zeros((vocab_size, 100))
	for word, i in t.word_index.items():
		embedding_vector = embeddings_index.get(word)
		if embedding_vector is not None:
			embedding_matrix[i] = embedding_vector
	model = Sequential()
	e = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=15, trainable=False)
	model.add(e)
	# model.add(Dropout(0.2, input_shape=(100,)))
	model.add(Flatten())


	model.add(Dense(7, activation='softmax'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
	# print(model.summary())

	model.fit(padded_docs, dummy_y, epochs=50, verbose=0)
	print "Training complete"

	last_query_time=time.time()
	while (1) :
		# query = ""
		timeout = 150
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			query = sys.stdin.readline()
			# print query
		else :
			# print "incomplete"
			incomplete(global_event,global_service, events_dic,msg)
			continue
		# print query," 22",type(query)
		if query.lower() == "end\n" or query.lower() == "exit\n 	" :
			print "				Your final Plan"
			end_plan()
			break
	# 	query = raw_input()
	# 	# print query ," : Query before spell checker"
		query = spell_check(query.lower())
		

		# print query ," : Query after spell checker"
		l=[]
		l.append(query.lower())
		encoded_input = t.texts_to_sequences(l)
		# pad documents to a max length of 4 words
		# max_length = 15
		padded_input = pad_sequences(encoded_input, maxlen=max_length, padding='post')
		output=model.predict(np.array(padded_input))

		output=output.tolist()

		maxprobality=0
		for i in range(1,len(cls)) :
			if output[0][i] > output[0][maxprobality] :
				maxprobality = i
		req_type = cls[maxprobality]
		# print "Dialogue act : ",req_type

		details={}
		if req_type == "info" or req_type == "req" :
			details = extract_info(query)
			details,global_event,global_service, events_dic = context_manager(details,global_event,global_service, events_dic)
			# print details
			# print events_dic[global_event].printdetails()
			if details["service"] == "" and req_type == "req" :
				print "				Sorry for the inconvience , service not available"
			if req_type == "req" :
				msg=response_manager(details)
				generate_response(req_type,msg)
			else :
				generate_response(req_type,"")
		elif req_type == "yn" or req_type == "greeting" :
			generate_response(req_type,"")

		elif req_type == "pfb" :
			vendor = get_vendor(query,msg)
			print "				",vendor ," : Selected vendor"
			selected_vendors = selected_vendors+global_event+"->"+global_service+"->"+vendor+"\n";

		last_query_time=time.time()

# import socket

# if __name__ == "__main__":
#     # serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # serversocket.bind(('localhost', 9988))
#     # serversocket.listen(1) # become a server socket, maximum 1 connections
#     # print "Chat server started on port " + str(9988)

#     while True:
#         connection, address = serversocket.accept()
#         buf = connection.recv(256)
#         if len(buf) > 0:
#             print "USER: ",buf
#             # resp=query_handling(buf)
#             print "Webot: ",resp
#             connection.send(resp)
#         connection.close();
#     serversocket.close()