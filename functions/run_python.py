import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    if file_path.endswith("\\.py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python", abs_full_path]
        if args:
            commands.extend(args)
        completed_process = subprocess.run(
            commands,
            timeout=30,
            cwd=working_directory,
            capture_output=True,
            text=True
        )
        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

    