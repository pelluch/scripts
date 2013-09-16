#!/usr/bin/env python3
import os
from os.path import expanduser

def get_config_path():

	config_file_path = expanduser('~' + '/.gitrepos')
	return config_file_path

def validate_config():

	config_file_path = get_config_path()
	valid_repos = []
	
	if os.path.isfile(config_file_path):		
		rewrite = False
		with open(config_file_path, 'r') as config_file:
			for line in config_file:
				repo = line.rstrip('\n')
				if repo != '':
					if os.path.isdir(repo) and repo not in valid_repos:
						valid_repos.append(repo)
					else:
						print('Will remove ' + repo)
						rewrite = True

		#print 'Finished check'
		if rewrite:
			#print 'Rewriting...'
			with open(config_file_path, 'w') as config_file:
				for repo in valid_repos:
					config_file.write(repo + "\n")
	return valid_repos

# Attempts to add a new repository to ~/.gitrepos after
# a pull, clone or other operation.
# returns True if folder was added, False otherwise.
def add_new_repo(repo_folder):

	print('Checking if folder ' + repo_folder + ' in cache...')
	# If it's not even a folder, no need to continue
	if not os.path.isdir(repo_folder):
		print('Error: is not a directory')
		return False

	config_file_path = get_config_path()
	full_path = os.path.abspath(repo_folder)

	# Parse config
	with open(config_file_path, 'r') as config_file:
		for line in config_file:
			# If folder is already in cache, do not add
			if line.rstrip() == full_path.rstrip():
				print('Folder already in cache, not adding.')
				return False

	print('Adding folder to cache')
	with open(config_file_path, 'a') as config_file:
		config_file.write(full_path + "\n")
	
	return True

# Receives a folder where a pull was executed. Returns closest path with .git folder.
def find_base_folder(folder):
	old_folder = None
	while folder != old_folder and not os.path.isdir(folder + '/.git'):
		old_folder = folder
		folder = os.path.dirname(folder)
	return folder