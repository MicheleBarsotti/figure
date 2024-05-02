import numpy as np
import pandas as pd
from typing import List, Dict, Sequence, Optional, Union, Literal, Tuple
from numpy.typing import NDArray
from pathlib import Path
import matplotlib.pyplot as plt


def best_row_column_number(n: int) -> Tuple[int, int]:
    """
    Returns the best number of rows and columns for neatly displaying 'n' plots.

    Args:
        n (int): Total number of items (desired number of subplots).

    Returns:
        Tuple[int, int]: Number of rows and number of columns required to show 'n' plots.
    """
    best_ratio = float("inf")
    best_rows = best_cols = 1

    for rows in range(1, int(np.sqrt(n)) + 1):
        cols = np.ceil(n / rows)
        ratio = cols / rows

        if ratio < best_ratio and rows * cols >= n:
            best_ratio = ratio
            best_rows, best_cols = rows, cols

    return int(best_rows), int(best_cols)


def plot_lines_subplots_first_all(
    x_y_l: List[Tuple], title: str = "plot", show: bool = True
):
    n_lines = len(x_y_l)
    fig, axx = plt.subplots(n_lines + 1, sharex=True)
    colors = [None] * n_lines
    axx[0].text(0, 1.1, s=title, transform=axx[0].transAxes)
    for en, (xx, yy, ll) in enumerate(x_y_l):
        ln = axx[0].plot(xx, yy, label=ll)
        colors[en] = ln[0].get_color()
        axx[0].legend(loc="upper left")
        axx[0].grid()

    for en, ax in enumerate(axx[1:]):
        ax.plot(
            x_y_l[en][0], x_y_l[en][1], marker="*", label=x_y_l[en][2], color=colors[en]
        )
        ax.legend(loc="upper left")
        ax.grid()
    if show:
        plt.show()
    return axx


def plot_chan_ts_matrix_on_ax(
    eeg: np.ndarray,
    timestamp: Optional[np.ndarray] = None,
    std_bias: float = 5,
    ch_names: list = [],
    ax: Optional[plt.Axes] = None,
):
    """plot_chan_ts_matrix_on_ax _summary_

    Args:
        eeg (np.ndarray): 2D array with [N x T] with N=#Channels and T=#Timestamps
        timestamp (np.ndarray): time vector of len T. If None np.arange is created. Defaults to None.
        std_bias (float, optional): Bias between channels in terms of
          multiplicative factor to the global std of the matrix. Defaults to 5.
        ch_names (list, optional): channel names (displayed on y axis). Defaults to [].
        ax (Optional[plt.Axes], optional): Axes. If None a new one is created. Defaults to None.
    """
    if timestamp is None:
        timestamp = np.arange(eeg.shape[-1])
    if ax is None:
        fig, ax = plt.subplots()
    stdd = np.mean(np.std(eeg, axis=1)) * std_bias
    if ch_names:
        assert len(ch_names) == eeg.shape[0]
    else:
        ch_names = np.arange(eeg.shape[0])
    ytick_new = []
    ytick_lab = []
    for en, (ch, chlab) in enumerate(zip(eeg, ch_names)):
        ax.plot(timestamp, ch + en * stdd, linewidth=0.8)
        ytick_new.append(en * stdd)
        ytick_lab.append(str(chlab))
    ax.set_yticks(ytick_new)
    ax.set_yticklabels(ytick_lab)        


def plot_yy(
    ax: plt.Axes,
    ts: np.ndarray,
    y1: list,
    y2: list,
    ylab1: str = "ylab1",
    ylab2: str = "ylab2",
    labels1: Optional[list] = None,
    labels2: Optional[list] = None,
    show_legend: bool = True,
) -> tuple:
    """Double y-axis plot. Only 1 time stamp is supported.

    Args:
        ax (plt.Axes): axis to be twin-x
        ts (np.ndarray): time stamps
        y1 (list): list of np.ndarray to be plot in the first ax
        y2 (list): list of np.ndarray to be plot in the second ax
        ylab1 (str, optional): ylabel left. Defaults to "ylab1".
        ylab2 (str, optional): ylabel right. Defaults to "ylab2".
        labels1 (list, optional): list of labels for y1 (same len of y1). Defaults to None.
        labels2 (list, optional): list of labels for y2 (same len of y2). Defaults to None.

    Returns:
        axtw, lines: the twin axes and the list for all plotted lines
    """
    if labels1 is None:
        labels1 = [None for _ in range(len(y1))]
    if labels2 is None:
        labels2 = [None for _ in range(len(y1))]
    assert len(labels1) == len(y1), "different number of labels and signals"
    assert len(labels2) == len(y2), "different number of labels and signals"

    axtw = ax.twinx()
    lines_count = 0
    color_left = "C0"

    lines1 = []
    for yy, lab in zip(y1, labels1):
        lines1.append(ax.plot(ts, yy, color=f"C{lines_count}", label=lab))
        lines_count += 1
    ax.set_ylabel(ylab1, color="C0")
    ax.tick_params(axis="y", color="C0", labelcolor="C0")
    # # # manage the twin x
    color_right = f"C{lines_count}"
    lines2 = []
    for yy, lab in zip(y2, labels2):
        lines2.append(axtw.plot(ts, yy, color=f"C{lines_count}", label=lab))
        lines_count += 1
    axtw.set_ylabel(ylab2, color=color_right)
    axtw.tick_params(axis="y", color="C1", labelcolor=color_right)
    axtw.spines["right"].set_color(color_right)
    axtw.spines["left"].set_color(color_left)
    lines = [l[0] for l in lines1 + lines2]
    if show_legend:
        axtw.legend(lines, labels1 + labels2)
    return axtw, lines


def plot_dict(diz: dict, ts, max_sb: int = 12, fig_title="", fig_size: tuple = (12, 7)):
    """Take a dictionary and plot all keys in different axes

    If more than max_sb axes are reached another figure will be created

    Args:
        diz (dict): Dict with a np.ndarray of size (N, ) each
        ts (np.ndarray): time stamp vector (size (N, ))
        max_sb (int, optional): Max number of subplots. Defaults to 12.
        fig_title (str, optional): Title for the figure(s). Defaults to "".
        fig_size (tuple, optional): Size of each figure. Defaults to (12, /=

    Returns:
        [type]: [description]
    """

    def _adjust_subplots_fig():
        plt.tight_layout()
        plt.subplots_adjust(hspace=0.0)

    fig_size = (12, 7)
    fig, axx = plt.subplots(max_sb, 1, sharex=True, figsize=fig_size)
    sb_count = 0
    fig_count = 0
    all_fig = [fig]
    all_axx = axx
    for key in list(diz.keys()):
        if sb_count >= max_sb:
            _adjust_subplots_fig()
            fig, axx = plt.subplots(max_sb, 1, sharex=True, figsize=fig_size)
            all_fig.append(fig)
            sb_count = 0
            all_axx = np.concatenate((all_axx, axx))
        if sb_count == 0:
            axx[sb_count].text(
                0,
                1.1,
                f"{fig_title}-{fig_count}",
                transform=axx[sb_count].transAxes,
            )
            fig_count += 1
            axx[sb_count].set_xlim((ts[0], ts[-1] + 1))
        axx[sb_count].plot(ts, diz[key], label=key)
        axx[sb_count].legend(loc="right")
        axx[sb_count].set_ylim((np.nanmin(diz[key]), np.nanmax(diz[key])))
        sb_count += 1
    _adjust_subplots_fig()
    return all_axx, all_fig
