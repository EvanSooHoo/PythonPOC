from rtlsdr import RtlSdr

print('Hello, and welcome to HelloRTL\n')
print('Attempting to instantiate sdr object')
''' #A silly attempt at exception handling because sdr still has a valid error, and ValueError means something else
try:
    sdr = RtlSdr()
    print(sdr)
except ValueError:
    print("CATASTROPHIC ERROR. RTL-SDR NOT DETECTED. ABORT. ABORT.")
'''
#https://pypi.org/project/pyrtlsdr/
sdr.sample_rate = 2.04e6
sdr.center_freq=70e6
sdr.freq_correction = 60
sdr.gain = 'auto'

print(sdr.read_samples(512))
