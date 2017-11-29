#!/usr/bin/python
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import json
from parse import get_table

#creating a new user session
client = MongoClient()

#creating a new DB called, traveldata
db = client.webot

def response_manager(details) :
	# print details,"response"
	service=details["service"]
	if service == "" :
		print("				Sorry for the inconvience , service not available ")
	table = get_table(service)
	# print "				",table,details["location"]
	records = db[table].find({"location":details["location"].lower()})
	msg=""
	for doc in records :
		msg=msg+"\n"+" Vendor: "+doc["name"]+" Ratings :"+str(doc["rating"])
	print "				Below are the most suitable vendors for ",details["service"]
		# for %s:"%service")
		# records= db[service].find({"location":"Hyderabad".lower()})
		# for entry in records :
		# 	# print entry,type(entry)
	print "				",msg
	return msg

def generate_response(req_type,msg):
	if(req_type == "info"):
		print("				Thanks for the information.")
	elif req_type == "greeting" :
		print "				Welcome to Webot !!!"
	elif(req_type == "yn"):
		print("					Yes,this is the best available option.")
	elif req_type == "req":
		print ""
	else :
		print "				This service is currently not provided by Webot"

generate_response("req","venues")		