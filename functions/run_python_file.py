import os
import subprocess 
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
  abs_working_dir = os.path.abspath(working_directory)
  target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
  valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

  if not valid_target_file:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(target_file):
    return f'Error: "{file_path}" does not exist or is not a regular file'
  
  if not target_file.endswith('.py'):
    return f'Error: "{file_path}" is not a Python file'
  
  command = ["python3", target_file]

  if args != None:
    command.extend(args)
   
  try:
    output = subprocess.run(
      command, 
      capture_output=True, 
      text=True, 
      cwd=abs_working_dir, 
      timeout=30
      )
    
    final_string = f"""
      STDOUT:\n{output.stdout}\nSTDERR:\n{output.stderr}
    """
    if output.stdout == "" and output.stderr == "":
      final_string += "Note: Python file produced no output.\n"

    if output.returncode != 0:
      final_string += f"Error: Python file exited with code {output.returncode}\n" 
    
    return final_string
  
  except Exception as e:
    return f"Error: executing Python file: {e}"
  
schema_run_python_file = types.FunctionDeclaration(
  name="run_python_file",
  description="Executes or runs a Python (.py) file. Use this when the user asks to run, execute, or launch a specific Python file by name. Accepts an optional array of string arguments to be passed to the Python file.",
  parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
          "file_path": types.Schema(
              type=types.Type.STRING,
              description="Path to the file to run, relative to the working directory",
          ),
          "args": types.Schema(
              type=types.Type.ARRAY,
              description="Optional array of string arguments to be passed to the Python file",
              items=types.Schema(type=types.Type.STRING),
          ),
      },
      required=["file_path"],
  ),
)