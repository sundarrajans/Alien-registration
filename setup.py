from setuptools import setup, find_packages

setup(
    name='Alien-registration',
    version='1.0.0',
    author='Sundar',
    author_email='sundarcool14@gmail.com',
    packages=find_packages(exclude=[]),
    scripts=['register'],
    url='https://github.com/sundarrajans/Alien-registration',
    description='Alien-registration is an application to register Aliens details.' ,
    long_description=open('README.md').read(),
    install_requires=[
        "reportlab == 3.1.8"

	
       ],
)
