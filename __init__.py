

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

from . presetting import PLUGINPROFILER_OT_add_trackerpreset
from . presetting import PLUGINPROFILER_OT_remove_trackerpreset
from . presetting import PLUGINPROFILER_PT_scatter_preset_header

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
    PLUGINPROFILER_OT_add_trackerpreset,
    PLUGINPROFILER_OT_remove_trackerpreset,
    PLUGINPROFILER_PT_scatter_preset_header,
    PLUGINPROFILER_PR_exectracker_modules_ignore,
    PLUGINPROFILER_PR_exectracker_modules_only,
    PLUGINPROFILER_PR_exectracker_functions_ignore,
    PLUGINPROFILER_PR_exectracker_functions_only,
    PLUGINPROFILER_AddonPref,
    )

import bpy

def cleanse_modules():
    """remove all plugin modules from sys.modules, will load them again, creating an effective hit-reload soluton
    Not sure why blender is no doing this already whe disabling a plugin..."""
    #https://devtalk.blender.org/t/plugin-hot-reload-by-cleaning-sys-modules/20040

    import sys
    all_modules = sys.modules 
    all_modules = dict(sorted(all_modules.items(),key= lambda x:x[0])) #sort them
    
    for k,v in all_modules.items():
        if k.startswith(__name__):
            del sys.modules[k]

    return None 

def register():

    for cls in classes: 
       bpy.utils.register_class(cls)

    return None 

def unregister():
    
    for cls in reversed(classes): 
        bpy.utils.unregister_class(cls)

    cleanse_modules()
    
    return None 

if (__name__=="__main__"):
    pass