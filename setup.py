from setuptools import setup , find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='calcprimenumbers',
    version='1.0',
    author="alejandro velazco",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    description="package example",
    install_requires=install_requires,
    long_description=long_description,
)
