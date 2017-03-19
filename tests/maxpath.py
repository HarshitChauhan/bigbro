import re

import tests.helper as th

def passes(out, err):
    return all(
        [th.reads(err, '/tmp/foo'),
         th.reads(err, '/tmp/subdir1/foo_symlink'),
         th.mkdirs(err, '/tmp/subdir1/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'),
         th.mkdirs(err, '/tmp/subdir1/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'),
         th.mkdirs(err, '/tmp/subdir1/abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdef_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'),
         th.count_readdir(err, 0),
     ])

needs_symlinks = False
skip_windows = True
