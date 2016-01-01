"""Python Package setup."""
from setuptools import setup


def requirements():
    """Requirement from source."""
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


def readme():
    """Readme from source."""
    with open('README.md', 'r') as f:
        return f.read()

setup(name='uom',
      version='0.1',
      description='Unit of Measure conversion tool',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
      ],
      keywords='uom unit measurement measure energistics oilfield',
      url='http://github.com/schlumberger/UOM',
      author='Velizar VESSELINOV',
      author_email='vvesselinov@slb.com',
      license='BSD',
      packages=['uom'],
      install_requires=requirements(),
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['convert=uom.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
