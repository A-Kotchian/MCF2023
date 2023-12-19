import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import ctypes

_libserie = np.ctypeslib.load_library('libserie', '.') #the same folder of this file


_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double 

def fibonacci(n):
    return _libserie.fibonacci(int(n))

