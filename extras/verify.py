import xbmc
import xbmcgui
import os.path

dialog      = xbmcgui.Dialog()

VERIFY = '/system/priv-app/NetworkTest/NetworkTest.apk'

if os.path.isfile(VERIFY):
    xbmc.executebuiltin('Skin.SetBool(Verification)')
    xbmc.executebuiltin('PlayMedia(special://skin/tvpmc/videos/tvpmcintro.mp4)')
    if xbmc.getCondVisibility("Skin.HasSetting(TVPLUS.Welcome.Accepted)"):
        xbmc.executebuiltin('ReplaceWindow(home)')
    else:
        xbmc.executebuiltin('ReplaceWindow(1133)')
else:
    xbmc.executebuiltin('ActivateWindow(1156)')