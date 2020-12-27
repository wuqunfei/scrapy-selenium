"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages

def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    with open(source) as f:
        dependencies = [line for line in f if "==" in line]


setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)


