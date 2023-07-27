from setuptools import setup, find_packages

setup(
    name="dad_joke",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pywhatkit"
    ],
    # Other optional information about your library can be added here
)
