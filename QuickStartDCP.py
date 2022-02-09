""" 
*
	Title: Quick start DCP
*	Description: This script is used to quickly open DCP in a specific directory
	Made by: Victor Le Juez
*
"""

import subprocess
from itertools import chain
from tkinter import Tk, filedialog


def path_request():
	
	root = Tk(); root.withdraw()
	
	path = filedialog.askdirectory(title='Select your work path')
	
	root.quit()
	
	if path != None and path != '': return path
	else: return False

def start_dcp(open_path='C:\\', dcp_path=r'$VSINSTALLDIR\Common7\Tools\VsDevCmd.bat'):
	
	""" # If you want a "matrix terminal"
	cmd1 = ['color', '0a']
	cmd2 = ['cd', open_path]
	cmd3 = ['cmd', '/k', dcp_path]
	command = list(chain(cmd1, '&', cmd2, '&', cmd3))
	"""
	
	# Command generation
	cmd1, cmd2 = ['cd', work_path], ['cmd', '/k', dcp_path]
	command = list(chain(cmd1, '&', cmd2))
	
	# Starting DCP
	subprocess.Popen(command, shell=True)


if __name__ == '__main__':
	
	# Path to your $VSINSTALLDIR\Common7\Tools\VsDevCmd.bat
	DCP_PATH = r'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat'
	
	# Request the working directory to the user
	work_path = path_request()
	
	# If directory is selected launch DCP
	if work_path != False:
		start_dcp(work_path, DCP_PATH)
