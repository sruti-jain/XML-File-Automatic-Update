# Importing necessary libraries
import os
import xml.etree.cElementTree as ET

# Fetching the working directory and the xml files in the folder
cwd = os.getcwd()
cwd = cwd + '\\problem'
onlyfiles = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

# Making a new directory to save the modified files
if not os.path.exists('Modified'):
    os.makedirs('Modified')

# Adding the new attribute 'Objective' and saving the files in new directory
for filenames in onlyfiles:
    path = cwd + '\\' + filenames
    tree = ET.parse(path)
    root = tree.getroot()
    for problem in root.iter('problem'):
        problem.set('objectives', ' ')
    tree.write(os.getcwd() + '\\Modified\\' + filenames)