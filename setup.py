'''
cloudelementssdk: SDK for Cloud Elements

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2015, LeadGenius.
Licensed under MIT.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGELOG.txt')).read()
requires = open(os.path.join(here, 'requirements.txt')).read().splitlines()

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = "0.1"

setup(name="cloudelementssdk",
      version=version,
      description="SDK for Cloud Elements",
      long_description=README + '\n\n\n' + CHANGES,
      classifiers=[
        'Programming Language :: Python'
      ],
      keywords="", # Separate with spaces
      author="LeadGenius",
      author_email="developer@leadgenius.com",
      url="http://leadgenius.github.com/cloudelementssdk",
      license="MIT",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      setup_requires=['setuptools_git'],
      cmdclass={'test': PyTest},
      install_requires=requires,
      entry_points={}
)
