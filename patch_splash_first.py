#!/usr/bin/env python3
from pathlib import Path
import sys

OFF1 = 20480
OFF2 = 7798784
SLOT = OFF2 - OFF1
HERE = Path(__file__).resolve().parent


def main():
    splash = Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/c/Users/comma/rom/work/splash.img")
    bmp = Path(sys.argv[2] if len(sys.argv) > 2 else HERE / "splash_first_1080x2400.bmp")
    out = Path(sys.argv[3] if len(sys.argv) > 3 else splash.with_name("splash_elaina.img"))

    raw = bytearray(splash.read_bytes())
    pic = bmp.read_bytes()
    if pic[:2] != b"BM":
        raise SystemExit("not a BMP: %s" % bmp)
    if len(pic) > SLOT:
        raise SystemExit("bmp too big")
    if raw[OFF1 : OFF1 + 2] != b"BM":
        raise SystemExit("no BMP at offset %s" % OFF1)

    print("splash", splash, "size", len(raw))
    print("new bmp", len(pic), "bytes")
    raw[OFF1 : OFF1 + len(pic)] = pic
    if len(pic) < SLOT:
        raw[OFF1 + len(pic) : OFF2] = b"\x00" * (SLOT - len(pic))
    if raw[OFF2 : OFF2 + 2] != b"BM":
        raise SystemExit("second BMP magic lost")
    out.write_bytes(raw)
    print("wrote", out, out.stat().st_size)


if __name__ == "__main__":
    main()
