import pandas as pd
import numpy as np
from tqdm import tqdm

# Register the progress_apply method
tqdm.pandas(desc="Hello Medium")


def dummy_func(s):
    return np.abs(s) ** 1 / 2


# Create some random but "large" dataset wiht 10 000 rows.
df = pd.DataFrame(np.random.rand(10000, 10))
result_basic = df.progress_apply(dummy_func, axis=1)

import swifter

result_swifter = df.swifter.apply(dummy_func, axis=1)
result_swifter = df.swifter.progress_bar(True).apply(dummy_func, axis=1)

from time import time

ts = time()
df.swifter.apply(dummy_func, axis=1)
t_swifter = time() - ts

ts = time()
df.apply(dummy_func, axis=1)
t_normal = time() - ts

print(t_normal / t_swifter)
