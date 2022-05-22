from setuptools import setup, find_packages
import os


VERSION = '1.0'
if ("GITHUB_REF" in os.environ) and ("GITHUB_RUN_NUMBER" in os.environ):
    ref = os.environ["GITHUB_REF"]
    build_number = os.environ["GITHUB_RUN_NUMBER"]
    VERSION = f'{VERSION}.{build_number}'
    if 'release' in ref:
        VERSION = f'{VERSION}rc1'
with open("PYPI_VERSION", 'w') as f:
    f.write(VERSION)


setup(
    name='python-release-test',
    version=VERSION,
    package_dir={"": "src"},
    packages=find_packages("src")
)

