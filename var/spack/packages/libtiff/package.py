from spack import *

class libtiff(Package):
    """libtiff graphics format library"""
    homepage = "http://www.remotesensing.org/libtiff/"
    url      = "http://download.osgeo.org/libtiff/tiff-4.0.3.tar.gz"

    version('4.0.3', '051c1068e6a0627f461948c365290410')

    depends_on('jpeg')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)

        make()
        make("install")
