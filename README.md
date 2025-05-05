# Isaac Sim Replicator Tutorial
A Tutorial Repository for Isaac Sim Replicator for Synthetic Data Generation.

## Requirements
Isaac Sim 4.5 installation was tested on Ubuntu 22.04, Nvidia RTX 3060, Cuda 12.4, Python 3.10 and ROS2 Humble.

## Installation
- First, go through the tutorial for Isaac Sim Installation from [here](https://github.com/ArghyaChatterjee/Isaac-Sim-Tutorial).

## Proccedure
### Start Isaac Sim:
```
cd isaacsim
./isaac-sim.sh
```
On the upper left corner, click on `window` and click on `script editor`. Grab the script editor and release it on the down panel where there are other panels like `console`, `content` and `Isaac Sim Assets`. 

### Start the Process:
Here is a demo script for replicator. Paste it inside script editor.
```
import omni.replicator.core as rep

with rep.new_layer():
    # Create camera
    camera = rep.create.camera(position=(0, 0, 500))
    render_product = rep.create.render_product(camera, (1024, 1024))

    # Create objects
    torus = rep.create.torus(semantics=[("class", "torus")], position=(0, -20, 10))
    sphere = rep.create.sphere(semantics=[("class", "sphere")], position=(0, 10, 10))
    cube = rep.create.cube(semantics=[("class", "cube")], position=(10, -20, 10))

    # Trigger per frame
    with rep.trigger.on_frame(num_frames=10):
        rep.modify.pose(
            [torus, sphere, cube],
            position=rep.distribution.uniform((-10, -10, -10), (20, 20, 20)),
            rotation=rep.distribution.uniform((0, 0, 0), (360, 360, 360))
        )
        rep.modify.scale(
            [torus, sphere, cube],
            scale=rep.distribution.uniform(0.1, 8.0)
        )
```

## Resources
- Omniverse Replicator Tutorial: Setup Guide for Synthetic Data Generation [[video]](https://www.youtube.com/watch?v=_a55hAAF27I)
- Isaac Sim Installation & Core Functions | "Hello World" of Omniverse Replicator [[video]](https://www.youtube.com/watch?v=_kzW6yBno6Q)
- Isaac Sim: Replicator - People and Robots [[video]](https://www.youtube.com/watch?v=F3jxzIKAf9M)
- Isaac Sim: Omniverse Replicator - Synthetic Data Generation (Warehouse with palletjacks) [[video]](https://www.youtube.com/watch?v=hk8nQT9Q0CM)
- NVIDIA Omniverse Replicator - Synthetic Data Generation [[video]](https://www.youtube.com/watch?v=oPYjV8R4pCE) 
