import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="humdrum",
    version="0.0.1",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/humdrum",
    description=("A  CLI tool for youtube data api v3"),
    long_description=read('README.md'),
    license="MIT",
    py_modules=['helper','cli'],
    entry_points={'console_scripts': ['humdrum = cli:main']},
    install_requires=['google-api-python-client', 'click'],
    include_package_data=True
)

