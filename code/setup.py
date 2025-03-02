from setuptools import setup, find_packages

setup(
    name="ztransform",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sympy>=1.5"
    ],
    author="University Federal of Ceara - Quixada",
    description="A library for Z transform in Python",
    url="https://github.com/pedronobredmc/z-transform-lib",
)
