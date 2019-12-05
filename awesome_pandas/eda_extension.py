import awesome_pandas.report_extension
import seaborn as sns

df = sns.load_dataset("titanic")
df.report.show_in_browser()