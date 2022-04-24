# picpunch
<a href="https://www.buymeacoffee.com/schluggi" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/white_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>


Punches out a grid from an image and renders the results.

## Requirements
- Python >= 3.0

## Installation
1. Clone this repo
2. Install `pillow`
    ```shell script
    $ pip3 install pillow   
    ```

## Usage
```
usage: picpunch.py [-h] [-b BORDER] -i INPUT -o OUTPUT -x PIECES_X -y PIECES_Y
                   [-p PREFIX] [-q QUALITY]

Punches out a grid from an image and renders the results

optional arguments:
  -h, --help            show this help message and exit
  -b BORDER, --border BORDER
                        cut off X% of the edges on every image (default: 0)
  -i INPUT, --input INPUT
                        input image
  -o OUTPUT, --output OUTPUT
                        output directory
  -x PIECES_X, --pieces-x PIECES_X
                        the amount of pieces in the x-axis
  -y PIECES_Y, --pieces-y PIECES_Y
                        the amount of pieces in the y-axis
  -p PREFIX, --prefix PREFIX
                        the output file prefix (default: output-XXXX-Y.ZZZ)
  -q QUALITY, --quality QUALITY
                        render quality in percent (default is 100 which means
                        lossless)

picpunch by Schluggi
```
### Examples
#### Punch a 4x8 grid (lossless)
```shell script
$ ./picpunch.py -i grid.jpeg -o /tmp/output -x 4 -y 8
```

#### Punch a 7x1 grid (400dpi) for web
```shell script
$ ./picpunch.py -i grid.jpeg -o /tmp/output -x 7 -y 1 -q 30
```

#### Cut off only 5% of the edges (don't punch)
```shell script
$ ./picpunch.py -i grid.jpeg -o /tmp/output -x 1 -y 1 -b 5
```

## Credits
Created and maintained by Schluggi.
