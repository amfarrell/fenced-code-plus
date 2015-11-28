import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        if isinstance(self.pytest_args, list):
            self.pytest_args.append('-v')
        else:
            self.pytest_args += ' -v'
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='fenced_code_plus',
    packages=['fenced_code_plus'],
    description="A markdown extension for adding additional attributes to fenced code.",
    author = "Andrew M. Farrell",
    author_email = "amfarrell@mit.edu",
    version='0.1',
    py_modules=['fenced_code_plus.fenced_code_plus'],
    install_requires=['markdown>=2.6'],
    tests_require=['pytest',],
    cmdclass = {'test': PyTest},
    url = "https://github.com/amfarrell/fenced-code-plus",
    keywords = ["code format", "fenced code", "markdown"],
)
