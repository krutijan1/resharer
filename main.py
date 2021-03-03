import pyheif
import click
import os

from os import walk
from PIL import Image

@click.command()
@click.option('--src_format', default='HEIC', help='Select source format to convert to jpeg')
@click.option('--source', prompt='Source folder', help='Source folder in current folder')
@click.option('--target', prompt='Target folder', help='Target folder in current folder')
def converter(src_format, source, target):

    source = os.getcwd() + '/{}/'.format(source)
    target = os.getcwd() + '/{}/'.format(target)

    _, _, filenames = next(walk(source))

    with click.progressbar(filenames,
                       label='Converting photos',
                       length=len(filenames)) as photos:

        for f in photos:
            if src_format in f:
                heif_file = pyheif.read(source + f)
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                    )

                image.save(target + f.split('.')[0] + '.jpg', "JPEG")

@click.group(help="CLI tool to manage full development cycle of projects")
def cli():
    pass

cli.add_command(converter)

if __name__ == '__main__':
    cli()
