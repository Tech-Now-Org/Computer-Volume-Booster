import pulsectl

def increase_volume(increase_percent):
    with pulsectl.Pulse('increase-volume') as pulse:
        # Get the default sink (output device)
        sink = pulse.sink_list()[0]
        
        # Get the current volume
        current_volume = sink.volume.value_flat
        
        # Calculate the target volume after increasing by the specified percentage
        target_volume = min(1.0, current_volume + increase_percent / 100)
        
        # Set the new volume
        pulse.volume_set_all_chans(sink, target_volume)

# Example: Increase volume by 20%
increase_volume(20)
