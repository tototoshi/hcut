from hcut import  __version__
from setuptools import setup

setup(
    name='hcut',
    py_modules=['hcut'],
    scripts=["bin/hcut"],
    version=__version__,
    license='BSD',
    platforms=['POSIX', 'Windows'],
    description='Cutter for text files with header',
    author='Toshiyuki Takahashi',
    author_email='t.toshi.0412 at gmail.com',
    url='https://github.com/tototoshi/hcut',
    keywords=['cut', 'tsv'],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities ",
        "Topic :: Software Development",
        ],
    long_description='Cutter for text files with header',
    install_requires = ["argparse"]
    )
