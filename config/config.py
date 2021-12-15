from os import path

import yaml

with open(path.join(path.dirname(__file__), 'config.yaml'), 'r') as yaml_file:
    Config = yaml.safe_load(yaml_file)


def apply_platform(name: str):
    if 'platforms' in Config:
        Config.update(Config['platforms'][name].items())
        del Config['platforms']
