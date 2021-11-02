import os
import sys

base_path = os.path.dirname( os.path.abspath(__file__))
config_path = os.path.join(base_path, "Config.ini")

print(base_path)
print(config_path)
if os.path.exists(config_path):
    cfg = configparser.ConfigParser()
    cfg.read(config_path)
else:
    print("Config File not cound!")
    sys.exit()
