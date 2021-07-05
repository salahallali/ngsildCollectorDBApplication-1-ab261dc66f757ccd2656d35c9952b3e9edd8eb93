import configparser
# Load the parameters from the configuration file (Config.cfg)
cfg = configparser.ConfigParser()
cfg.read('Config.cfg')

# Get Configuration parameters from Configuration file (Config.cfg)
CBhost = cfg.get('ContextBroker', 'host')
CBport = cfg.get('ContextBroker', 'port')
DBname = cfg.get('DataBase','name')
DBhost = cfg.get('DataBase','host')
DBport = cfg.get('DataBase','port')









