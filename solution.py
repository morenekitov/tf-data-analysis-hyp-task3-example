import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
import scipy.stats as st

chat_id = 287133833 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    x = x[:-5]
    y = y[:-5]
    
    a = 0.05
    #H0 - средние равны, x_mean = y_mean
    _, p_krusk = st.kruskal(y,x)



    if p_krusk<a:
        print('Крускалл: ', p_krusk)
        t_val, p_stud = st.ttest_ind(y,x,alternative='less',equal_var=False)
        print(t_val, p_stud)
        return p_stud < a
    else:
        return False
