from dodal.beamlines.i20_1 import panda, turbo_slit_x
from dodal.common.beamlines.beamline_utils import wait_for_connection
# from spectroscopy_bluesky.i20_1.plans import single_sweep_plan
from sweep_plan import fly_scan_ts
from bluesky.run_engine import RunEngine

p = panda()
turbo_slit = turbo_slit_x()

for dev in p, turbo_slit:
    await dev.connect(dev)

RE = RunEngine({})
RE(single_sweep_plan.fly_scan_ts(start=0, stop=10, num=11, duration=10.0, motor=turbo_slit, panda=p))

