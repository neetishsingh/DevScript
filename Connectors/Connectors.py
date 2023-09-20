from FileSystem.FileSystem import FileSystem
from ConnectorConfig import ConnectorConfig

class Connector:
    typesofconnectors = ['localfilebypath', 'azure']
    def __init__(self,id,type,configuration:ConnectorConfig,projectid,name="ConnectionX"):
        self.name=name
        self.id=id
        self.type=type
        self.configration=configuration
        self.files=[]
        self.projectid=projectid

    def initializeConnector(self):
        if self.type=='localfilebypath':

            am=FileSystem(self.configration.fileConfig,self.projectid,self.id)
            am.loadFileFromPath()
            self.files.extend([am])
        elif  self.type=="localfilebyfile":
            print("Not yet started")
              


    
    
