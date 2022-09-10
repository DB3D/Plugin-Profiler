
import bpy 

from . utils import RunningOperator


class PLUGINPROFILER_OT_benchmarker(RunningOperator):
    """https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script"""

    bl_idname = "pluginprofiler.benchmarker"

    def start(self):
        return None 

    def end(self):
        return None 