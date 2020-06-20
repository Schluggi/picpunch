#!/usr/bin/python3
from PIL import Image
from argparse import ArgumentParser, ArgumentTypeError
from os.path import isdir, splitext, join as pjoin
from uuid import uuid1


def check_pieces(piec):
    if piec.isdigit() is False or int(piec) <= 0:
        raise ArgumentTypeError("{} is an invalid quality value (it must be between 1 and 100)".format(piec))
    return int(piec)

def check_output_dir(dir):
    if isdir(dir):
        return dir
    raise ArgumentTypeError("No such directory: {} ".format(dir))

def check_percentage(value):
    if value.isdigit() is False or int(value) not in range(1, 101):
        raise ArgumentTypeError("{} is an invalid value (it must be between 1 and 100)".format(value))
    return int(value)

def check_input_file(file):
    try:
        Image.open(file)
    except OSError:
        raise ArgumentTypeError("{} is not an image".format(file))
    return file

def img_crop(img, pieces_x, pieces_y):
    img_width, img_height = img.size
    piece_height = img_height // pieces_y
    piece_width = img_width // pieces_x

    for i in range(0, pieces_y):
        for j in range(0, pieces_x):
            box = (j * piece_width, i * piece_height, (j + 1) * piece_width, (i + 1) * piece_height)
            yield img.crop(box)


parser = ArgumentParser(description='Punches out a grid from an image and renders the results ',
                        epilog='picpunch by Schluggi')
parser.add_argument('-b', '--border', help='cut off X%% of the edges on every image (default: 0)',
                    type=check_percentage, default=0)
parser.add_argument('-i', '--input', help='input image', type=check_input_file, required=True)
parser.add_argument('-o', '--output', help='output directory', type=check_output_dir, required=True)
parser.add_argument('-x', '--pieces-x', help='the amount of pieces in the x-axis', type=check_pieces, required=True)
parser.add_argument('-y', '--pieces-y', help='the amount of pieces in the y-axis', type=check_pieces, required=True)
parser.add_argument('-p', '--prefix', help='the output file prefix (default: output-XXXX-Y.ZZZ)')
parser.add_argument('-q', '--quality', help='render quality in percent (default is 100 which means lossless)',
                    default=100, type=check_percentage)


args = parser.parse_args()


_, file_extension = splitext(args.input)

img = Image.open(args.input)
img_list = img_crop(img, args.pieces_x, args.pieces_y)

if args.prefix:
    prefix = args.prefix
else:
    prefix = 'output-{}'.format(str(uuid1())[:4])

for i, img in enumerate(img_list):
    filename = '{}-{}.{}'.format(prefix, i, file_extension)
    print('Progressing {}...'.format(filename), flush=True, end='')

    img_width, img_height = img.size
    border_width = img_width * args.border / 100
    border_height = img_height * args.border / 100

    img = img.crop((border_width, border_height, img_width-border_width, img_height-border_height))

    if args.quality != 100:
        img.thumbnail((img_width * args.quality / 100, img_height * args.quality / 100), Image.LANCZOS)

    img.save(pjoin(args.output, filename))
    print('done')
