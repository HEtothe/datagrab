import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


# This call to setup() does all the work
setup(
    name="datagrab",
    version="0.1.1",
    description="The easy way to access and interpret textual web resources",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HEtothe/datagrab",
    author="HEtothe",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests",
                    "beautifulsoup4",
                    "treelib"],
)
