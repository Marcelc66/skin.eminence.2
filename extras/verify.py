import xbmc
import xbmcgui
import os.path

dialog      = xbmcgui.Dialog()

VERIFY = '/system/priv-app/networktest/networktest.apk'

if os.path.isfile(VERIFY):
    xbmc.executebuiltin('Skin.SetBool(Verification)')
    xbmc.executebuiltin('PlayMedia(special://skin/tvpmc/videos/tvpmcintro.mp4)')
    if xbmc.getCondVisibility("Skin.HasSetting(TVPLUS.Welcome.Accepted)"):
        xbmc.executebuiltin('ReplaceWindow(home)')
    else:
        xbmc.executebuiltin('ReplaceWindow(1133)')
    
else:
    dialog.ok('TVPlus Media Center Verification','TVPMC Verification Failed![CR]CONTACT XXXXXXX for support')
    xbmc.executebuiltin('Quit')