from setuptools import setup

setup(
    name="johnnydep",
    version="0.4",
    description="Display dependency tree of Python distribution",
    long_description=open("README.md").read(),
    packages=["johnnydep"],
    author="Wim Glenn",
    author_email="hey@wimglenn.com",
    license="MIT",
    url="https://github.com/wimglenn/johnnydep",
    install_requires=[
        "anytree",
        "structlog",
        "tabulate",
        "wimpy",
        "colorama",  # pretty output for structlog
        "cachetools",
        "oyaml",
        "pytoml",
        "pip",
        "packaging>=17",
        "wheel>=0.31.0",
        "setuptools>=38.3",  # for pkg_resources
        "pkginfo>=1.4.2",
    ],
    entry_points={
        "console_scripts": [
            "johnnydep=johnnydep.cli:main",
            "pipper=johnnydep.pipper:main",
        ]
    },
)
