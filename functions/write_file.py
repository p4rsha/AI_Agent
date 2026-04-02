import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_directory_abs,file_path))

        valid_target_file_path = os.path.commonpath([working_directory_abs,target_file_path]) == working_directory_abs

        if not valid_target_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # making sure all the parent directories exist
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
            
        return f'The program encountered the following Error : {e}'
    
#Function Schema
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the specified content at a path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)