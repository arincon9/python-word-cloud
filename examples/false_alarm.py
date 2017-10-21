#!/usr/bin/env python
"""
Image-colored wordcloud
=======================

You can color a word-cloud by using an image-based coloring strategy
implemented in ImageColorGenerator. It uses the average color of the region
occupied by the word in a source image. You can combine this with masking -
pure-white will be interpreted as 'don't occupy' by the WordCloud object when
passed as mask.
If you want white as a legal color, you can just pass a different image to
"mask", but make sure the image shapes line up.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'theweeknd.txt')).read()

# read the mask / color image taken from
# Google http://newsroom.mohegansun.com/wp-content/uploads/2016/11/unspecified.jpg
weeknd_coloring = np.array(Image.open(path.join(d, "theweeknd.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="#D91637", max_words=2000, mask=weeknd_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(weeknd_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(weeknd_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()