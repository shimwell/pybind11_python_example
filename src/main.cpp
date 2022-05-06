#include <pybind11/pybind11.h>
#include <iostream>
#include <memory>
#include <fstream>
#include <string>

// I would like to include this header file from another package,
// I normalling install the other package with mamba install -c conda-forge dagmc
// The error this makes is below
// in src/main.cpp:10:10: fatal error: DagMC.hpp: No such file or directory
// to reporduce
// pip install .
// python
// import dagmc_volume_finder
#include "DagMC.hpp"
// putting in the full path to the file doesn't help much as these hpp files need other hpp files
// #include "/home/jshimwell/DAGMC/DAGMC/src/dagmc/DagMC.hpp"
// for example this DagMCVersion file is needed by DagMC
// #include "/home/jshimwell/DAGMC/DAGMC/src/dagmc/DagMCVersion.hpp.in"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int volume(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(dagmc_volume_finder, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: dagmc_volume_finder

        .. autosummary::
           :toctree: _generate

           volume
           subtract
    )pbdoc";

    m.def("volume", &volume, R"pbdoc(
        volume two numbers

        Some other explanation about the volume function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
