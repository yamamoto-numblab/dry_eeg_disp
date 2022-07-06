from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt
import mne
from mne_realtime import LSLClient
import numpy as np

wait_max = 5
info = mne.create_info(ch_names = ['F7','Fp1', 'Fp2', 'F8','F3', 'Fz', 'F4', 'C3', 'Cz', 'P8', 'P7', 'Pz','P4', 'T3', 'P3', 'O1','O2', 'C4', 'T4'], \
                      sfreq=500, ch_types="eeg")
_, ax = plt.subplots(figsize=(10,8))
with LSLClient(host="myuid323458", info=info, wait_max=wait_max) as client:
    client_info = client.get_measurement_info()
    sfreq = int(client_info['sfreq'])
    print(client_info)
    plt.cla()
    epoch = client.get_data_as_epoch(n_samples=500)
    epoch.average().plot(axes=ax)
    epoch.plot_psd(fmax=250)
    plt.show()