import subprocess
import sys
import kalhatti

reqs = subprocess.check_output([sys.executable,'pip'])
install_requires = [r.decode().split('==')[0] for r in reqs.split()]

	

	if(install_requires)
		install_packages == 1
			print(success)
	elif(!install_packages)
			print(install_requires)		
	
	
	
