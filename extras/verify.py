import xbmc
import xbmcgui
import os.path

dialog      = xbmcgui.Dialog()

VERIFY = '/system/priv-app/networktest/networktest.apk'
ALTVERIFY = '~/verify'

if os.path.isfile(VERIFY) or os.path.isfile(ALTVERIFY):
    xbmc.executebuiltin('Skin.SetBool(Verification)')
    xbmc.executebuiltin('PlayMedia(special://skin/tvpmc/videos/tvpmcintro.mp4)')
    if xbmc.getCondVisibility("Skin.HasSetting(TVPLUS.Welcome.Accepted)"):
        xbmc.executebuiltin('ReplaceWindow(home)')
    else:
        xbmc.executebuiltin('ReplaceWindow(1133)')
    
else:
    dialog.ok('TVPMC Verification','TVPMC Verification Failed!')
    xbmc.executebuiltin('Quit')