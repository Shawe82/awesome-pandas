import numpy as np
import pandas as pd
import awesome_pandas.report_extension
import webbrowser
import seaborn as sns


def gen_data(n_samples: int) -> pd.DataFrame:
    data = {}
    uncorrelated = np.random.standard_normal((3, n_samples))
    data["normal-1"] = uncorrelated[0, :] + 123.12
    for i, cor in enumerate((0.2, 0.95)):
        L = np.linalg.cholesky([[1, cor], [cor, 1]])
        data[f"normal-1-{i}"] = (
            np.dot(L, uncorrelated[:2, :]) + np.random.rand(2, 1) * 100
        )[1, :]
        data[f"normal-2-{i}"] = (
            np.dot(L, uncorrelated[[0, 2], :]) + np.random.rand(2, 1) * 100
        )[1, :]

    data["log-normal"] = np.random.lognormal(19.45, 4.23, n_samples)
    data["exp"] = np.random.exponential(14.54, n_samples)
    data["exp"][
        np.random.choice(n_samples, int(n_samples * 0.15), replace=False)
    ] = np.nan

    data["rand-ints-1"] = np.random.randint(0, 8, n_samples)
    data["rand-ints-2"] = np.random.randint(4, 100, n_samples)
    data["probs"] = np.random.random(n_samples)
    data["probs"][
        np.random.choice(n_samples, int(n_samples * 0.05), replace=False)
    ] = np.nan

    return pd.DataFrame(data)


if False:
    df = sns.load_dataset("titanic")
    report = df.profile_report(style={"full_width": True})
    html_file = "output.html"
    report.to_file(output_file=html_file)
    webbrowser.open(html_file, new=2)
