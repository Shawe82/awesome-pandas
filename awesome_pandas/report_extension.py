import pandas as pd
import pandas_profiling
import webbrowser
from funcy import cached_property

PReport = pandas_profiling.ProfileReport

@pd.api.extensions.register_dataframe_accessor("report")
class Report:
    def __init__(self, df: pd.DataFrame):
        self._df = df

    def __call__(self) -> PReport:
        return self.report

    def show_in_browser(self):
        html_file = "output.html"
        self.report.to_file(output_file=html_file)
        webbrowser.open(html_file, new=2)

    @cached_property
    def report(self) -> PReport:
        return self._df.profile_report(style={"full_width": True})
