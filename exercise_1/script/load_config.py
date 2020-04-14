# Read cofiguration file
file = open(r'exercise_1/config_exercise_1.yaml')
yaml_list = yaml.load(file, Loader=yaml.FullLoader)
yaml_graph_path = yaml_list.get("graph")
yaml_tools = yaml_list.get("tools")
yaml_text = yaml_list.get("text")
yaml_js_path = yaml_list.get("js_file")