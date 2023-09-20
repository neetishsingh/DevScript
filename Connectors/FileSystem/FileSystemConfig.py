class FileSystemConfig:

    def __init__(self,loadtype='path',filepath=None,name='FileName1',fileformat='.txt'):
        #loadtype=path if you want to fetch file from a path
        #loadtype=file if you want to have file directly via api
        self.loadtype=loadtype
        self.name=name
        self.filepath=filepath
        self.fileformat=fileformat
