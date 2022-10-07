# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

s = pd.Series([1,2,3,np.nan,8,9])
s

daty = pd.date_range("20221007",periods=6)
daty

df = pd.DataFrame(np.random.randn(6,4), index=daty, columns=list("ABCD"))
df

