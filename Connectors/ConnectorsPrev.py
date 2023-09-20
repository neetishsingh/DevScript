import os
import re

import pandas as pd


class Connector:
    typesofconnectors = ['localfile', 's3', 'gcp', 'azure']

    def __init__(self, type, credentials, name):
        self.type = type
        self.credentials = credentials
        self.isActive = False
        self.dataframe = None
        self.name = name

    def verifyFileCredentials(self):
        typesoffiles = ['csv', 'xlsx', 'parquet', 'json', 'txt']

        pattern = re.compile("^(files://)(.*)(@)(.*)")
        if (pattern.match(self.credentials)):
            typeoffile = self.credentials[8:].split('@')[0]
            locationoffile = self.credentials[8:].split('@')[1]
            if (self.credentials.startswith('files://') and typeoffile in typesoffiles):
                print("File Credentials Verified")
                return os.path.isfile(locationoffile)
        else:
            return False

    def establishConnection(self):
        # choosename

        if (self.type == 'localfile' and self.verifyFileCredentials()):

            # try to find the file. If it exists, set isActive to true else return false.
            # load that file to the dataframe
            typeoffile = self.credentials[8:].split('@')[0]
            locationoffile = self.credentials[8:].split('@')[1]
            if (typeoffile == 'csv'):
                self.dataframe = pd.read_csv(locationoffile)
            elif (typeoffile == 'xlsx'):
                self.dataframe = pd.read_excel(locationoffile)
            elif (typeoffile == 'parquet'):
                self.dataframe = pd.read_parquet(locationoffile)
            elif (typeoffile == 'json'):
                self.dataframe = pd.read_json(locationoffile)
            elif (typeoffile == 'txt'):
                self.dataframe = pd.read_csv(locationoffile, sep="\t")
            else:
                print(
                    "Error: Invalid file type. Please choose from the following: ", self.typesoffiles)
                raise Exception("Invalid file type")

            self.isActive = True
        elif (self.type not in self.typesofconnectors):
            print(self.type)
            print(
                "Error: Invalid connector type. Please choose from the following: ", self.typesofconnectors)
            raise Exception("Invalid connector type")
        elif (self.type == 'localfile' and not self.verifyFileCredentials()):
            print("Error: Invalid credentials or File Not Readable")
            raise Exception("Invalid credentials or format")
        else:
            raise Exception("Unknown Error while connection ")
        

    def removeConnection(self):
        self.isActive = False
        self.dataframe = None
        print("Connection Removed")
