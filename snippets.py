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



	return parser

def main():
	"""Main function"""
	logging.info("Starting snippets")
	parser=make_parser()
	arguments= parser.parse_args(sys.argv[1:])

	#Convert arguments from namespace to dictionary
	arguments=vars(arguments)

	command = arguments.pop("command")
	
	if command == 'put':
		name, snippet = put(**arguments)
		print "Stored '{}' as '{}'".format(snippet, name)


if __name__=="__main__":
	main()
