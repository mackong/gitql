from setuptools import setup, find_packages
import os

import gitql


def extra_dependencies():
    import sys
    ret = []
    if sys.version_info < (2, 7):
        ret.append('argparse')
    if sys.platform == 'win32':
        ret.append('pyreadline')
    return ret


def read(*names):
    values = dict()
    extensions = ['txt', 'md']
    for name in names:
        value = ''
        for ext in extensions:
            filename = name + ext
            if os.path.isfile(filename):
                value = open(filename).read()
                break
        values[name] = value
    return values


long_description = """
%(README)s
""" % read('README')

setup(
    name='gitql',
    version=gitql.__version__,
    description='A git query language',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Indented Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
    ],
    keywords='git gitql',
    author='MacKong',
    author_email='mackonghp@gmail.com',
    maintainer='MacKong',
    maintainer_email='mackonghp@gmail.com',
    url='https://github.com/mackong/gitql',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['gitql = gitql.main:main', ]},
    install_requires=[
        'GitPython',
        'prettytable',
        'termcolor',
    ] + extra_dependencies())
