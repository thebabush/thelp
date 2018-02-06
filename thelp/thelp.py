import ctypes
import os
import z3


SO_NAME = '_thelp.so'


so_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SO_NAME)
so = ctypes.cdll.LoadLibrary(so_path)


TRITON_TO_Z3 = ctypes.PYFUNCTYPE(z3.Ast, ctypes.py_object, z3.ContextObj, ctypes.py_object)
_convertAstToZ3 = TRITON_TO_Z3(('convertAstToZ3', so))


def convertAstToZ3(triton_ctx, ast_node):
    return z3.ExprRef(_convertAstToZ3(triton_ctx, z3.main_ctx().ctx, ast_node))

