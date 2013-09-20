#!/usr/bin/env python
import os
from os.path import expanduser
import argparse

def parse_clone(opts, unknown):

	print('Repository used: ' + opts.repository)
	if opts.directory:
		print('Directory used: ' + opts.directory)
		directory = os.path.abspath(opts.directory)
	else:
		base_name = os.path.basename(opts.repository.rstrip('/').split(':')[-1])
		file_name, extension = os.path.splitext(base_name)		
		print('Directory used: ' + file_name)
		directory = os.path.abspath(file_name)

	add_new_repo(directory)


def parse_pull(opts, unknown):
	if opts.repository:
		print('Repository pulled: ' + opts.repository)
	else:
		print('Pulling from base')

	base_folder = find_base_folder(os.getcwd())
	add_new_repo(base_folder)
	
def add_clone_subparser(subparsers):

	parser_clone = subparsers.add_parser('clone')
	parser_clone.add_argument('repository')
	parser_clone.add_argument('directory', nargs='?')
	parser_clone.set_defaults(func=parse_clone)

def add_pull_subparser(subparsers):

	parser_pull = subparsers.add_parser('pull')
	parser_pull.add_argument('repository', nargs='?')
	parser_pull.add_argument('refspec', nargs='*')
	parser_pull.set_defaults(func=parse_pull)

