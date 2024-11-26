from setuptools import setup, find_packages

setup(
    name="cnatools",
    version="0.1.0",
    author="TChapman",
    author_email="tarunchapman@hotmail.com",
    description="A set of tools to aid with playing the board game 'Campaign for North Africa'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/theonetruenerd/pramikon",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)