import dagmc_volume_finder as m

assert m.__version__ == '0.0.1'
assert m.volume('dagmc.h5m') == 3
