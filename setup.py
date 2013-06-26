from setuptools import setup, find_packages
import mitgr81com

setup(
    name="mitgr81com",
    version=mitgr81com.version,
    packages=find_packages(),
    namespace_packages=['mitgr81com'],
)
