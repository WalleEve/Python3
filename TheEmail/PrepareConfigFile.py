import configparser

config = configparser.ConfigParser()

config['user'] = {'user_name': 'Admin',
                  'password': 'Admin'}

with open ("C:\\Users\\Sayed\\Documents\\GitHub\\Python3\\TheEmail\\Config.ini", 'w') as configfile:
    config.write(configfile)
