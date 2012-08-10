import subprocess
import sys
import os
"""
hosts.py
By Jason Knabl

Script to easily add/remove entries from hosts file
on Unix-like machines. Use on command line.

-a [address] adds an entry
-r [address] removes an entry

TODO: Convert arg parser to use optparse module
			Add dual hosts switching functionality.
			Clean up.

"""

def addToHosts(address):
	#check that this is a valid address/ip, then --
	#validated, so add it
	toAdd = "\n127.0.0.1	%s" % address
	appendToFile('/etc/hosts', toAdd)
	print "\nAdded %s to hosts" % address

def removeFromHosts(address):
	#check that this is a valid address/ip, then --
	#check if it's in the file, then remove it
	foundAdd = 0
	f = open('/etc/hosts', 'rw')
	nf = open('/etc/hosts.new', 'a+')
	for line in f:
		if address in line:
			foundAdd = 1
		else:
			nf.write(line)	
	f.close()
	nf.close()
	os.rename('/etc/hosts.new', '/etc/hosts')
	if foundAdd == 1:
		print "Removed %s from hosts.\n" % address
	else:
		print "Didn't find entry %s.\n" % address

def appendToFile(file, stuff):
	f = open(file, 'a+')
	f.write(stuff)
	f.close()

def stripWhitespace(file):
	temp = open('/etc/hosts.tmp', 'a+') 	
	with open(file, 'rw') as f:
		for line in f:
			if line.strip('\r\n'):
				new = line.strip('\r\n')
				temp.write(new + '\n')
	os.rename('/etc/hosts.tmp', '/etc/hosts')

def main():
	#let's parse command line arguments
	arguments = sys.argv

	if arguments[1] == "-a":
		#add entry to hosts	
		addToHosts(arguments[2])
		stripWhitespace('/etc/hosts')
	elif arguments[1] == "-r":
		#remove entry from hosts
		removeFromHosts(arguments[2])
		stripWhitespace('/etc/hosts')
	elif arguments[1] == "lol":
		print "YOU TYPED LOL -- YOU'RE FUNNY!"
	else:
		print "Here be dragons... Try again."

if __name__=='__main__':
	main()
