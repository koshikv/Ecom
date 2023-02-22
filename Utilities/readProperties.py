import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")


class readConfig:
    @staticmethod
    def getapplicationurl():
        url = config.get("common_info", "baseurl")
        return url

    @staticmethod
    def getusename():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common_info", "password")
        return password
