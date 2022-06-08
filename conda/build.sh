#!/bin/bash
set -e
set -x

sudo apt-get --yes install libeigen3-dev

mkdir MOAB
cd MOAB
git clone  --single-branch --branch 5.3.1 --depth 1 https://bitbucket.org/fathomteam/moab.git
mkdir build
cd build
sudo cmake ../moab -DENABLE_HDF5=ON \
                -DENABLE_NETCDF=OFF \
                -DENABLE_FORTRAN=OFF \
                -DENABLE_BLASLAPACK=OFF \
                -DBUILD_SHARED_LIBS=OFF \
                -DCMAKE_INSTALL_PREFIX=/MOAB
sudo make -j
sudo make -j install
sudo cmake ../moab -DENABLE_HDF5=ON \
                -DENABLE_PYMOAB=ON \
                -DENABLE_FORTRAN=OFF \
                -DBUILD_SHARED_LIBS=ON \
                -DENABLE_BLASLAPACK=OFF \
                -DCMAKE_INSTALL_PREFIX=/MOAB
sudo make -j install
cd pymoab
bash install.sh
python setup.py install
# the following rm command appears to remove libraries that are need to use
# pymoab so this has been commented out for now
# rm -rf /MOAB/moab /MOAB/build

cd ..
cd ..
cd ..

mkdir DAGMC
cd DAGMC
git clone --single-branch --branch v3.2.1 --depth 1 https://github.com/svalinn/DAGMC.git
mkdir build
cd build
sudo cmake ../DAGMC -DBUILD_TALLY=ON \
                -DMOAB_DIR=/MOAB \
                -DBUILD_STATIC_EXE=OFF \
                -DBUILD_STATIC_LIBS=OFF \
                -DCMAKE_INSTALL_PREFIX=/DAGMC/
sudo make -j install


cd ..
cd ..

python -m pip install . -vvv
