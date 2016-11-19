import configparser 
import os

#get next version from db
ver = (os.popen("php /home/santiago/Downloads/Bundle/bundle/rabbitMQClient.php bundleRequest").read())
ver = ver.strip()
print("The next bundle version is version: " + ver)

#Section 1 - configparser
#Initializes the variable that will store the config file during execution.
#Use the absolute path if the config file is NOT located in the same directory as this script.
conf = configparser.ConfigParser()
conf.read("testConfig.cfg")

#Section 2 - Import Configurations
#Creates variables from the config file that this script will use to define folder locations.
#If you would like to test without the config file, use absolute paths in Section 3 and comment
#out the following four lines of code.
temp = conf.get("Test", "tempLocation")
file1 = conf.get("Test", "feFiles")
file2 = conf.get("Test", "siFiles")
file3 = conf.get("Test", "saFiles")
file4 = conf.get("Test" , "seFiles")
confFile = conf.get("Test", "ownLocation")

#Section 3 - File Operations
#Uses the variables created in Section 2 to run specified commands. If you would like to test
#without the config file, remove the variables and use absolute paths.
os.system("mkdir " + temp)
os.system("sudo cp -R " + file1 + " " + temp)
os.system("sudo cp -R " + file2 + " " + temp)
os.system("sudo cp -R " + file3 + " " + temp)
os.system("sudo cp -R " + file4 + " " + temp)
os.system("cp " + confFile + " " + temp)

#Section 4 - Compress/Send Tarball
#Creates tarball and uses SCP to transfer it to specified VM. Replace IP address with your own.
#NOTE: SSH needs to be installed and configured on the remote machine (the one you are copying to),
#and you will need to create SSH keys, since you can't enter the remote machine's password.

os.system("tar -cvzf /home/santiago/Desktop/FEv" + ver + ".tgz -C /home/santiago/Desktop/temp .")
#os.system("tar -cvzf /home/santiago/Desktop/FEv.tgz -C /home/santiago/Desktop/temp .")

#os.system("scp /home/santiago/Desktop/FEv" + ver + ".tgz vm1@192.168.2.31:/home/vm1/Desktop")
os.system("scp /home/santiago/Desktop/FEv" + ver + ".tgz ses@192.168.2.11:/home/ses/bundles")

os.system("php /home/santiago/Downloads/Bundle/bundle/rabbitMQClient.php updateBundleVer")

#Section 5 - Cleanup
#Removes the temp folder and the tarball.
os.system("sudo rm -r " + temp)
os.system("sudo rm -r /home/santiago/Desktop/FEv" + ver + ".tgz")


os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
