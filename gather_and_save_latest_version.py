bl_info = {
    "name": "Gather and Save Latest Version",
    "description": "Addon to gather latest file from specified path and save new version to same path",
    "author": "Vamps (Swapnil Nare)",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "View3D > Tool",
    "category": "Object"
}

import bpy
import os

class OBJECT_OT_gather_latest_version_operator(bpy.types.Operator):
    """Operator to gather the latest version of the specified file"""
    bl_idname = "object.gather_latest_version_operator"
    bl_label = "Gather Latest Version"
    
    file_path: bpy.props.StringProperty(name="File Path")
    file_prefix: bpy.props.StringProperty(name="File Prefix")
    
    def execute(self, context):
        try:
            files = os.listdir(self.file_path)
            latest_version = 0
            latest_file_path = ""
            for f in files:
                if f.endswith(".blend") and f.startswith(self.file_prefix):
                    try:
                        version = int(f[-7:-6])
                        if version > latest_version:
                            latest_version = version
                            latest_file_path = os.path.join(self.file_path, f)
                    except ValueError:
                        pass
            
            if latest_file_path:
                print("Opening file:", latest_file_path)
                bpy.ops.wm.open_mainfile(filepath=latest_file_path)
            else:
                print("No valid file found.")
        
        except FileNotFoundError:
            print("File path does not exist:", self.file_path)
        
        return {'FINISHED'}

    """Gather latest version of the selected file"""
    bl_idname = "object.gather_latest_version"
    bl_label = "Gather Latest Version"
    
    prefix: bpy.props.StringProperty(default="", name="File Prefix")

    def execute(self, context):
        # Get the directory path
        dir_path = os.path.dirname(bpy.data.filepath)
        
        # Get a list of files in the directory that start with the prefix
        files = [f for f in os.listdir(dir_path) if f.startswith(self.prefix) and f.endswith(".blend")]

        # Get the latest version number
        latest_version = 0
        for f in files:
            try:
                version = int(f.split("_v")[-1].split(".")[0])
                if version > latest_version:
                    latest_version = version
            except ValueError:
                pass
        
        # Open the latest version file
        if latest_version > 0:
            latest_file_name = [f for f in files if f.endswith("_v" + str(latest_version).zfill(3) + ".blend")][0]
            latest_file_path = os.path.join(dir_path, latest_file_name)
            bpy.ops.wm.open_mainfile(filepath=latest_file_path)
            self.report({'INFO'}, "Opened file: " + latest_file_name)
        else:
            self.report({'ERROR'}, "No matching files found")
        
        return {'FINISHED'}
    """Operator to gather the latest version of the specified file"""
    bl_idname = "object.gather_latest_version_operator"
    bl_label = "Gather Latest Version"
    
    file_path: bpy.props.StringProperty(name="File Path")
    file_prefix: bpy.props.StringProperty(name="File Prefix")
    
    def execute(self, context):
        try:
            files = os.listdir(self.file_path)
            latest_version = 0
            latest_file_path = ""
            for f in files:
                if f.endswith(".blend") and f.startswith(self.file_prefix):
                    try:
                        version = int(f[-7:-6])
                        if version > latest_version:
                            latest_version = version
                            latest_file_path = os.path.join(self.file_path, f)
                    except ValueError:
                        pass
            
            if latest_file_path:
                print("Opening file:", latest_file_path)
                bpy.ops.wm.open_mainfile(filepath=latest_file_path)
            else:
                print("No valid file found.")
        
        except FileNotFoundError:
            print("File path does not exist:", self.file_path)
        
        return {'FINISHED'}

    """Operator to gather the latest version of the specified file"""
    bl_idname = "object.gather_latest_version_operator"
    bl_label = "Gather Latest Version"
    
    file_path: bpy.props.StringProperty(name="File Path")
    
    def execute(self, context):
        try:
            files = os.listdir(self.file_path)
            latest_version = 0
            latest_file_path = ""
            for f in files:
                if f.endswith(".blend") and f.startswith("_"):
                    try:
                        version = int(f[-7:-6])
                        if version > latest_version:
                            latest_version = version
                            latest_file_path = os.path.join(self.file_path, f)
                    except ValueError:
                        pass
            
            if latest_file_path:
                print("Opening file:", latest_file_path)
                bpy.ops.wm.open_mainfile(filepath=latest_file_path)
            else:
                print("No valid file found.")
        
        except FileNotFoundError:
            print("File path does not exist:", self.file_path)
        
        return {'FINISHED'}

    """Operator to gather latest version of specified file"""
    bl_idname = "object.gather_latest_version_operator"
    bl_label = "Gather Latest Version"

    file_path: bpy.props.StringProperty(name="File Path")

    def execute(self, context):
        # Get directory and file name from file path
        directory = os.path.dirname(self.file_path)
        file_name = os.path.basename(self.file_path)

        # Get list of all files in directory that match file name format (e.g. "file_v001.blend")
        files = [f for f in os.listdir(directory) if f.startswith(file_name[:-7]) and f.endswith(".blend")]

        if not files:
            # If no matching files found, do nothing
            return {'CANCELLED'}
        else:
            # Otherwise, get latest version number
            latest_version = 0
            for f in files:
                try:
                    version = int(f[-7:-6])
                    latest_version = max(latest_version, version)
                except ValueError:
                    pass


        # Create file path for latest version
        latest_file_name = f"{file_name[:-7]}_v{latest_version:03}.blend"
        latest_file_path = os.path.join(directory, latest_file_name)

        # Open latest version of file
        bpy.ops.wm.open_mainfile(filepath=latest_file_path)

        return {'FINISHED'}

