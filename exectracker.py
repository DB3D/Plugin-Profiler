
import bpy 

import os
import sys
import time 
import types
import datetime

from . utils import RunningOperator
from . utils import list_have_common_elements


def tracker(frame: types.FrameType, event: str, arg):
    """tracker to be registered in sys.setprofile
    https://docs.python.org/3/library/sys.html#sys.setprofile"""

    prefs = bpy.context.preferences.addons["Plugin Profiler"].preferences

    #initiate a static variable 
    _f = tracker
    if (not hasattr(_f,"callstack")):
        _f.callstack = {}

    #trace a function 
    if (event=="call"):

        func_source = os.path.abspath(frame.f_code.co_filename)
        func_name = frame.f_code.co_name
        func_key = f"{func_source}:{func_name}"

        #Default Filters:

        #filter out all builtin python function 
        if func_source.startswith(sys.prefix):
            return tracker
        #ignore list comp
        if ( prefs.exectracker_ignore_listcomp):
            if ("<listcomp>" in func_name)
                return tracker

        #Preference Filters: 

        #listen only to specific modules ?
        if ( prefs.exectracker_module_path!="" and not func_source.startswith(prefs.exectracker_module_path) ):
            return tracker
        #ignore some sub-modules?
        if (len(prefs.exectracker_modules_ignore)):
            l1 = [e.name for e in prefs.exectracker_modules_ignore]
            l2 = [e if (".py" not in e) else e.replace(".py","") for e in os.path.normpath(func_source).split(os.sep)]
            if (list_have_common_elements(l1,l2)):
                return tracker
        #only listen to x sub-modules?
        if (len(prefs.exectracker_modules_only)):
            l1 = [e.name for e in prefs.exectracker_modules_only]
            l2 = [e if (".py" not in e) else e.replace(".py","") for e in os.path.normpath(func_source).split(os.sep)]
            if (not list_have_common_elements(l1,l2)):
                return tracker
        #ignore some functions
        if (len(prefs.exectracker_functions_ignore)):
            if prefs.exectracker_functions_ignore_proxy:
                for e in [e.name for e in prefs.exectracker_functions_ignore]:
                    if (e in func_name):
                        return tracker
            else:
                if (func_name in prefs.exectracker_functions_ignore):
                    return tracker
        #only listen to x functions?
        if (len(prefs.exectracker_functions_only)):
            if prefs.exectracker_functions_only_proxy:
                for e in [e.name for e in prefs.exectracker_functions_only]:
                    if (e not in func_name):
                        return tracker
            else:
                if (func_name not in prefs.exectracker_functions_only):
                    return tracker

        #save the time at the moment of a call
        _f.callstack[func_key] = {"datetime":datetime.datetime.now()}

        return tracker

    #function exiting
    elif (event=="return"):

        func_source = os.path.abspath(frame.f_code.co_filename)
        func_name = frame.f_code.co_name
        func_key = f"{func_source}:{func_name}"

        if (func_key in _f.callstack):

            printer = "Executed "

            #generate print string
            
            if prefs.exectracker_print_funcname:

                if prefs.exectracker_print_funcdepth:

                    fct_path = os.path.normpath(func_source).split(os.sep)
                    for i in range(prefs.exectracker_print_funcdepth):
                        modidx = i-prefs.exectracker_print_funcdepth
                        modname = fct_path[modidx]
                        if (".py" in modname):
                            modname = modname.replace(".py","")
                        printer+=f"{modname}\\"

                printer+=f"{func_name}() "

            if prefs.exectracker_print_sourcepath:
                printer+=f"from '{func_source}' "

            if prefs.exectracker_print_datetime:
                start_time = _f.callstack[func_key]["datetime"]
                printer+="at %sh%sm%ss " % (start_time.hour, start_time.minute, start_time.second)

            if prefs.exectracker_print_functime:
                start_time = _f.callstack[func_key]["datetime"]
                elapsed = (datetime.datetime.now() - start_time).total_seconds()
                printer+=f"during '{elapsed:4f}s' "

            print(printer)

            del _f.callstack[func_key]
    
        return tracker

    return tracker

class PLUGINPROFILER_OT_exectracker(RunningOperator):
    """https://stackoverflow.com/questions/73620822/how-to-track-functions-executions-in-real-time/73654195#73654195"""

    bl_idname = "pluginprofiler.exectracker"

    def start(self):
        sys.setprofile(tracker)
        return None 

    def end(self):
        sys.setprofile(None)
        return None 