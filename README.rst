=============
web-lookup
=============

-----------
Description
-----------
A command line tool that returns a url's status code to a file called status.txt and to the command line if you enable verbosity.

.. note::
    Can be a single URL or a file with URLs

Installation
============

Clone the project 

.. code-block:: bash

    $ git clone https://github.com/SageHourihan/weblookup.git

Navigate to parent folder

.. code-block:: bash

    $ cd weblookup

Install setup.py with Python

.. code-block:: bash
    
    $ python setup.py install

Usage
=====

After installation run the program.

.. code-block:: bash

    $ weblookup -w https://www.foo.com

or for using a file

.. code-block:: bash

    $ weblookup -f bar.txt

.. note ::
    For additional help and commands run:
.. code-block:: bash
    $ weblookup --help

License
=======

MIT 
