#!/usr/bin/env python2

from distutils.core import setup, Extension


setup(
    name='thelp',
    ext_modules=[
        Extension(
            'thelp._thelp',
            ['src/thelp.cpp'],
            extra_compile_args=['-std=c++11'],
            libraries=['z3', 'triton'],
        )
    ],
    #py_modules=['thelp'],
    packages=['thelp'],
)

