# blue-marimo

based on this, testing for the bluesky file test.py
<https://docs.marimo.io/guides/deploying/prebuilt_containers/>

## setup 3 items

both the deps and venv approaches worked to import dodal, but it's the main version
> cannot import name 'panda' from 'dodal.beamlines.i20_1' (/usr/local/lib/python3.13/site-packages/dodal/beamlines/i20_1.py)

### for deps

`pip install git+http://github.com/DiamondLightSource/dodal@i20_1_add_panda_and_motors`

might need to isntall git manutally into the container

### venv ultimately best to handle from the GUI

<https://github.com/marimo-team/marimo/issues/4689>

### need to explore and integration with the blueapi application

<https://docs.marimo.io/guides/deploying/programmatically/?h=auth#dynamic-directory>
