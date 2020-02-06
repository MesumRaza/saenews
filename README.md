[![Downloads](https://pepy.tech/badge/saenews)](https://pepy.tech/project/saenews)

# Quickstart

### Installation


Install via pip

```bash
pip install saenews
```

or install a specific version

```bash
pip install saenews==1.1.7
```

### Downloading utilities

#### Update : No need to download from version 1.1.0 - utilites come with the repository itself

The code will assume the fonts are available in the `./fonts/` directory. You can change it by passing `text_font` argument in everyfunction

Download the utilities like fonts and social media icons from https://github.com/dheerajmpai/saenews/raw/master/utils.zip

```bash

wget https://github.com/dheerajmpai/saenews/raw/master/utils.zip
unzip utils.zip

```
# Issues and feature requests

If you find any bug or if you find any feature missing. Raise an issue ![here](https://github.com/dheerajmpai/saenews/issues)


# Example

Download the image you want to modify 

example code to add a title and tagline to the image (Here Image is saved as `image.jpg`)

```python

from saenews.utils import *
title_tagline_news(title='Title',tag_line='Tag Line',input_file='image.jpg')

```

Original Image 

![alt text](http://sae.news/developer_tools/qq.jpg)

Final Image

![alt text](http://sae.news/developer_tools/qq.png)


Installing Python

The package runs on python3 (3.5+). It is recomended to use anaconda if you are on Windows or Ubuntu. Anaconda is a package distributer. It creates "Virtual Environments" and hence safer as it does not alter the core Python installation of the system. Miniconda, as the name says, is a minimal version of anaconda. If you are not a regular user of python use Miniconda.

# Installing Miniconda

https://docs.conda.io/en/latest/miniconda.html

Choose the relevant version (Windows, Linux or Mac)

For Windows : Execute the .exe file.

For Linux :

1. Download the file 
2. Go to the folder you had downloaded
3. Open the terminal
4. Install it with the command `sh <the file name>.sh` (Should look something like `sh Miniconda3-latest-Linux-x86_64.sh`)
5. Accept the Terms and Conditions
6. In the final step when the command asks if you want to initialize. Press `Y` or `yes` (By default it will be `no`). This will prevent you from reinitializing the Miniconda everytime you boot up.
7. Exit the terminal and open it again (Or you can give the command `source ~/.bashrc`.)


# Installing Image editing library

For Windows : Open the Anaconda Prompt.
For Linux : Open Terminal

Install the package using `pip`. `pip` is a package installer (Kind of Software installer you can say). It will download the version that is compatible with your computer and installs it. Essentially it automates the installation process. The user need not care about the manual installation. 

Use the specific version number to get the particular version of the package

`pip install saenews==<version_number>`

As of now the latest version is `1.2.0` so use.

`pip install saenews==1.2.0`

(installation may take 5-10 mins)


# Editing Images

Once the package is installed you can use the package to edit images. (You need the image, obviously). 

With the package you can do the following edits.

1. Adding Logo, twitter, facebook handles etc.
2. Adding border
3. Adding Quotes
4. Adding focus (Shading out unimportant regions, also known as vignette effect)
5. Automatically focus on face.
6. Add Title.
7. Add Tagline.
8. And moreover, if you have `N` images you can just repeatedely do the work with just one additional `for` loop.

## Importing Library

First go to the directory wher you have the image that you want to edit. Then open Python with the command `python`. On Windows you need to do this on the Anaconda Command prompt. On Linux use the terminal.

```
python
```
Check of the package is installed properly. To do this import the library using

```python
import saenews
from saenews.utils import quote, put_quote
```
(The second command checks if the functions are imported or not)

### Putting Twitter and Facebook handles
For namesake I am considering the image name to be `image.jpg`. But change it accordingly.

```python
from saenews.utils import quote, put_quote
put_quote('image.jpg')
```
The final image would be saved in the directory in the format <Current Date and time>.png . It will also be displayed on the terminal. There will be a lot of other intermediate images for references which you can delete.

The current version the default handles are of Awakened Indian. If you need to change them you need to pass additional arguments. Following is an example where I am using the code for sae.news. 

```python
from saenews.utils import put_quote
put_quote('image.jpg', fb_logo='www.sae.news', tw_logo='saenews_')
```

Note that it has also put a border. To remove the border use an argument `border_width=0`'

```python
from saenews.utils import quote, put_quote
put_quote('image.jpg', border_width=0)
```

## Repeating with a `for` loop

Suppose the name of the images are `image1.jpg` , `image2.jpg`, `image3.jpg`, `image4.jpg` we can do all the four at one shot.

```python
from saenews.utils import quote, put_quote

images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg' ]
for i in images:
    put_quote(i, border_width=0)
```
 (There will be 4 images with the date and time of editing with it. The names will also be displayed on terminal.)


## Adding black strip at the bottom 

You can add a black strip at the bottom so you can put an additional quote there.

There is an another argument to control the width of the blackstrip.

black_strip_dims=(left, top, right, bottom)
Where in the place of left, top etc. we need to pass the ratio by which the black strip should be extended out of image. (Examples will make it very clear). 

Suppose the image height is `H` and width is `W`. You can add a black strip at the bottom of with 50% of the height of the current image you will use `0.5` in the fourth place.

i.e 

```python
black_strip_dims=(0,0,0,0.5)
``` 

This will add an addition black strip at the bottom of height `0.5*H`. 





======================================================================================================
Below are Unedited
======================================================================================================

### Features

### Updates

### Bugfixes

Do Visit our website <a href="https://sae.news"> SAE NEWS</a>

