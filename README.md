# Axon 30 Pro splash (first screen)

1080x2400 first boot BMP + patcher for Vertu/ZTE `splash.img` (offset 20480).

## Files

- `splash_first_1080x2400.png` — preview
- `splash_first_1080x2400.bmp` — 24-bit, drop into splash.img
- `patch_splash_first.py` — replaces only the first BMP

## WSL

```bash
python3 patch_splash_first.py \
  /mnt/c/Users/comma/rom/work/splash.img \
  splash_first_1080x2400.bmp \
  /mnt/c/Users/comma/rom/work/splash_elaina.img
```

Then: `fastboot flash splash splash_elaina.img`
