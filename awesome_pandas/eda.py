import numpy as np
import pandas as pd
import awesome_pandas.report_extension
import webbrowser
import seaborn as sns

df = sns.load_dataset('titanic')
report = df.profile_report(style={'full_width':True})
html_file = "output.html"
report.to_file(output_file=html_file)
webbrowser.open(html_file, new=2)