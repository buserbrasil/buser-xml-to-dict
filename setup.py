from os import lchown
import setuptools


with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='buser-xml-to-dict',
    author='Abraao Barros Lacerda',
    author_email='abraao.lacerda@buser.com.br', 
    version='0.0.6',
    description='Simple lib to handle with xml like a dictionary',
    long_description=long_description,
    py_modules=["xml-to-dict"],
    package_dir={'':'src'},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    classifier=[
        "Programming Language :: Python :: 3",  
        "Programming Language :: Python :: 3.6",  
        "Programming Language :: Python :: 3.7",  
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",   
    ],
    extras_require={
        "dev": [
            "pytest>=3.6" 
        ],
    }
)