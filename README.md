[![Build Status](https://travis-ci.org/amueller/word_cloud.png)](https://travis-ci.org/amueller/word_cloud)
[![licence](http://img.shields.io/badge/licence-MIT-blue.svg?style=flat)](https://github.com/amueller/word_cloud/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/21369/amueller/word_cloud.svg)](https://zenodo.org/badge/latestdoi/21369/amueller/word_cloud)



word_cloud
==========

A little word cloud generator in Python. Read more about it on the [blog
post][blog-post] or the [website][website].
The code is Python 2, but Python 3 compatible.

## Installation

Fast install:

    pip install wordcloud

If you are using conda, it might be even easier to use anaconda cloud:

    conda install -c https://conda.anaconda.org/amueller wordcloud

For a manual install get this package:
    
    wget https://github.com/amueller/word_cloud/archive/master.zip
    unzip master.zip
    rm master.zip
    cd word_cloud-master

Install the package:

    python setup.py install

#### Installation notes

worcloud depends on numpy>=1.5.1, pillow and matplotlib.
To install it via pip, you will also need a C compiler.

##### Windows

If you're having trouble with pip installation on windows, you can find a .whl file at:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

##### Ubuntu

If the installation of the package fails, due to a missing ``pyconfig.h`` file, you need to install the python-dev package. 

For Python 2.*

	sudo apt-get install python-dev
	
For Python 3.*

	sudo apt-get install python3-dev
	
##### CentOS / RHEL

If the compilation via gcc of the package fails, due to a missing ``Python.h`` file, you need to install the python-devel package. 

For Python 2.*

	sudo yum install -y python-devel
	
For Python 3.*

	sudo yum install -y python34-devel

## Licensing
The wordcloud library is MIT licenced, but contains DroidSansMono.ttf, a true type font by Google, that is apache licensed.
The font is by no means integral, and any other font can be used by setting the ``font_path`` variable when creating a ``WordCloud`` object.
