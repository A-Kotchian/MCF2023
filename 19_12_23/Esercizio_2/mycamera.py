import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import ctypes

_libmycamera = np.ctypeslib.load_library('libmycamera', '.') #the same folder of this file


_libmycamera.read_camera.argtypes = [ctypes.c_char_p]     #puntatore char 
_libmycamera.read_camera.restype  = ctypes.c_int

def read_camera():
    buffer=ctypes.create_string_buffer(1536*1024*2) #numero di bit nel buffelibmycamerare  
    c= _libmycamera.read_camera(buffer)
    return buffer

