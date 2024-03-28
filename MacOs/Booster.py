import AppKit
from Foundation import NSBundle

def increase_volume(increase_percent):
    NSSound = NSBundle.bundleWithPath_('/System/Library/Frameworks/AppKit.framework').classNamed_('NSSound')
    system_sound = NSSound.alloc().initWithContentsOfFile_byReference_('/System/Library/LoginPlugins/BezelServices.loginPlugin/Contents/Resources/volume.aiff', True)
    system_sound.play()
    current_volume = AppKit.NSSound.systemVolume()
    target_volume = min(1.0, current_volume + increase_percent / 100)
    AppKit.NSSound.setSystemVolume_(target_volume)

# Example: Increase volume by 20%
increase_volume(20)
