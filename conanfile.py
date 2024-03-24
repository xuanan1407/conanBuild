from conans import ConanFile, CMake

class MyMQTTProject(ConanFile):
    name = "MyMQTTProject"
    version = "1.0.0"
    license = "MIT"
    author = "An Tram"
    url = "https://github.com/yourusername/mymqttproject"
    description = "A C++ project using Paho MQTT C library"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    requires = "paho-mqtt-c/1.3.8"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["paho-mqtt3c"]