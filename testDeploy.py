# Sample deploy script (NON-FUNCTIONAL!!! DO NOT USE!!!)

# This script assumes a few things:

# The bundles are being stored on a central machine (BE QA)
# IP addresses are hard-coded into the script
# Version numbers are integers, and are incremented by 1 for every new bundle
# The machines being deployed to are the API servers

import os

envmt = input("Where do you want to deploy your bundle? [Q]A or [P]roduction: ")
verChoice = input("Do you want to [R]ollback or [U]pdate? ")
qaIP = "192.168.2.21"
prodIP = "192.168.2.22"

if (envmt.lower() == "q"):
	if (verChoice.lower() == "r"):
		print ("Rolling back QA server...")
		#Check all versions available
		#Decrement highest version number by 1 & select it
		#Use SCP to transfer this version to QA (192.168.2.21)
		#Send message via RabbitMQ to QA that a package is waiting to be installed

	elif (verChoice.lower() == "u"):
		print ("Updating QA server...")
		#Check all versions available
		#Select highest version number
		#Use SCP to transfer this version to QA (192.168.2.21)
		#Send message to QA that a package is waiting to be installed

elif (envmt.lower() == "p"):
	if (verChoice.lower() == "r"):
		print ("Rolling back Production server...")
		#Check all versions available
		#Decrement highest version number by 1
		#Use SCP to transfer this version to QA (192.168.2.22)
		#Send message via RabbitMQ to Production that a package is waiting to be installed

	elif (verChoice.lower() == "u"):
		print ("Updating Production server...")
		#Check all versions available
		#Select highest version number
		#Use SCP to transfer this version to QA (192.168.2.22)
		#Send message via RabbitMQ to Production that a package is waiting to be installed

os.system("echo")
os.system("echo Operation completed successfully.")
os.system("echo")