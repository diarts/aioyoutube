from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='aioyoutube',
    version='0.1.4',
    packages=['aioyoutube', 'aioyoutube.helpers', 'aioyoutube.handlers',
              'aioyoutube.exeptions'],
    url='https://github.com/diarts/aioyoutube.git',
    license='MIT',
    author='konstantin',
    author_email='korobanov1993@yandex.ru',
    description='Async wrapper for REST API youtube.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7.2',
)
