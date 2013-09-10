import os

from setuptools import setup, find_packages
from commentjson import __version__


install_requires = []

description = ''

path = lambda fname: os.path.join(os.path.dirname(__file__), fname)
for file_ in ('README',):
    with open(path('%s.rst' % file_)) as f:
        description += f.read() + '\n\n'

classifiers = ["Programming Language :: Python"]


setup(name='commentjson',
      version=__version__,
      url='https://github.com/vaidik/commentjson',
      packages=find_packages(),
      long_description=description,
      description=("Add Python style comments in your JSON files."),
      author="Vaidik Kapoor",
      author_email="kapoor.vaidik@gmail.com",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      test_suite='commentjson.tests')
