import numpy as np
import torch
a=np.load('voc12/cls_labels.npy', allow_pickle=True).item()
print(type(a))
print(len(a))
for ket in a.keys():
    print(type(a[ket]))
    print(a[ket].shape)
    print(a[ket])
print(a[0].shape)
a=5