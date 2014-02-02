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

from pyembed.core import render
from pyembed.rst import PyEmbedRst

from docutils.core import publish_parts

from hamcrest import assert_that, contains_string, equal_to, is_not
import pytest


class DummyRenderer(render.PyEmbedRenderer):

    def render(self, content_url, response):
        return "<p>%s by %s from %s</p>" % \
            (response.title, response.author_name, content_url)


def test_should_get_correct_embedding():
    PyEmbedRst().register()

    embedding = publish_parts(
        '.. embed:: https://twitter.com/BarackObama/status/266031293945503744',
        writer_name='html')['body']

    assert_that(embedding, contains_string('Four more years.'))
    assert_that(embedding, is_not(contains_string('&gt;')))


def test_should_embed_with_custom_renderer():
    PyEmbedRst(DummyRenderer()).register()

    embedding = publish_parts(
        '.. embed:: http://www.youtube.com/watch?v=qrO4YZeyl0I',
        writer_name='html')['body']

    assert_that(embedding, equal_to(
        '<p>Lady Gaga - Bad Romance by LadyGagaVEVO from ' +
        'http://www.youtube.com/watch?v=qrO4YZeyl0I</p>'))