class OBJECT_OT_save_new_version_operator(bpy.types.Operator):
    """Operator to save new version of specified file"""
    bl_idname = "object.save_new_version_operator"
    bl_label = "Save New Version"

    file_path: bpy.props.StringProperty(name="File Path")

    def execute(self, context):
        # Get directory and file name from file path
        directory = os.path.dirname(self.file_path)
        file_name = os.path.basename(self.file_path)

        # Get list of all files in directory that match file name format (e.g. "file_v001.blend")
        files = [f for f in os.listdir(directory) if f.startswith(file_name[:-7]) and f.endswith(".blend")]

        if not files:
            # If no matching files found, save new file as version 001
            new_version = 1
        else:
            # Otherwise, get latest version number and increment by 1
            latest_version = max([int(f[-7:-6]) for f in files])
            new_version = latest_version + 1

        # Create new file name with updated version number
        new_file_name = f"{file_name[:-7]}_v{new_version:03}.blend"
        new_file_path = os.path.join(directory, new_file_name)

        # Save copy of current Blender file as new version
        bpy.ops.wm.save_as_mainfile(filepath=new_file_path)

        return {'FINISHED'}

class OBJECT_PT_gather_latest_version_panel(bpy.types.Panel):
    """Panel for Gather Latest Version addon"""
    bl_idname = "OBJECT_PT_gather_latest_version_panel"
    bl_label = "Gather Latest Version"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label(text="File Path:")
        layout.prop(scene.gather_latest_version_props, "file_path", text="")
        
        layout.label(text="File Prefix:")
        layout.prop(scene.gather_latest_version_props, "file_prefix", text="")
        
        layout.separator()
        layout.operator("object.gather_latest_version_operator", text="Gather Latest Version")

    """Panel for Gather Latest Version addon"""
    bl_idname = "OBJECT_PT_gather_latest_version_panel"
    bl_label = "Gather Latest Version"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        row = layout.row()
        row.operator("object.gather_latest_version", text="Gather Latest Version")

        row = layout.row()
        row.prop(context.scene, "prefix")
    """Panel for Gather Latest Version addon"""
    bl_idname = "OBJECT_PT_gather_latest_version_panel"
    bl_label = "Gather Latest Version"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label(text="File Path:")
        layout.prop(scene.gather_latest_version_props, "file_path", text="")
        
        layout.label(text="File Prefix:")
        layout.prop(scene.gather_latest_version_props, "file_prefix", text="")
        
        layout.separator()
        layout.operator("object.gather_latest_version_operator", text="Gather Latest Version")

    """Panel for Gather and Save Latest Version addon"""
    bl_idname = "OBJECT_PT_gather_and_save_latest_version_panel"
    bl_label = "Gather and Save Latest Version"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Gather and Save"
    bl_order = 0

    def draw(self, context):
        layout = self.layout

        # Create text box for file path
        layout.prop(context.scene, "file_path")

        # Create button to gather latest version
        layout.operator("object.gather_latest_version_operator", text="Gather Latest Version").file_path = context.scene.file_path

        # Create button to save new version
        layout.operator("object.save_new_version_operator", text="Save New Version").file_path = context.scene.file_path

def register():
    bpy.utils.register_class(OBJECT_PT_gather_and_save_latest_version_panel)
    bpy.utils.register_class(OBJECT_OT_gather_latest_version_operator)
    bpy.utils.register_class(OBJECT_OT_save_new_version_operator)
    bpy.types.Scene.file_path = bpy.props.StringProperty(name="File Path")

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_gather_and_save_latest_version_panel)
    bpy.utils.unregister_class(OBJECT_OT_gather_latest_version_operator)
    bpy.utils.unregister_class(OBJECT_OT_save_new_version_operator)
    del bpy.types.Scene.file_path

if __name__ == "__main__":
    register()

