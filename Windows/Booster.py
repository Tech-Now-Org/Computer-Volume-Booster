from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def increase_volume(increase_percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    target_volume = min(1.0, current_volume * (1.0 + increase_percent / 100))  # Increase by the specified percentage
    volume.SetMasterVolumeLevelScalar(target_volume, None)

increase_volume(20)  # Increase volume by 20%
