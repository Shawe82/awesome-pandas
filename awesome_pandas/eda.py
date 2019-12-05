import pandas as pd
import pandas_profiling
import webbrowser
import seaborn as sns


def open_report(df: pd.DataFrame):
    report = df.profile_report(style={'full_width': True})
    html_file = "probably-some-unique-file-name.html"
    report.to_file(output_file=html_file)
    webbrowser.open(html_file, new=2)


if __name__ == '__main__':
    df = sns.load_dataset("titanic")
    open_report(df)