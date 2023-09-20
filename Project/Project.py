
from utils.Commonutils import generateRandomHash
import os
import json
from Connectors.Connectors import Connectors,ConnectorConfig


class Project:
    #differnt kind of states
    #new- first time created the project
    #draft- created the project locally and saved at certain instance
    #published-published the report at cloud
    #deactivated-report is published but not active so will not eat ram
    #deleted- deleted from cloud and local as well


    #except new Project JSON will come in all cases

    def __init__(self,projectName,connectors:list(Connectors),projectId=generateRandomHash(),projectstate="new",ProjectJSON={}):
            self.ProjectName=projectName
            self.connectors=connectors
            self.ProjectId=projectId
            self.Projectstate=projectstate
            self.ProjectJSON=ProjectJSON
            self.initializeProjectComponents()
            self.connectors=[]
            
            
    def getProjectPath(self):
         return './ProjectDumps/'+self.ProjectId
    
    def createProjectFolder(self):
        newpath = './ProjectDumps/'+self.ProjectId
        
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    def checkifProjectFolderExists(self):
        newpath = './ProjectDumps/'+self.ProjectId
        
        if os.path.exists(newpath):
            return True
        return False  
    
    def createConfigFile(self):
        
        with open(self.getProjectPath()+'/data.json', 'w', encoding='utf-8') as f:
            json.dump(self.ProjectJSON, f, ensure_ascii=False, indent=4)
    
                          
         
    def initializeProjectComponents(self):
         if self.Projectstate=='new':
              self.createProjectFolder()
              self.createConfigFile()
         elif self.Projectstate=='draft':
              if not self.checkifProjectFolderExists:
                   self.createProjectFolder()
                   self.createConfigFile()
              else:
                   self.createConfigFile()        
              #read config from cloud and write it in config
              
         elif self.Projectstate=='published':
              #read config from cloud and write it in config     
              if not self.checkifProjectFolderExists:
                   self.createProjectFolder()
                   self.createConfigFile()
              else:
                   self.createConfigFile()         
         elif self.Projectstate=='deactivated':
              #read config from cloud and write it in config     
              if not self.checkifProjectFolderExists:
                   self.createProjectFolder()
                   self.createConfigFile()
              else:
                   self.createConfigFile()     


    def createContainer(self):
         cf=ConnectorConfig('localfilebypath',File)
         
         
         
                       
                    

         
                        
                        
            




        