import os , subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    
    try:
        working_directory_abs = os.path.abspath(working_directory)

        targe_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_path = os.path.commonpath([targe_file_path, working_directory_abs]) == working_directory_abs

        #Set the cage
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        #ensure the file is valid
        if not os.path.isfile(targe_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        #ensure the file is a .py
        if file_path.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        
        # Now , Build the shell command from those inputs ( filepath and args ) THEN Execute it and capture the output
        
        command = ["python", targe_file_path]
        
        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=working_directory_abs , capture_output= True, text= True, timeout= 30)

        # Output String

        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"

        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT: {result.stdout}"
            if result.stderr:
                output += f"STDERR: {result.stderr}"

        return output
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

#Function Schema
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to the working directory with optional command-line arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional command-line arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)