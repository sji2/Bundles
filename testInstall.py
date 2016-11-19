import configparser 
import os

#Section 1 - Create temp Folder & Unzip Tarball
#Ideally, we would use the config file in the bundle to define where the temp folder
#is created; we can't do this however, because we would end up unzipping to a location
#we don't want, defeating the purpose. It therefore has to be hard-coded.
os.system("mkdir /home/santiago/Desktop/temp")
os.system("tar -xzvf /home/santiago/Desktop/FEv.tgz -C /home/santiago/Desktop/temp")

#Section 2 - configparser
#Initializes the variable that will store the config file during execution.
#Use the absolute path, since the script will never exist inside the same folder
#as the config file.
conf = configparser.ConfigParser()
conf.read("/home/santiago/Downloads/Bundle/testConfig.cfg")

#Section 3 - Import Configurations
#Creates variables from the config file that this script will use to define file locations.
#These paths will make sure that the files are copied to the exact locations as necessary.
#If you would like to test without the config file, use absolute paths in Section 4 and comment
#out the following three lines of code.
temp = conf.get("Test", "tempLocation")
file1 = conf.get("Test", "feFiles")
file2 = conf.get("Test", "siFiles")
file3 = conf.get("Test", "saFiles")
file4 = conf.get("Test", "seFiles")

#Section 4 - File Operation
#Uses the variables created in Section 3 to run specified commands. If you would like to test
#without the config file, remove the variables and use absolute paths.
os.system("mv /home/vm164/Desktop/temp/audi.jpg " + audiPic)
os.system("mv /home/vm164/Desktop/temp/test.txt " + testText)

#Section 5 - Cleanup
#Removes the temp folder and the tarball.
os.system("rm -r /home/vm164/Desktop/testCompress.tgz")
os.system("rm -r " + temp)

os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
