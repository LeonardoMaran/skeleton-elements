import fontforge
import os
import md5
import subprocess
import tempfile
import json
import copy

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
SQUARE_PATH = os.path.join(SCRIPT_PATH, 'square.svg')
OUTPUT_FONT_DIR = os.path.join(SCRIPT_PATH, '..', '..', 'src/fonts')
AUTO_WIDTH = False
KERNING = 0

m = md5.new()

f = fontforge.font()
f.encoding = 'UnicodeFull'
f.design_size = 28
f.em = 512
f.ascent = 448
f.descent = 64

# Import base characters
for char in "0123456789abcdefghijklmnopqrstuvwzxyzABCDEFGHIJKLMNOPQRSTUVWZXYZ_- .,:;/\!/*&'\"|(){}[]":
  glyph = f.createChar(ord(char))
  glyph.importOutlines(SQUARE_PATH)
  glyph.width = 256

font_name = 'skeleton';
m.update(font_name + ';')

fontfile = '%s/skeleton' % (OUTPUT_FONT_DIR)
print fontfile;
build_hash = m.hexdigest()

f.fontname = font_name
f.familyname = font_name
f.fullname = font_name

f.generate(fontfile + '.ttf')

# # Hint the TTF file
subprocess.call('ttfautohint -s -f -n ' + fontfile + '.ttf ' + fontfile + '-hinted.ttf > /dev/null 2>&1 && mv ' + fontfile + '-hinted.ttf ' + fontfile + '.ttf', shell=True)

# WOFF2 Font
subprocess.call('woff2_compress ' + fontfile + '.ttf', shell=True)
