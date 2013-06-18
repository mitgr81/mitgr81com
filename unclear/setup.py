from setuptools import setup, find_packages
import unclear

setup(
    name="unclear",
    version=unclear.version,
    packages=find_packages(),
    namespace_packages=['unclear'],
)
