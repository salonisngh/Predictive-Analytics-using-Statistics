from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Saloni-102317246",
    version="0.3",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
    'console_scripts': [
        'topsis=topsis.topsis:main',
    ],
    },

    author="Saloni Singh",
    description="A command-line Python package to implement the TOPSIS method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
)