def get_git_parser():

	parser = argparse.ArgumentParser(description='Python front end for several git commands', conflict_handler='resolve', add_help=False)
	subparsers = parser.add_subparsers()

	parser_add = subparsers.add_parser('add')
	parser_checkout_index = subparsers.add_parser('checkout-index')
	parser_cvsserver = subparsers.add_parser('cvsserver')
	parser_fsck_objects = subparsers.add_parser('fsck-objects')
	parser_ls_files = subparsers.add_parser('ls-files')
	parser_mktree = subparsers.add_parser('mktree')
	parser_reflog = subparsers.add_parser('reflog')
	parser_revert = subparsers.add_parser('revert')
	parser_tag = subparsers.add_parser('tag')
	parser_add__interactive = subparsers.add_parser('add--interactive')
	parser_cherry = subparsers.add_parser('cherry')
	parser_daemon = subparsers.add_parser('daemon')
	parser_gc = subparsers.add_parser('gc')
	parser_ls_remote = subparsers.add_parser('ls-remote')
	parser_mv = subparsers.add_parser('mv')
	parser_relink = subparsers.add_parser('relink')
	parser_rm = subparsers.add_parser('rm')
	parser_tar_tree = subparsers.add_parser('tar-tree')
	parser_am = subparsers.add_parser('am')
	parser_cherry_pick = subparsers.add_parser('cherry-pick')
	parser_describe = subparsers.add_parser('describe')
	parser_get_tar_commit_id = subparsers.add_parser('get-tar-commit-id')
	parser_ls_tree = subparsers.add_parser('ls-tree')
	parser_name_rev = subparsers.add_parser('name-rev')
	parser_remote = subparsers.add_parser('remote')
	parser_send_email = subparsers.add_parser('send-email')
	parser_unpack_file = subparsers.add_parser('unpack-file')
	parser_annotate = subparsers.add_parser('annotate')
	parser_citool = subparsers.add_parser('citool')
	parser_diff = subparsers.add_parser('diff')
	parser_grep = subparsers.add_parser('grep')
	parser_mailinfo = subparsers.add_parser('mailinfo')
	parser_notes = subparsers.add_parser('notes')
	parser_remote_ext = subparsers.add_parser('remote-ext')
	parser_send_pack = subparsers.add_parser('send-pack')
	parser_unpack_objects = subparsers.add_parser('unpack-objects')
	parser_apply = subparsers.add_parser('apply')
	parser_clean = subparsers.add_parser('clean')
	parser_diff_files = subparsers.add_parser('diff-files')
	parser_gui = subparsers.add_parser('gui')
	parser_mailsplit = subparsers.add_parser('mailsplit')
	parser_p4 = subparsers.add_parser('p4')
	parser_remote_fd = subparsers.add_parser('remote-fd')
	parser_sh_i18n__envsubst = subparsers.add_parser('sh-i18n--envsubst')
	parser_update_index = subparsers.add_parser('update-index')
	parser_archimport = subparsers.add_parser('archimport')
	parser_find = subparsers.add_parser('find')
	parser_browse = subparsers.add_parser('browse')

	add_clone_subparser(subparsers)
	add_pull_subparser(subparsers)

	parser_diff_index = subparsers.add_parser('diff-index')
	parser_gui__askpass = subparsers.add_parser('gui--askpass')
	parser_merge = subparsers.add_parser('merge')
	parser_pack_objects = subparsers.add_parser('pack-objects')
	parser_remote_ftp = subparsers.add_parser('remote-ftp')
	parser_shell = subparsers.add_parser('shell')
	parser_update_ref = subparsers.add_parser('update-ref')
	parser_archive = subparsers.add_parser('archive')
	parser_column = subparsers.add_parser('column')
	parser_diff_tree = subparsers.add_parser('diff-tree')
	parser_hash_object = subparsers.add_parser('hash-object')
	parser_merge_base = subparsers.add_parser('merge-base')
	parser_pack_redundant = subparsers.add_parser('pack-redundant')
	parser_remote_ftps = subparsers.add_parser('remote-ftps')
	parser_shortlog = subparsers.add_parser('shortlog')
	parser_update_server_info = subparsers.add_parser('update-server-info')
	parser_bisect = subparsers.add_parser('bisect')
	parser_commit = subparsers.add_parser('commit')
	parser_difftool = subparsers.add_parser('difftool')
	parser_help = subparsers.add_parser('help')
	parser_merge_file = subparsers.add_parser('merge-file')
	parser_pack_refs = subparsers.add_parser('pack-refs')
	parser_remote_http = subparsers.add_parser('remote-http')
	parser_show = subparsers.add_parser('show')
	parser_upload_archive = subparsers.add_parser('upload-archive')
	parser_bisect__helper = subparsers.add_parser('bisect--helper')
	parser_commit_tree = subparsers.add_parser('commit-tree')
	parser_difftool__helper = subparsers.add_parser('difftool--helper')
	parser_http_backend = subparsers.add_parser('http-backend')
	parser_merge_index = subparsers.add_parser('merge-index')
	parser_patch_id = subparsers.add_parser('patch-id')
	parser_remote_https = subparsers.add_parser('remote-https')
	parser_show_branch = subparsers.add_parser('show-branch')
	parser_upload_pack = subparsers.add_parser('upload-pack')
	parser_blame = subparsers.add_parser('blame')
	parser_config = subparsers.add_parser('config')
	parser_fast_export = subparsers.add_parser('fast-export')
	parser_http_fetch = subparsers.add_parser('http-fetch')
	parser_merge_octopus = subparsers.add_parser('merge-octopus')
	parser_peek_remote = subparsers.add_parser('peek-remote')
	parser_remote_testsvn = subparsers.add_parser('remote-testsvn')
	parser_show_index = subparsers.add_parser('show-index')
	parser_var = subparsers.add_parser('var')
	parser_branch = subparsers.add_parser('branch')
	parser_count_objects = subparsers.add_parser('count-objects')
	parser_fast_import = subparsers.add_parser('fast-import')
	parser_http_push = subparsers.add_parser('http-push')
	parser_merge_one_file = subparsers.add_parser('merge-one-file')
	parser_prune = subparsers.add_parser('prune')
	parser_repack = subparsers.add_parser('repack')
	parser_show_ref = subparsers.add_parser('show-ref')
	parser_verify_pack = subparsers.add_parser('verify-pack')
	parser_bundle = subparsers.add_parser('bundle')
	parser_credential = subparsers.add_parser('credential')
	parser_fetch = subparsers.add_parser('fetch')
	parser_imap_send = subparsers.add_parser('imap-send')
	parser_merge_ours = subparsers.add_parser('merge-ours')
	parser_prune_packed = subparsers.add_parser('prune-packed')
	parser_replace = subparsers.add_parser('replace')
	parser_stage = subparsers.add_parser('stage')
	parser_verify_tag = subparsers.add_parser('verify-tag')
	parser_cat_file = subparsers.add_parser('cat-file')
	parser_credential_cache = subparsers.add_parser('credential-cache')
	parser_fetch_pack = subparsers.add_parser('fetch-pack')
	parser_index_pack = subparsers.add_parser('index-pack')
	parser_merge_recursive = subparsers.add_parser('merge-recursive')
	parser_repo_config = subparsers.add_parser('repo-config')
	parser_stash = subparsers.add_parser('stash')
	parser_web__browse = subparsers.add_parser('web--browse')
	parser_check_attr = subparsers.add_parser('check-attr')
	parser_credential_cache__daemon = subparsers.add_parser('credential-cache--daemon')
	parser_filter_branch = subparsers.add_parser('filter-branch')
	parser_init = subparsers.add_parser('init')
	parser_merge_resolve = subparsers.add_parser('merge-resolve')
	parser_push = subparsers.add_parser('push')
	parser_request_pull = subparsers.add_parser('request-pull')
	parser_status = subparsers.add_parser('status')
	parser_whatchanged = subparsers.add_parser('whatchanged')
	parser_check_ignore = subparsers.add_parser('check-ignore')
	parser_credential_gnome_keyring = subparsers.add_parser('credential-gnome-keyring')
	parser_fmt_merge_msg = subparsers.add_parser('fmt-merge-msg')
	parser_init_db = subparsers.add_parser('init-db')
	parser_merge_subtree = subparsers.add_parser('merge-subtree')
	parser_quiltimport = subparsers.add_parser('quiltimport')
	parser_rerere = subparsers.add_parser('rerere')
	parser_stripspace = subparsers.add_parser('stripspace')
	parser_write_tree = subparsers.add_parser('write-tree')
	parser_check_mailmap = subparsers.add_parser('check-mailmap')
	parser_credential_store = subparsers.add_parser('credential-store')
	parser_for_each_ref = subparsers.add_parser('for-each-ref')
	parser_instaweb = subparsers.add_parser('instaweb')
	parser_merge_tree = subparsers.add_parser('merge-tree')
	parser_read_tree = subparsers.add_parser('read-tree')
	parser_reset = subparsers.add_parser('reset')
	parser_submodule = subparsers.add_parser('submodule')
	parser_check_ref_format = subparsers.add_parser('check-ref-format')
	parser_cvsexportcommit = subparsers.add_parser('cvsexportcommit')
	parser_format_patch = subparsers.add_parser('format-patch')
	parser_log = subparsers.add_parser('log')
	parser_mergetool = subparsers.add_parser('mergetool')
	parser_rebase = subparsers.add_parser('rebase')
	parser_rev_list = subparsers.add_parser('rev-list')
	parser_svn = subparsers.add_parser('svn')
	parser_checkout = subparsers.add_parser('checkout')
	parser_cvsimport = subparsers.add_parser('cvsimport')
	parser_fsck = subparsers.add_parser('fsck')
	parser_lost_found = subparsers.add_parser('lost-found')
	parser_mktag = subparsers.add_parser('mktag')
	parser_receive_pack = subparsers.add_parser('receive-pack')
	parser_rev_parse = subparsers.add_parser('rev-parse')
	parser_symbolic_ref = subparsers.add_parser('symbolic-ref')

	parser.add_argument('--version', action='store_true')
	parser.add_argument('--help', nargs='?')
	parser.add_argument('--exec-path=', nargs='?')
	parser.add_argument('--html-path', action='store_true')
	parser.add_argument('--man-path', action='store_true')
	parser.add_argument('--info-path', action='store_true')
	parser.add_argument('-p, --paginate', action='store_true')
	parser.add_argument('--no-pager', action='store_true')
	parser.add_argument('--no-replace-objects', action='store_true')
	parser.add_argument('--bare', action='store_true')
	parser.add_argument('--git-dir=', nargs='?')
	parser.add_argument('--work-tree=', nargs='?')
	parser.add_argument('--namespace=', nargs='?')

	return parser

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