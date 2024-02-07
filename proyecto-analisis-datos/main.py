from datasets import load_dataset
import numpy as np
import pandas as pd

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

df = pd.DataFrame(data)

df_perecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

promedio_perecidos = df_perecidos.groupby('is_dead')['age'].mean()
promedio_sobrevivientes = df_sobrevivientes.groupby('is_dead')['age'].mean()