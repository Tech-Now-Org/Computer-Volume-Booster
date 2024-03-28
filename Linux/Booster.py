import sys
import pulsectl

def increase_volume(increase_percent):
    with pulsectl.Pulse('increase-volume') as pulse:
        sink = pulse.sink_list()[0]
        current_volume = sink.volume.value_flat
        target_volume = min(1.0, current_volume + increase_percent / 100)  # Increase by specified percentage
        pulse.volume_set_all_chans(sink, target_volume)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        percentage = float(sys.argv[1])
        increase_volume(percentage)
    else:
        print("Usage: python booster.py <increase_percent>")
