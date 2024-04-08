import pickle
import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# stim, neuron1, neuron2, neuron3

stim = data['stim']
neuron1 =  data['neuron1']
neuron2 =  data['neuron2']
neuron3 =  data['neuron3']
neuron4 =  data['neuron4']
r = []

def STA(data, array, trial_num=10, rep_num=24):
    for trial in range(trial_num):  # trial_num = 10
        avg = data[trial] / rep_num
        array.append(avg)
    return avg

def compute_mean(data):
    val = sum(data) / len(data)
    return val

def compute_var(data):
    mean = compute_mean(data)
    arr = []
    for i in range(len(data)):
        arr.append((data[i]-mean)**2)
    var = sum(arr) / len(arr)
    return var

dataset = [neuron1, neuron2, neuron3, neuron4]

for i in range(len(dataset)):
    avg = STA(dataset[i], r)
    mean = compute_mean(avg)
    var = compute_var(avg)
    print(f'For neuron{i}, mean: {mean}, var: {var}')
    r = []

# find the answer according to the stats