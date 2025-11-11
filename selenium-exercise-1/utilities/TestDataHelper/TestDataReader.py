import json
import os

def GetTestDataStringFromJsonFile(file_name, data_set, data_string_ref):
    file_path = GetJsonFilePathFromFileName(file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    if data_set in data:
        given_data_set = data[data_set]
        search_data = given_data_set.get(data_string_ref)
    else:
        print("Dataset {data_set} not found in the JSON.")
    return search_data

def GetTestDataFromJsonFile(file_name, data_set):
    file_path = GetJsonFilePathFromFileName(file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    if data_set in data:
        given_data_set = data[data_set]
    else:
        print("Dataset {data_set} not found in the JSON.")
    return given_data_set

def GetJsonFilePathFromFileName(file_name):
    current_dir = os.path.join(os.path.abspath(os.getcwd()), "features", "testdata")
    for root, dirs, files in os.walk(current_dir):
        for name in files:
            if file_name in name:
                file_path = os.path.abspath(os.path.join(root, name))
    return file_path    

def UpdateJsonFile(file_name, data_set, data_string_ref, new_data_string_value):
    file_path = GetJsonFilePathFromFileName(file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    if data_set in data:
        data[data_set][data_string_ref] = new_data_string_value
    else:
        print("Dataset {data_set} not found in the JSON.")
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4) 

def GetTestDataInputFilePath():
    path = os.path.join(os.path.abspath(os.getcwd()), "features", "testdata", "inputfiles")
    return path

def Get_Env_Var(context, env_variable1, env_variable2 = None):
    env = os.getenv('ENVIRONMENT', 'test')
    if env_variable2 is not None:
        
        #Change hardcoded "test" to which env it runs calling ir from execution 
        variable = context.config.userdata.get(env_variable2) or context.behave_config[env][env_variable1].get(env_variable2, None)
    else:
        variable = context.config.userdata.get(env_variable1) or context.behave_config[env].get(env_variable1, None)
    return variable

def field_present_in_test_data(test_data, key):
    try:
        value = test_data[key]
        if value:
            return True
        else:
            return False
    except KeyError:
        return False