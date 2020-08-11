#
# 'Scale and convert images using PIL'
# A final project for 'Automating Real-World Tasks with Python'
#
# Oliver Frolovs, 2020
# This is free and unencumbered software released into the public domain.

# Design constraints:
#   * Assume file extension matches file format.
#   * Assume no subdirectories. They get ignored.
#   * Actually, a subdirectory with a name ending in .tiff would crash the script.
#   * Assume no extra files in the source directory. They get ignored.
#   * Don't assume source file extension is in lower case.
#   * Preserve the file name case as is but new extension is in lower case.

# The test images are in the 'images_test' directory
#
# Generated test images (JPG, 192x192):
# https://picsum.photos/seed/olliefr/192
# https://picsum.photos/seed/ofr/192
# https://picsum.photos/seed/gruffalo/192
# https://picsum.photos/seed/mouse/192
#
# Converted them to TIFF using Image Converter
# https://www.microsoft.com/en-us/p/image-converter/9pgn31qtzq26


import os
import os.path
import sys

from PIL import Image

# Directory with the source images
src = 'data/'

# Expected format of the source image
src_img_fmt = 'tiff'

# Expected size of the source image
src_img_size = (192,192)

# Directory with the target images
dst = src[:]

# Format of the target image
dst_img_fmt = 'jpg'

# Size of the target image
dst_img_size = (128,128)


# Run!
if __name__ == '__main__':

  # Either both src and dst directories are set,
  # or src == dst is set,
  # or default src == dst == 'data/' is assumed
  if len(sys.argv) == 3:
    dst = sys.argv[-1]
    src = sys.argv[-2]
  elif len(sys.argv) == 2:
    src = sys.argv[-1]
    dst = src[:]

  # OK to terminate if listdir fails
  for src_img_file in os.listdir(src):
    if src_img_file.lower().endswith('.' + src_img_fmt):
      # not OK to fail, report failed file name and exception
      try:
        img = Image.open(os.path.join(src, src_img_file))

        # Rotate clockwise by 90 degrees
        img_new = img.rotate(-90)

        # Resize if applicable. Print warning otherwise and skip resizing
        if img.size != src_img_size:
          print("Warning: {} is size {} but size {} expected. Resize operation skipped",
            src_img_file, img.size, src_img_size, file=sys.stderr)
        else:
          img_new = img_new.resize(dst_img_size)

        # Save in a target format
        dst_img_file = os.path.basename(src_img_file)[:-(len(src_img_fmt)+1)]
        dst_img = os.path.join(dst, '{}.{}'.format(dst_img_file, dst_img_fmt))
        img_new.save(dst_img)
      except:
        print("Error: ", sys.exc_info())
