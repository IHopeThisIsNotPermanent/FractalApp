# Jupyter Notebook Function Navigator

This module is intended for complex function navigation, though it is very easy to use it to navigate any function or zoomable image.

#### Controls

- Click And Drag over an area to zoom into it
- Double click to return to the origin
- Scroll to go back to previous selections

#### Screenshots

![Alt Text](screenshots/demogif.gif)

#### Making your own classes

Your class must implement these two functions:

```python
def start(self, x0,y0,x1,y1):
    """Initializes the internal variables.

    Args:
        x0 (float): The left xlim
        y0 (float): The top ylim
        x1 (float): The right xlim
        y1 (float): The bottom ylim
    """

def val(self, Iterations):
    """Get the image of the state after Iterations.

    Args:
        Iterations (int): The number of iterations you wish to do.

    Returns:
        np.array(shape = (Pixel Width, Pixel Height, 3)).astype(int): The image representing the state of the sim.
    """
```

Then you can pass this class as an argument to the frame_class :D

The complex class is an example implementation of a valid class. 

#### Setting up the python environment for Windows

Download Python3.x, where x is at least 9, or if you already have it installed skip this step!

Ensure you have installed virtualenv to that python environment, then using that run:

```bash
python -m venv .\.env
```

Activate the environment

```bash
.env\Scripts\activate
```

Then import the module.

```bash
pip install -e src\jpcf
```
