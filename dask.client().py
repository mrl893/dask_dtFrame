from dask.distributed import Client
from dask import delayed
import time

def f(x):
    time.sleep(x)
    return x
if __name__ == "__main__":
    client = Client()
    res=[]
    for x in [1,2,3,4]:
        f_ = delayed(f)(x)
        res.append(f_)
    sum_=delayed(sum)(res)
    print(sum_.compute())
    client.dashboard_link
