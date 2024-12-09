import inspect
import __future__

import sys

class dump(type):
    
    def __new__(metacls, name, parents, namespace):
        #print(f'namespace = {namespace}')
        for func_name, func in namespace.items():
            if callable(func):  # if method
                @staticmethod
                def wrapp(func):
                    def wrapped_method(self, *args, **kwargs):
                        print(f"{func.__name__}: {args}, {kwargs}")
                        return func(self, *args, **kwargs)
                    return wrapped_method

                namespace[func_name] = wrapp(func)  # new addition to old 
        return super().__new__(metacls, name, parents, namespace)


exec(sys.stdin.read())
