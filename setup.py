from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path):
    reqs = []
    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace("\n","") for req in reqs]

        if '-e .' in reqs:
            reqs.remove('-e .')
setup(
    
    name = 'mlProject',
    version='0.0.1',
    author='shasnak',
    author_email='shasank@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)