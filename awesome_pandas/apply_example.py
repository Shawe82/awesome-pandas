import pandas as pd
import numpy as np
from tqdm import tqdm
# Register the progress_apply method
tqdm.pandas(desc="Hello Medium")

# Create some random but "large" dataset wiht 10 000 rows.
df = pd.DataFrame(np.random.rand(10000,10))
result = df.progress_apply(lambda x:np.abs(x)**1/2, axis=1)