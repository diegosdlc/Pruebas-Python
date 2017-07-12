Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\Diego SdLC\AppData\Roaming\Spotify\Spotify.exe"
WScript.sleep 50
CreateObject("WScript.Shell").Run("spotify:user:diegosparrow:playlist:3NolHF4AxA3noA3h3uhAr5")
WScript.sleep 30
WshShell.SendKeys " "
