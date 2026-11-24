#!/usr/bin/env python3
"""Ship THE TUESDAY GLOBE front page to the grader's output folder.

The finished page lives beside this file as ``entry.png``. Running
the program:

1. opens that file and walks its PNG chunks one by one, checking
   each chunk's stored CRC against a fresh CRC-32 of its payload,
   and reading the IHDR width and height;
2. refuses to ship anything over the contest limits (1024 x 1024
   pixels, 1 MiB on disk);
3. copies the bytes into the output directory under a scratch
   name, flushes and fsyncs, then renames over ``entry.png`` so a
   reader never sees a half-written page;
4. re-reads the shipped copy and compares length and SHA-256 with
   the original, failing loudly on any difference.

Output directory: ``MAKEFUN_OUTPUT_DIR`` if set, else ``/output``.
No network, no clock, no randomness — every run ships the same
bytes. Standard library only.
"""

import hashlib
import os
import struct
import sys
import tempfile
import zlib
from pathlib import Path

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PAGE = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def walk_png(data):
    """Yield (kind, payload) per chunk; raise ValueError if malformed."""
    if not data.startswith(PNG_MAGIC):
        raise ValueError("missing PNG signature")
    pos = len(PNG_MAGIC)
    saw_iend = False
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError("truncated chunk header")
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        end = pos + 8 + length
        if end + 4 > len(data):
            raise ValueError(f"truncated chunk {kind!r}")
        payload = data[pos + 8:end]
        (stored_crc,) = struct.unpack(">I", data[end:end + 4])
        fresh_crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
        if fresh_crc != stored_crc:
            raise ValueError(f"CRC mismatch in chunk {kind!r}")
        yield kind, payload
        saw_iend = saw_iend or kind == b"IEND"
        pos = end + 4
    if not saw_iend:
        raise ValueError("no IEND chunk")
    if pos != len(data):
        raise ValueError("trailing bytes after IEND")


def page_size(data):
    for kind, payload in walk_png(data):
        if kind == b"IHDR":
            width, height = struct.unpack(">II", payload[:8])
            return width, height
    raise ValueError("no IHDR chunk")


def deliver(source_bytes, out_dir):
    """Write source_bytes to out_dir/entry.png atomically; return its path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / PAGE
    fd, scratch = tempfile.mkstemp(dir=out_dir, prefix=".globe-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(source_bytes)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(scratch, target)
    except BaseException:
        try:
            os.unlink(scratch)
        except OSError:
            pass
        raise
    return target


def main():
    here = Path(__file__).resolve().parent
    source = here / PAGE
    data = source.read_bytes()

    if len(data) > MAX_BYTES:
        print(f"refusing: page is {len(data)} bytes, limit is {MAX_BYTES}", file=sys.stderr)
        return 1
    width, height = page_size(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"refusing: page is {width}x{height}, limit is {MAX_SIDE}x{MAX_SIDE}",
              file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = deliver(data, out_dir)

    shipped = target.read_bytes()
    if len(shipped) != len(data) or hashlib.sha256(shipped).digest() != hashlib.sha256(data).digest():
        print("refusing: shipped copy differs from the source page", file=sys.stderr)
        return 1
    print(f"shipped {PAGE}: {width}x{height}, {len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
