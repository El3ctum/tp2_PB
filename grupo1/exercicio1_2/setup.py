from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("openMp.pyx", compiler_directives={'language_level': "3"}),
    include_dirs=[numpy.get_include()],
    define_macros=[('CYTHON_TRACE', '1')],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp']
)