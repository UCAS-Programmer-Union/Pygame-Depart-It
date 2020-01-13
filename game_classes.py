import pygame
import json

import color as clr

with open("config.json") as config_json:
    configs = json.load(config_json)