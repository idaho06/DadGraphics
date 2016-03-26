from setuptools import setup, find_packages

setup (
       name='dadgraphics',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['PySDL2>=0.9.3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='idaho06',
       author_email='',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Easy graphics library so my dad is able to program in python',

       # could also include long_description, download_url, classifiers, etc.

  
       )