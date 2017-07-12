Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\Diego SdLC\AppData\Roaming\Spotify\Spotify.exe"
WScript.sleep 500
CreateObject("WScript.Shell").Run("spotify:user:8aller:playlist:4aoBDuMJnk4Oza13a8Fnbo")
WScript.sleep 3000
WshShell.SendKeys " "
