#!/usr/bin/env python2

from distutils.core import setup, Extension
import os


include_dirs = []
runtime_library_dirs = []

# Figure out if we are in a venv
venv = os.getenv('VIRTUAL_ENV', None)
if venv:
    # This is needed in order to link to a Z3 installed under a venv
    include_dirs.append(os.path.join(venv, 'include'))
    runtime_library_dirs.append(os.path.join(venv, 'lib'))


setup(
    name='thelp',
    ext_modules=[
        Extension(
            'thelp._thelp',
            ['src/thelp.cpp'],
            extra_compile_args=['-std=c++11'],
            include_dirs=include_dirs,
            runtime_library_dirs=runtime_library_dirs,
            libraries=[
                #'z3',
                'triton',
            ],
        )
    ],
    #py_modules=['thelp'],
    packages=['thelp'],
)

