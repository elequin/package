from setuptools import setup, find_packages

setup(
    name='mypkg',
    version='0.1',
    description='A sample Python package',
    author='mypkg',
    author_email='srikanth_py06@gmail.com',
    packages=find_packages(),
    install_requires=[
        'wheel',
        'setuptools'
    ],
)
