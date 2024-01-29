from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edades_paciente = np.array(data['age'])
promedio_edades = np.mean(edades_paciente)

print(promedio_edades)