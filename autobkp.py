import zipfile, os


PluginName = 'autobkp'
BackupPath = f'Backup/{PluginName}'
SavePath = 'server/world'


def create_zip(zipname):
    f = zipfile.ZipFile(f'{BackupPath}/{zipname}.zip','w',zipfile.ZIP_DEFLATED) 
    for dirpath, dirnames, filenames in os.walk(SavePath): 
        for filename in filenames: 
            f.write(os.path.join(dirpath,filename)) 
    f.close() 


def on_info(server, info):
    if info.is_player == 1 and info.content.startswith('!!bkp'):
    	server.stop()
    	server.wait_for_start()
    	zipname = f'{info.hour}h{info.min}min{info.sec}'
    	create_zip(zipname)

