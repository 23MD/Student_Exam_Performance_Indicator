from setuptools import find_packages,setup # automatically find all the packages in the app that we have created
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    #opening requirements using file path as temp object called file_obj
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # reading each line
        #when reading line from requirement /n will be added hence we need to replace /n with blank using list comprehension
        requirements=[req.replace("\n","") for req in requirements] 

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Mihir',
author_email='mihir.damania@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)