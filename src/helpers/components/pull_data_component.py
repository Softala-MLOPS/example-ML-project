# pull_data_component.py
from kfp.v2.dsl import component, Output, Dataset
import pandas as pd

@component(base_image="python:3.10", packages_to_install=["numpy~=1.26.4", "pandas~=1.4.2"])
def pull_data(url: str, data: Output[Dataset]):
    df = pd.read_csv(url, sep=";")
    df.to_csv(data.path, index=False)
