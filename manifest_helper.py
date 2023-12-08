import yaml
from pathlib import Path


directory_path = Path('./data')

# Get the list of files in the directory
file_list = [file.name for file in directory_path.iterdir() if file.is_file()]
file_list.sort()

data = {
    "images": [{"name": file_name, "text": "", "menu": ""} for file_name in file_list]
}

# Writing to a YAML file
output_file_path = 'data_manifest-new.yaml'
with open(output_file_path, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

print(f"YAML file '{output_file_path}' generated successfully.")
