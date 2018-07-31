#!/usr/bin/env python
import json
import sys

# for real life  - load the data, proces it and then dump. (So here its opposite because just playing).

# dump
data = {
	"files": [
		{
		  "pattern": "libs-release-local/zipFiles/*.txt",
		  "target": "./testing2/"
		}
	]
}
with open("data_file.json", "w") as write_file:
	json.dump(data, write_file, indent=4)
json_string1 = json.dumps(data)
json_string2 = json.dumps(data, indent=4)
   #print 'string 1 = ' + json_string1
   #print 'string 2 = ' + json_string2

# load from file
with open("data_file.json", "r") as read_file:
	data = json.load(read_file)
print 'data from file = '
print data

# loads from string
json_string = """
{
	"files": [
		{
		  "pattern": "libs-release-local/zipFiles/*.txt",
		  "target": "./testing2/"
		}
	]
}
"""
data2 = json.loads(json_string)

# get data from input arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Argument 1 = ', sys.argv[1]

# process data
print data
data['files'][0]['target'] = "./" + sys.argv[1] + "/"
print data

# dump again
with open("data_file2.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
