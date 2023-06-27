from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements (file_path:str)->List[str]:
    '''
    This function will return all the requirements from the file path
    '''
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirement=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='genericMLproject',
verison='0.1.0',
author='Jiten',
author_email='jitensutarbrjn2000@gmail.com',
packges=find_packages(),
install_requires=get_requirements('requirements.txt')
)