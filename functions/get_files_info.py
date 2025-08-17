import os

def get_files_info(working_directory, directory="."):
    abs_full_path = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_full_path.startswith(os.path.abspath(working_directory)):
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        item_list = []
        for item in os.listdir(abs_full_path):
            item_path = f'{abs_full_path}/{item}'
            item_list.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
        return "\n".join(item_list)
    except Exception as e:
        return f'Error listing files: {e}'