import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
import scipy.stats as st

chat_id = 287133833 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    x = x[10:-10]
    y = y[10:-10]
    
    a = 0.05
    #H0 - средние равны, x_mean = y_mean
    z_obs, p_val_mean = ztest (y,x,0,usevar='pooled',alternative='smaller')
    


    return (p_val_mean < a)
