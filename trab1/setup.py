
from distutils.core import setup
from distutils.core import Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from os.path import splitext, basename, join as pjoin, walk
import os

class CleanCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._clean_me = [ ]
        for root, dirs, files in os.walk('.'):
            for f in files:
                if f.endswith('.pyc'):
                    self._clean_me.append(pjoin(root, f))

    def finalize_options(self):
        pass

    def run(self):
        for clean_me in self._clean_me:
            try:
                os.unlink(clean_me)
            except:
                pass

class DatasetCommand(Command):
    """Generate datasets."""
    user_options = []
    description = 'generate datasets'

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        pass


class TestCommand(Command):
    user_options = [ ]
    description = 'run unittests'

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/, and runs them.
        '''
        testfiles = [ ]
        for t in glob(pjoin(self._dir, 'tests', '*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    ['tests', splitext(basename(t))[0]])
                )

        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity = 1)
        t.run(tests)


setup(name='trab1',
      version='1.0',
      description='Primeiro trabalho para Metaheuristicas',
      author='Rodrigo Mosconi',
      author_email='rmosconi@inf.puc-rio.br, mosconi.rmg@gmail.com',
      test_suite= 'tests',
      cmdclass = {  'dataset': DatasetCommand }
      )
