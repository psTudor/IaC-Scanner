import os
import hcl2

def parse_terraform(file_path):
    resources_list = []
    
    with open(file_path, 'r') as file:
        data = hcl2.load(file)
    
    if 'resource' in data:
        for resource_block in data['resource']:
            for res_type, res_details in resource_block.items():
                for res_name, res_config in res_details.items():
                    normalized_resource = {
                        "type": res_type,
                        "name": res_name,
                        "config": res_config,
                        "file": os.path.basename(file_path)
                    }
                    resources_list.append(normalized_resource)
                    
    return resources_list