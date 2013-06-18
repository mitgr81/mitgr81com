from setuptools import setup, find_packages
import app2


setup(
    name="app2",
    version=app2.version,
    packages=find_packages(),
    namespace_packages=['app2'],
    )
