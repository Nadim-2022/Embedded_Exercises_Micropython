from machine import Pin, ADC
import time
from lib.piotimer import Piotimer
from fifo import Fifo
from filefifo import Filefifo



adc = ADC(26)
sample_rate = 250
samples = Fifo(100)
def read_sample(tid):
    samples.put(adc.read_u16())
    
tmr = Piotimer( mode = Piotimer.PERIODIC, freq = sample_rate, callback = read_sample)
# samples = Filefifo('')
def heart_rate(sample):
    max_peak = 0
    current_peak = 0
    previous_peak = 0
    peaks = []
    #threshold = sum(sample)/len(sample)
    threshold = (min(sample)+max(sample))/2
    for i in range(len(sample)):
        if sample[i] > threshold and sample[i] > max_peak:
            max_peak = sample[i]
            current_peak = i
            
        if sample[i] < threshold:
            if max_peak != 0:
                peaks.append(current_peak)
                #print(max_peak)
                max_peak = 0
    
    #print(peaks)
    for i in range(len(peaks)-1):
        interval_n = (peaks[i+1] - peaks[i])
        if interval_n >= 62.5 and interval_n <=500:
            hr = 60000//(interval_n*4)
            print(hr)
        else:
            return 0
            #print(f"Interval {interval_n} current_peaak {current_peak} max_peak {max_peak}")
    #print(current_peak)
values = []
while True:
    if samples.dropped() > 0:
        raise RuntimeError ('You lost' + str(samples.dropped()) + ' samples')
    while not samples.empty():
        sample = samples.get()
        values.append(sample)
        if len(values) > 750:
            hear_rate = heart_rate(values)
            values = []
        
        #time.sleep(0.2)
        if sample < 0:
            raise ValueError('end of data')




