from __future__ import (unicode_literals, division, absolute_import, print_function)
import os

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher
from powerline.segments.shell import ShellCwdSegment

@requires_segment_info
class Rainbow(ShellCwdSegment):
	def __call__(self, pl, segment_info, **kwargs):
		seg = super(Rainbow, self).__call__(pl, segment_info, **kwargs)
		val = 0
		for item in seg:
			if (val > 100):
				val = 0
			item['gradient_level'] = val
			item['highlight_groups'] = ['cascading_rainbow']
			val += 5
		return seg

rainbow_segment = with_docstring(Rainbow(), 'hi')
