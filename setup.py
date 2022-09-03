from setuptools import setup
import os

DIRECTORY = os.path.dirname(__file__)

REQUIREMENTS = open(os.path.join(DIRECTORY, "REQUIREMENTS.txt")).read().split()
VERSION = open(os.path.join(DIRECTORY, "akinator", "VERSION.txt")).read()
READ_ME = open(os.path.join(DIRECTORY, "README.md")).read()

setup(
    name="akinator",
    version=VERSION,
    author="avizum",
    author_email="juliusrt@outlook.com",
    packages=["akinator"],
    package_data={
        "akinator": ["VERSION.txt"]
    },
    url="https://github.com/avizum/akinator",
    project_urls={
        "Documentation": "https://github.com/avizum/akinator/blob/master/README.rst",
        "Source": "https://github.com/avizum/akinator",
        "Tracker": "https://github.com/avizum/akinator/issues",
    },
    license="MIT License",
    description="An API wrapper for the online game, Akinator, written in Python",
    long_description=READ_ME,
    long_description_content_type="text/x-rst",
    keywords="akinator api async",
    install_requires=REQUIREMENTS,
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Utilities"
    ]
)
