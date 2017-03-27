import xbmc
import xbmcgui
import os, shutil

dialog      = xbmcgui.Dialog()

SYSTEMPATH          = '/storage/emulated/0/Android/data/com.tvplusmedia.tvpmc/files/.tvpmc'
PACKAGES            = 'addons/packages/'
MASTER              = 'userdata'
WICKEDXXX           = 'userdata/profiles/WICKED XXX'
THUMBS              = 'Thumbnails/'
TEXTURES            = 'Database/Textures13.db'

packages            = os.path.join(SYSTEMPATH,PACKAGES)
masterthumb         = os.path.join(SYSTEMPATH,MASTER,THUMBS)
mastertextures      = os.path.join(SYSTEMPATH,MASTER,TEXTURES)
wickedxxxthumb      = os.path.join(SYSTEMPATH,WICKEDXXX,THUMBS)
wickedxxxtextures   = os.path.join(SYSTEMPATH,WICKEDXXX,TEXTURES)

def deleteall(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def deletefile(file):
    try:
        if os.path.isfile(file):
            os.unlink(file)
    except Exception as e:
        print(e)

confirm = dialog.yesno('Auto-Clean TVPMC Cache', 'Are you sure you want to auto-clean your device?', 'TVPMC will quit once auto-clean is completed.', 'Click OK to confirm.', 'CANCEL', 'OK')

if confirm:
    i = 0
    progress = xbmcgui.DialogProgress()
    progress.create('Auto-Clean', 'Deleting...')
    while i < 1:
        message = "Packages\n" + str(packages)
        progress.update( int(20), "", message, "" )
        deleteall(packages)
        if progress.iscanceled():
            break
        message = "Thumbnails\n" + str(masterthumb)
        progress.update( int(40), "", message, "" )
        deleteall(masterthumb)
        if progress.iscanceled():
            break
        message = "Textures Cache\n" + str(mastertextures)
        progress.update( int(60), "", message, "" )
        deletefile(mastertextures)
        if progress.iscanceled():
            break
        message = "Thumbnails\n" + str(wickedxxxthumb)
        progress.update( int(80), "", message, "" )
        deleteall(wickedxxxthumb)
        if progress.iscanceled():
            break
        message = "Textures\n" + str(wickedxxxtextures)
        progress.update( int(100), "", message, "" )
        deletefile(wickedxxxtextures)
        if progress.iscanceled():
            break
        i = 2
    progress.close()
    if i == 2:
        dialog.ok('Auto-Clean Complete!','Users should quit TVPMC after launching an Auto Clean.','Press OK to Quit.')
        xbmc.executebuiltin('Quit()')
else:
    pass

