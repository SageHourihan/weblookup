from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='weblookup',
      version='1.0',
      description='Command line tool',
      long_description=readme(),
      url='https://github.com/SageHourihan/weblookup.git',
      author='Sage Hourihan',
      author_email='samiho97@gmail.com',
      license='MIT',
      packages=['weblookup'],
      entry_points = {
        'console_scripts': ['weblookup=weblookup.command_line:main'],
    }
)