# cluster_attrs_edi
This package provides tools to find the attribute names from limnology data in the edi repository and cluster them.

Download csv-files data on limnology from the edi website  https://portal.edirepository.org/nis/home.jsp
notebook provides step by step on how to crawl the data from the website.
The downloaded files can be found on https://drive.google.com/open?id=14uYij9hGgIg7ybbcJ1Fxs5sAoHsxv835



Installing
To install this package:

First install PyQt5, e.g. using one of the following methods:

If you have Anaconda installed on your machine, then use the following command:

$ conda install pyqt

Otherwise follow the instructions at http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

Then install the package using one of the following methods:

Run the following command:

pip install git+https://github.com/meldhose/cluster_attrs_edi

First clone the package source code using the following command:

$ git clone https://github.com/meldhose/cluster_attrs_edi

Then enter the source code root folder (cluster_attrs_edi) and install the package using the following command:

$ python setup.py install

You can use --prefix to change the destination folder for installing the package (see the help using $ python setup.py --help).

Usage Guide
To use this package, import it by running the following python command:

>>> import cluster_attrs_edi as ca
