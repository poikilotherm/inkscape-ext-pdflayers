#!/usr/bin/env python

from setuptools import setup

# The get_description function takes the local README.md and adds on the
# local icon.svg to the bottom of the string, this is then recovered
# later for display within the extension manager.


# from inkman.utils import get_description

setup(
    # Give your extension a good and unique name.
    name='inkscape-ext-pdflayers',

    # Your version should reflect the maturity of your extension
    # as well as optionally be linked to the version of a dependnant package
    #
    # 0.1 - 0.3 : Alpha level, expected to fail
    # 0.4 - 0.8 : Beta level, some functionality is expected to fail
    #       0.9 : Pre-release level, everything should work, just fixing some things
    #       1.0 : Finished thing, all the features are working, all non working items
    #             have been removed.
    #       2.0 : The next version or release after 1.0
    #
    version='0.1',

    # This is the short summary which appears below the name in the extensions manager.
    # Try not to make this too long, use the long-description (in README.md).
    description='Write layered SVG images as multipage PDF.',

    # This shouldn't be changed
    #long_description=get_description(__file__),

    url='https://github.com/poikilotherm/inkscape-ext-pdflayers',
    author='Oliver Bertuch',
    author_email='oliver@bertuch.eu',

    # Licenses, see classifiers
    license='GPLv3',

    # Make sure to include all the inx files, place the in the inx directory
    data_files=[('inx', ['inkscape-ext-pdflayers.inx'])],

    # Include any of the extension scripts, remember they will end up in the
    # bin directory of the deployment. So:
    # ~/.config/inkscape/extensions/bin/my-extension.py
    # Which will be referenced in the inx file as bin/my-extension.py
    scripts=['inkscape-ext-pdflayers.py'],

    # Some extensions are more than just a script; the include python module
    # these modules are specified here, they get installed into the directory
    # ~/.config/inkscape/extensions/lib/python3.5/site-packages/
    # And should be available to your scripts after importing inkpath
    packages=[],

    # If modules (above) also include non-python files, such as images
    # and other data. Then this should be set to True.
    # Make sure the module data is included in the MANIFEST.in file.
    include_package_data=False,

    classifiers=[
        # These are REQUIRED for this to be detected as a valid inkscape extension
        'Environment :: Plugins',
        'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',

        # These are optional and depend on your requirements
        'Intended Audience :: Other Audience',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    python_requires='>=3.5',
    install_requires=[
        'PyPDF2==1.27.9'
    ],
)
