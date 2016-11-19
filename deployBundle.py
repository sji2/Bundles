#!/usr/bin/python3

import os
import sys

#send deployment request
os.system("php /home/santiago/Downloads/Bundle/bundle/rabbitMQClient.php deployBundle " + sys.argv[1])
