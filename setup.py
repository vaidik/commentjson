from setuptools import setup, find_packages
from commentjson import __version__
import sys

install_requires = []

description = ''

for file_ in ('README',):
    with open('%s.md' % file_) as f:
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
