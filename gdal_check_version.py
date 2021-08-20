import sys

def main():

    version_num = int(gdal.VersionInfo('VERSION_NUM'))
    if version_num < 1100000:
        sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')

main()