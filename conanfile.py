import os
from conans import ConanFile, CMake, tools


class QqqConan(ConanFile):
    name = "qqq"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = [("cmake"), ("cmake_find_package"), ("qt")]

    def export_sources(self):
        self.copy("*")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.run(self.deps_cpp_info["qt"].bin_paths[0] + "/windeployqt.exe bin/qqq.exe")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def configure(self):
        self.options["qt"].shared = True
        self.options["qt"].qtsvg = True
        self.options["qt"].qtdeclarative = True
        self.options["qt"].qttools = True

    def requirements(self):
        self.requires("qt/5.15.2")
        self.requires("boost/1.69.0")

    def package(self):
        self.copy("*", dst="bin", src="bin")
