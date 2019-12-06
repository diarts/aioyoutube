from setuptools import setup

setup(
    name='aioyoutube',
    version='0.1',
    packages=['aioyoutube', 'aioyoutube.helpers', 'aioyoutube.handlers',
              'aioyoutube.exeptions'],
    url='https://github.com/diarts/aioyoutube.git',
    license='MIT',
    author='konstantin',
    author_email='',
    description='Async wrapper for REST API youtube.com'
)
