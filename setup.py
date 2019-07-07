from __future__ import with_statement

import os
import sys

from setuptools import setup, find_packages


__version__ = '.'.join(map(str, (0, 8, 0)))

install_requires = [
    'lark-parser>=0.7.1'
]
if sys.version_info <= (2, 6):
    install_requires.append('simplejson')

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
      description=("Add Python and JavaScript style comments in your JSON "
                   "files."),
      author="Vaidik Kapoor",
      author_email="kapoor.vaidik@gmail.com",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      tests_require=[
          'six',
      ],
      test_suite='commentjson.tests')
