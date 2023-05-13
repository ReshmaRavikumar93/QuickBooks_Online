import os
import configparser

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        URL=config.get('CommonInfo','baseURL')
        return URL

    @staticmethod
    def getEmail():
        Email=config.get("CommonInfo","susername")
        return Email

    @staticmethod
    def getPassword():
        Password = config.get("CommonInfo", "sPassword")
        return Password
