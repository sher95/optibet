import configparser

config = configparser.RawConfigParser()

config.read("Configurations/config.ini")


class read_Config:
    @staticmethod
    def get_url():
        url = config.get('common info', 'codes')
        return url
