from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements that need to be installed
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '' )for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
  name = 'mlprojecte2e',
  version = '1.0',
  author = 'yvs_jayanth',
  author_email = 'yvsjayanth31@gmail.com',
  packages = find_packages(),
  install_requires = get_requirements('requirements.txt')
)