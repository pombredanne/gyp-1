#!/usr/bin/env python

"""
Verifies that .hpp files are ignored when included in the source list on all
platforms.
"""

import sys
import TestGyp

# TODO(bradnelson): get this working for windows.
test = TestGyp.TestGyp(formats=['make', 'scons', 'xcode'])

test.run_gyp('assembly.gyp', chdir='src')

test.relocate('src', 'relocate/src')

test.build_all('assembly.gyp', chdir='relocate/src')

expect = """\
Hello from program.c
Got 42.
"""
test.run_built_executable('program', chdir='relocate/src', stdout=expect)


test.pass_test()
