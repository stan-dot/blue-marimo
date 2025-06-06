import matplotlib.pyplot as plt
plt.ion()

from bluesky import RunEngine
from bluesky.callbacks.best_effort import BestEffortCallback

RE = RunEngine()
bec = BestEffortCallback()
RE.subscribe(bec)

from ophyd.sim import hw
hw = hw()

from bluesky.plans import scan

RE(scan([hw.ab_det], hw.motor, 1, 5, 5))

