# PI DAY 2023

This repo contains scripts for generating digits of `PI` using the [monte carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method). This is to celebrate [PI day](https://en.wikipedia.org/wiki/Pi_Day) 2023.

## Usage 

The repo contains two scripts
- main.py
- vis.py

main.py is used for calculating PI using python's [random](https://docs.python.org/3/library/random.html) module without any external dependencies. 

Run the script and provide an integer argument to the script. The higher the integer the more accurate your result of `PI` will be.     

```bash
python main.py 10000
```

vis.py gives a visualization of the entire `PI` calculation process using [turtle](https://docs.python.org/3/library/turtle.html). It is significantly slower than the first so avoid giving it large digits. 

It also requires external dependencies to work which are contained in the `requirements.txt` file. It uses [imageio](https://imageio.readthedocs.io/en/stable/index.html) to save create a video of the entire process. [FFMPEG](https://ffmpeg.org/) has to be installed in the host OS for the program to work.

```bash
pip install -r requirements.txt
python vis.py 1000
```
## Resources

The following resources were helpful:

- Daniel Shiffman [#95 coding challenge](https://www.youtube.com/watch?v=5cNnf_7e92Q)
- This [thread](https://python-forum.io/thread-25822.html) from [python-forum](https://python-forum.io/) was helpful to convert turtle canvas to image.