import sys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def increase_volume(increase_percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    target_volume = min(1.0, current_volume + increase_percent / 100)  # Increase by specified percentage
    volume.SetMasterVolumeLevelScalar(target_volume, None)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        percentage = float(sys.argv[1])
        increase_volume(percentage)
    else:
        print("Usage: python booster.py <increase_percent>")
