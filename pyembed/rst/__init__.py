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

from docutils.parsers.rst import Directive, directives

from pyembed.core import PyEmbed
from pyembed.rst.handler import PyEmbedRstHandler


class PyEmbedRst(object):

    def __init__(self, renderer=None):
        if renderer:
            self.pyembed = PyEmbed(renderer=renderer)
        else:
            self.pyembed = PyEmbed()

    def register(self):
        directive = self.__create_directive()
        directives.register_directive('embed', directive)

    def __create_directive(self):
        embed = PyEmbedRstHandler(self.pyembed).embed

        class PyEmbedRstDirective(Directive):
            required_arguments = 1
            optional_arguments = 0
            option_spec = {
                'max_width': directives.nonnegative_int,
                'max_height': directives.nonnegative_int
            }
            has_content = False

            def run(self):
                return embed(self.arguments, self.options)

        return PyEmbedRstDirective
