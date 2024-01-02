#  mypkg

mypkg

### Requirements to achieve

Create a Python package which  contains code that can be reusable, portable , can be called from anywhere 
after importing the package and its modules.

### Requirements
1.Wheel package 

You can install the package using `pip`:
Here, pip means package installer for python.

command:-  ``` pip install wheel ```

Wheel is a binary distribution,its a standard for packaging and distribution of python projects


2.Setuptools package

command:-  ``` pip install setuptools```

Setuptools is a library in Python that facilitates the packaging, distribution, and installation
of Python projects.

### Wheel distribution

Create a wheel distribution of a python package 
```python
python setup.py bdist_wheel 

```
When you run python setup.py bdist_wheel, setuptools will read the information in the setup.py file, 
gather the necessary files, and create a Wheel distribution in the dist directory within the project.

**Model Command**

```
pip install 'path/to/mypkg'
```
This command will install the python package in site-packages and will be ready to use  


### Test cases/ Some test cases written For user to understand 
**Command**

1. ```python
python test1.py``` 

2. ```python
python test2.py```

Here, the test cases from the test1,test2 files will be examined to check the functionality of the 
written functions.

### Importing functions 

Model command:- from package.module import function

From  above command, function is imported from a module in package 



