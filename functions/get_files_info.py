import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    try:

        wd_abs_path = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(wd_abs_path, directory))

        # Will be True or False
    
        valid_target_dir = os.path.commonpath([wd_abs_path, target_dir]) == wd_abs_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    
        #processing the valid target dir
        dir_content = os.listdir(target_dir)

        lines = []
        for content in dir_content:
            full_path = os.path.join(target_dir, content)
            lines.append(f"- {content}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")

        return "\n".join(lines)
    
    except Exception as e:
        return f'The program encountered the following Error : {e}'
    

# Function Schema 

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)