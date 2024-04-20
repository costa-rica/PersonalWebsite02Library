import os
from pw_config import ConfigDev, ConfigProd, ConfigWorkstation

match os.environ.get('FSW_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- pw_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- pw_models/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- pw_models/config: Workstation')
    