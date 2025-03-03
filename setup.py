"""Python Package setup."""
from __future__ import absolute_import

from setuptools import setup


def requirements():
    """Requirement from source."""
    with open('requirements.txt', 'r', encoding='utf8') as fil:
        return fil.read().splitlines()


def readme():
    """Readme from source."""
    with open('README.md', 'r', encoding='utf8') as fil:
        return fil.read()


setup(name='uom',
      version='0.5.2',
      description='Unit of Measure conversion tool',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Customer Service',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Information Analysis'],
      keywords='uom unit measurement measure energistics oilfield',
      url='http://github.com/schlumberger/UOM',
      author='Velizar VESSELINOV',
      author_email='vvesselinov@slb.com',
      license='MIT',
      packages=['uom'],
      install_requires=requirements(),
      test_suite='uom.tests',
      entry_points={
          'console_scripts': ['uom_convert_value=uom.cmd_line:cmd_convert',
                              'uom_base_unit=uom.cmd_line:cmd_base_unit'],
      },
      include_package_data=True,
      zip_safe=False)
