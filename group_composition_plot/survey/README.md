## Interactive RSE composition plotter

This is an interactive version of the plot provided by Frank Löffler.

To run you need to install numpy, Dash, dash-bootstrap-components and plotly.

```bash 
pip install numpy dash plotly dash-bootstrap-components
python interactive_RSE_comp_plot.py
```

After running the file dash will tell you an ip address where you GUI will be displayed.
Should the port already be used please change the `dash_port` variable to a new number.

## Hosting

For hosting we package interactive_RSE_comp_plot.py into a Docker image.
We mount a fixed size ext4 formatted file and use it as a volume to store the submissions, to cap the maximum used disk space.

The mountable file, `submissions.volume`, and the mount point, `submissions`, are created and mounted by executing

```
sh create_volume.sh
```

which makes sure to not override an existing file or remount an already mounted file.

We build and run the docker image using Docker Compose.
The file `compose.yaml` describes how to set the container up.
In addition an Nginx container is started that makes sure the survey is accessible under `/survey/` instead of the root path.

To run the survey execute

```
docker compose up -d
```

The survey is then accessible on port 9000 on the host under path `/survey/`.
