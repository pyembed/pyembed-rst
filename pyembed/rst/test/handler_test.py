# The MIT License(MIT)

# Copyright (c) 2013-2014 Matt Thomson

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pyembed.rst import PyEmbedRstHandler

from docutils.core import publish_parts
from hamcrest import assert_that, equal_to, has_length
from mock import Mock


def test_should_replace_url_with_embedding():
    generic_embed_test({}, None, None)


def test_should_apply_max_width():
    generic_embed_test({'max_width': 100}, 100, None)


def test_should_apply_max_height():
    generic_embed_test({'max_height': 200}, None, 200)


def test_should_apply_max_width_and_height():
    generic_embed_test({'max_width': 100, 'max_height': 200}, 100, 200)


def test_should_ignore_other_options():
    generic_embed_test({'max_height': 200, 'extra': 'value'}, None, 200)


def generic_embed_test(options, *embed_params):
    pyembed = Mock()
    pyembed.embed.return_value = '<h1>Bees!</h1>'

    handler = PyEmbedRstHandler(pyembed)

    result = handler.embed(['http://example.com'], options)
    assert_that(result, has_length(1))
    assert_that(result[0].astext(), equal_to('<h1>Bees!</h1>'))

    pyembed.embed.assert_called_with('http://example.com', *embed_params)
