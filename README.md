[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


# Number Guessing Game with Tensorflow

Implement neural network using tensorflow with pygame to predict a drawing of number.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install pygame
pip install Pillow
pip install opencv-python
pip install tensorflow

```

## Usage

```python
import pygame
import sys
import os
from PIL import Image
import numpy
import cv2 as cv
import tensorflow as tf
import tensorflow.python.util.deprecation as deprecation
```
## Instructions

Left click to draw

Right click to erase

E to clear board

## Demo

### Best results

<p align="center">
  <img src="./demo/draw1.png" width="300" height="300">
  <img src="./demo/result1.png" width="320" height="320">

  <img src="./demo/draw0.png" width="300" height="300">
  <img src="./demo/result0.png" width="320" height="320">

</p>
<p align="center">

  <img src="./demo/draw6.png" width="300" height="300">
  <img src="./demo/result6.png" width="320" height="320">

  <img src="./demo/draw8.png" width="300" height="300">
  <img src="./demo/result8.png" width="320" height="320">
</p>

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
