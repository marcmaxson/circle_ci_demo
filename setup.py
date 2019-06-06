from setuptools import setup, find_packages

setup(
    name='circle_ci_demo',
    version='1.0.0',
    url='git@github.com:marcmaxson/circle_ci_demo.git',
    author='Marc Maxmeister',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['sphinx','flask'],
)
