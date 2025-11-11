from configparser import ConfigParser
""" UCL environment """
import datetime
import logging
import sys
import yaml

from pprint import pformat
from box import Box

class config_reader():
    def load_config(config_yaml: str):
        """ Load the config yaml file """
        print(f'Load config: {config_yaml}')
        with open(config_yaml, 'r') as stream:
            try:
                # Load yaml file from path
                yaml_dict = yaml.safe_load(stream)
                print('Loaded Yaml Config')
            except yaml.YAMLError as exc:
                print(exc)
                print('Loading config Unsuccessful')
                raise Exception

        return Box(yaml_dict, box_dots=True)


    def derive_config(context, yaml_config):
        config = Box(yaml_config, box_dots=True)
        if 'platform' not in config:
            config['platform'] = {}
        for key, value in context.userdata.items():
            if isinstance(value, str):
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
            config[key] = value
        return config

    def get_ts():
        return str(datetime.datetime.now())


    def pformat(data):
        return pformat(data)