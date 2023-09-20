from FileSystem.FileSystemConfig import FileSystemConfig
class ConnectorConfig:
    def __init__(self,type:str,fileConfig:FileSystemConfig=None):
        self.type=type
        self.fileConfig=fileConfig
