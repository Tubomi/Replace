#import numpy as np
#np.zeros([2,3,4])

import numpy as np
import pandas as pd
def chess(tr,tc,dr,dc,size):
    global mark
    global table
    mark+=1
    count=mark
    if size ==1:
        return
    half =size//2
    if dr<tr+half and dc<tc +half:
        chess(tr,tc,dr,dc,half)
    else:
        table[tr+half-1][tc+half-1]=count
        chess(tr,tc,tr+half-1,tc+half-1,half)
    if dr<tr+half and dc>=tc+half:
        chess(tr,tc+half,dr,dc,half)
    else:
        table[tr+half-1][tc+half]=count
        chess(tr,tc+half,tr+half-1,tc+half,half)
    if dr>=tr+half and dc<tc+half:
        chess(tr+half,tc,dr,dc,half)
    else:
        table[tr+half][tc+half-1]=count
        chess(tr+half,tc,tr+half,tc+half-1,half)
    if dr>=tr+half and dc>=tc+half:
        chess(tr+half,tc+half,dr,dc,half)
    else:
        table[tr+half][tc+half]=count
        chess(tr+half,tc+half,tr+half,tc+half,half)
