import yaml


def load_rules(rules_file='rules.yaml'):
    with open(rules_file, 'r') as file:
        data = yaml.safe_load(file)
        return data['rules']


def scan_resources(resources):
    findings = []
    rules = load_rules()
    
    for res in resources:
        config = res.get("config", {})
        file_info = res.get("file", "Unknown") #defaut value is "Unknown" if file key is not present
        
        for rule in rules:
            if res["type"] == rule["resource_type"]:
                
                attribute = rule["attribute"]
                expected_value = rule["expected_value"]
                operator = rule.get("operator", "equals") #defaut value is "equals" if operator key is not present
                actual_value = get_nested_value(config, attribute)
                is_vulnerable = False
                
                if actual_value is not None:
                    if operator == "equals":
                        is_vulnerable = (actual_value != expected_value)
                    elif operator == "not_equals":
                        is_vulnerable = (actual_value == expected_value)
                    elif operator == "not_contains":
                        is_vulnerable = expected_value not in str(actual_value)
                else:
                    is_vulnerable = True 
                
                if is_vulnerable:
                    desc = rule.get("description", "No description provided.")
                    rem = rule.get("remediation", f"Expected: {expected_value}, Got: {actual_value}")
                    alert_msg = (
                        f"\n[!] VULNERABILITY: {rule['id']}"
                        f"\n -> Location: {file_info} -> {res['name']}"
                        f"\n -> Issue: {rule['message']} (Got: {actual_value})"
                        f"\n -> Why: {desc}"
                        f"\n -> Fix: {rem}"
                        f"\n" + "-"*50
                    )
                    findings.append(alert_msg)
                    
    return findings

def get_nested_value(config, path):
    keys = path.split('.')
    current_data = config
    
    for key in keys:
        if isinstance(current_data, list) and len(current_data) > 0:
            current_data = current_data[0]
            
        if isinstance(current_data, dict):
            current_data = current_data.get(key)
        else:
            return None
            
    return current_data

