import shutil, os

# TODO - replace with interactive interface
project_dest_path = input("Enter the full path to the folder you want the project to be inserted into: ").strip()

# building the project inside the path
projname = input("Enter the project name: ")
projlabel = projname.replace(" ", "")
proj_root_path = project_dest_path + '/' + projlabel
os.mkdir(project_dest_path + '/' + projlabel)

# populating project folder

# source files folder
os.mkdir(proj_root_path + '/' + projlabel.lower() )

# README
fp = open(proj_root_path + '/README.md', 'w')
fp.write('# ' + projlabel + '\n')
# TODO: add description option here
fp.close()

# get path to the script's folder to copy files from project starter
script_path = os.path.dirname(__file__)
shutil.copy(
        script_path + '/PythonStarter/pythonstarter/main.py', 
        proj_root_path + '/' + projlabel.lower() + '/')
shutil.copy(
        script
        )


