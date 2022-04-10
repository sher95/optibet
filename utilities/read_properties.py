import configparser

config = configparser.RawConfigParser()

config.read('../configurations/config.ini')


class read_Config:
    @staticmethod
    def get_url():
        url = config.get('common info', 'codes')
        return url

    @staticmethod
    def get_signing_url():
        url = config.get('common info', 'signing')
        return url
