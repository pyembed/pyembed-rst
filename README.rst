PyEmbed-Rst
===============

.. image:: https://secure.travis-ci.org/pyembed/pyembed-markdown.png?branch=master
    :target: http://travis-ci.org/pyembed/pyembed-markdown
.. image:: https://coveralls.io/repos/pyembed/pyembed-markdown/badge.png
    :target: https://coveralls.io/r/pyembed/pyembed-markdown
.. image:: https://pypip.in/v/pyembed-markdown/badge.png
    :target: https://crate.io/packages/pyembed-markdown/
.. image:: https://pypip.in/d/pyembed-markdown/badge.png
    :target: https://crate.io/packages/pyembed-markdown/

Python reStructuredText directive for embedding content using `OEmbed`_.

PyEmbed-Rst allows you to embed content in your reStructuredText websites and
documents from a wide range of producers.  You don't need to configure
anything - the extension automatically discovers how to embed content.

Usage
-----

Initialize the directive like this:

::

    PyEmbedRst().register()

You can then embed content by entering a link with the special text `.. embed::`,
like this:

::

    .. embed:: http://www.youtube.com/watch?v=9bZkp7q19f0

This will be turned into the following HTML:

::

    <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>

Compatibility
-------------

PyEmbed-Rst has been tested with Python 2.7 and 3.3.

Installation
------------

PyEmbed-Rst can be installed using pip:

::

    pip install pyembed-rst

Contributing
------------

To report an issue, request an enhancement, or contribute a patch, go to
the PyEmbed-Rst `GitHub`_ page.

License
-------

PyEmbed-Rst is distributed under the MIT license.

::

    Copyright (c) 2013 Matt Thomson

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. _OEmbed: http://oembed.com
.. _GitHub: https://github.com/pyembed/pyembed-rst