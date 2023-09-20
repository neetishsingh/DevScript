from FileSystemConfig import FileSystemConfig
import os
import shutil
from utils.Commonutils import generateRandomHash

class FileSystem:
    def __init__(self,config:FileSystemConfig,projectid,connectorid,id=generateRandomHash()):
        self.id=id
        self.config=config
        self.isFileExists=False
        self.projectid=projectid
        self.connectorid=connectorid
        

    def intitalizeFileSystem(self):
        if(self.config.loadtype=='path'):
            if(os.path.exists(self.config.filepath)):
                self.isFileExists=True
            if(self.isFileExists):
                self.loadFileFromPath()

    def loadFileFromPath(self):
        source=self.config.filepath
        destination='./ProjectDumps/'+self.projectid+"/Connectors/"+self.connectorid+"/Files/"+self.id+"/"
        if(os.path.exists(destination)):
            shutil(source,destination)
        else:
            os.mkdir(destination)
        shutil.copy(source,destination)
















        
        



