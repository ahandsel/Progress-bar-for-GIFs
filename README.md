# Progress bar for GIFs

A script that helps you catch the end of perfectly-looping GIFs, preventing you from falling into the trap. And yes, It helped save the world!

## Dependencies

We need two image processing libraries of python, [Pillow](https://pillow.readthedocs.io/en/4.1.x/) and [imageio](http://imageio.readthedocs.io/en/latest/installation.html) to manipulate image frames and compose a new GIF.

```python
pip3 install Pillow, imageio
```

## Usage
```
$ python gif2progressBar.py glass.gif
GIF with progress bar created,  progressBar_glass.gif
```

| Before | After |
| --- | --- |
| ![glass.gif](https://github.com/ustundag/Progress-bar-for-GIFs/blob/master/glass.gif?raw=true) | ![progressBar_glass.gif](https://github.com/ustundag/Progress-bar-for-GIFs/blob/master/progressBar_glass.gif) |

## TODOs
- [ ] Optimize the image processing function. The output gif file has a slight slowdown.
