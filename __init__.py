

bl_info = {
    "name" : "Plugin-Profiler",
    "author" : "bd3d",
    "description" : "Benchmark or Debug Python Plugins",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Development",
    }

from . exectracker import PLUGINPROFILER_OT_exectracker
from . benchmarker import PLUGINPROFILER_OT_benchmarker
from . interface import PLUGINPROFILER_UL_name_list1
from . interface import PLUGINPROFILER_UL_name_list2
from . interface import PLUGINPROFILER_UL_name_list3
from . interface import PLUGINPROFILER_UL_name_list4
from . interface import PLUGINPROFILER_OT_uilist_actions
from . property import PLUGINPROFILER_PR_exectracker_modules_ignore
from . property import PLUGINPROFILER_PR_exectracker_modules_only
from . property import PLUGINPROFILER_PR_exectracker_functions_ignore
from . property import PLUGINPROFILER_PR_exectracker_functions_only
from . property import PLUGINPROFILER_AddonPref

classes = (
    PLUGINPROFILER_OT_exectracker,
    PLUGINPROFILER_OT_benchmarker,
    PLUGINPROFILER_UL_name_list1,
    PLUGINPROFILER_UL_name_list2,
    PLUGINPROFILER_UL_name_list3,
    PLUGINPROFILER_UL_name_list4,
    PLUGINPROFILER_OT_uilist_actions,
    PLUGINPROFILER_PR_exectracker_modules_ignore,
    PLUGINPROFILER_PR_exectracker_modules_only,
    PLUGINPROFILER_PR_exectracker_functions_ignore,
    PLUGINPROFILER_PR_exectracker_functions_only,
    PLUGINPROFILER_AddonPref,
    )

import bpy

def register():

    for cls in classes: 
       bpy.utils.register_class(cls)

    return None 

def unregister():
    
    for cls in reversed(classes): 
        bpy.utils.unregister_class(cls)
    
    return None 

if (__name__=="__main__"):
    pass