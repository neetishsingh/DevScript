
import subprocess
import os
import sys
try:
    #sas token
    key = '?sp=r&st=2023-09-20T05:07:51Z&se=2023-09-20T13:07:51Z&spr=https&sv=2022-11-02&sr=b&sig=%2Bg%2BeDAVRzy%2BzDCYjJYTDwXaIdt9CLCgKhlxDKA6bslM%3D'

    #define the container name in blob storage
    mycontainer = "reckitt/5000_predictions.parquet"
    exepath = "C:\\Users\\PC\\Desktop\\GIGABI\\DevScript\\azcopy.exe"
    local_directory="C:\\Users\\PC\\Desktop\\GIGABI\\DevScript"
    endpoint="https://orcpocdevuksadls.blob.core.windows.net/"+mycontainer

    myscript=exepath + " copy "  + "\""+endpoint + key + "\"" + " \""+ local_directory + "\" "

    print(myscript)
    subprocess.call(myscript,shell=True)
    
    print(myscript)
    print('Transfer Complete.')

#Exception for exit error
except subprocess.CalledProcessError as e:
     raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

#Exception for EOF error, would be caused by missing token
except EOFError as error:
    print('Error with token')

#When an unexpected error has occured.
except Exception as e:
    print(str(e) + 'Unknown error has occured')
exit(0)