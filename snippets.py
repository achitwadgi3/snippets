import logging
import csv
import argparse
import sys

logging.basicConfig(filename="output.log", level=logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")

def put(name,snippet,filename):
	"""Store a snippet with associated name in the CSV file"""
	logging.info("Writing {}:{} to {}".format(name,snippet,filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writing snippet {}:{} to file".format(name,snippet))
		writer.writerow([name,snippet])
	logging.debug("Write successful")
	return name,snippet

def get(name, filename):
	"""Retrieve a snippet with a name from a CSV file"""
	flag=0
	logging.info("Searching {} from {}".format(name,filename))
	with open(filename, "r") as f:
		reader = csv.reader(f)
		for line in reader:
			if line[0]==name: 
				print "SNIPNAME: {} SNIPDATA: {}".format(line[0],line[1])
				logging.debug("Found SNIPNAME: {} SNIP: {}".format(line[0],line[1]))
				flag =1
		if flag == 0:
			print 'NOT FOUND'
			logging.debug("Snip SNIPNAME: {} not found".format(name))
    		
	return name

	
def make_parser():
	"""Construct the command line parser"""
	logging.info("Constructing Parser")
	description = "Sotre and retrieve snippets of text"
	parser = argparse.ArgumentParser()
	
	subparsers = parser.add_subparsers(help="Available commands")

	#Subparser for put
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name",help="The name of the snippet")
	put_parser.add_argument("snippet", help="Snippet text")
	put_parser.add_argument("filename", default="snippets.csv", nargs="?" ,help="The snippet filename")
	put_parser.set_defaults(command="put")

	#Subparser for get
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
	get_parser.add_argument("name", help="name of snippet to retrieve")
	get_parser.add_argument("filename",default="snippets.csv", nargs="?" ,help="The snippet filename")
	get_parser.set_defaults(command="get")


	return parser

def main():
	"""Main function"""
	logging.info("Starting snippets")
	parser=make_parser()
	arguments= parser.parse_args(sys.argv[1:])

	#Convert arguments from namespace to dictionary
	arguments=vars(arguments)

	command = arguments.pop("command")
	#print arguments
	if command == 'put':
		name, snippet = put(**arguments)
		print "Stored '{}' as '{}'".format(snippet, name)

	if command == "get":
		name = get(**arguments)



if __name__=="__main__":
	main()
