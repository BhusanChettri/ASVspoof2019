#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:05:27 2019
@author: Bhusan Chettri, QMUL


We used the following scripts to perform intervention experiments with zeros on the 
PA tasks post-evaluation of the ASVspoof 2019 challenge.

Details of our ASVspoof 2019 challenge participation and intervention experiments
can be found here:
    
    https://arxiv.org/abs/1904.04589
    
"""

import os
import soundfile as sf

def count_zeros(samples):
    consecutiveZeros=0
    for sample in samples:
        if sample == 0:
            consecutiveZeros+=1
        else:
            break
    return consecutiveZeros
        
def read_audio(audio,removeZeros,removeZerosFromStart):
    '''Read the audio, remove first consecutive block of zeros from start or end or from both '''
                            
    if not os.path.exists(audio):
        print('%s NOT FOUND !!'%(audio))
        return
        
    samples,fs = sf.read(audio)
    
    zeros_at_start=-99 # -99 indicates zero-removal script was not triggered
    zeros_at_end=-99
        
    if removeZeros:
        zeros_at_end=count_zeros(samples[::-1])
        samples=samples[0:len(samples)-zeros_at_end]            
            
    if removeZerosFromStart:
        zeros_at_start=count_zeros(samples)
        samples=samples[zeros_at_start :len(samples)]
                            
    print('Consecutive zeros in start = %d and at end = %d' %(zeros_at_start,zeros_at_end))
        
    return samples, fs
