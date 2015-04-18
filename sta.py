"""
sta
Stim/spike triggered average
@author: llerussell
"""
import numpy as np


def STA(signal, events, n_pre, n_post, baseline=False):
    """
    Compute STA

    Parameters
    ----------
    signal
    events
    n_pre
    n_post
    baseline

    Returns
    -------
    avg_trace
    all_traces
    """

    all_traces = np.zeros([len(events), n_pre + n_post])
    # avg_trace = np.zeros([n_pre + n_post])

    for idx, event in enumerate(events):
        all_traces[idx, :] = signal[event-n_pre:event+n_post]

    # n_samples = n_pre+n_post
    # chunk_size = np.arange(n_samples)
    # idx = triggers[:, None] + chunk_size[None, :]
    # all_traces = input_trace[idx]

    avg_trace = np.mean(all_traces, 0)

    return avg_trace, all_traces
