from dask.distributed import Client
from dask import delayed
import time

import numpy as np
import pandas as pd

import dask.dataframe as dd
import dask.array as da
import dask.bag as db

df=dd.read_csv("sitka_weather_07-2014.csv")
df.head()

df.compute()

index = pd.date_range("2021-09-01", periods=2400, freq="1H")
df=pd.DataFrame({"a": np.arange(2400), "b": list("abcaddbe" * 300)}, index=index)
ddf = dd.from_pandas(df, npartitions=10)
ddf

dff.divitions

ddf.partitions[1]

ddf.b

ddf["2021-10-01":"2021-10-09 5:00"]
ddf["2021-10-01":"2021-10-09 5:00"].compute()

ddf.a.mean().compute()
ddf.b.mean().unique().compute()

ddf.dask
