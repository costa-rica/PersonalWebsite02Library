import os
from pw_config import ConfigWorkstation, ConfigDev, ConfigProd
import logging
from logging.handlers import RotatingFileHandler

match os.environ.get('WS_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- PersonalWebsite02/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- PersonalWebsite02/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- PersonalWebsite02/config: Workstation')

#Setting up Logger
app_name = "PersonalWebsite02Library - pw_tools"
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter = logging.Formatter(f'%(asctime)s - {app_name} - %(name)s - [%(filename)s:%(lineno)d] - %(message)s')

#initialize a logger
logger_pw_tools = logging.getLogger(__name__)
logger_pw_tools.setLevel(logging.DEBUG)

#where do we store logging information
file_handler = RotatingFileHandler(os.path.join(config.DIR_LOGS,'ws_analysis.log'), mode='a', maxBytes=5*1024*1024,backupCount=2)
file_handler.setFormatter(formatter)

#where the stream_handler will logger_pw_tools
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger_pw_tools.addHandler(file_handler)
logger_pw_tools.addHandler(stream_handler)

