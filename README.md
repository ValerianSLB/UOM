# UOM

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f2c1140afacf439c8fec00194acdc7db)](https://www.codacy.com/gh/Schlumberger/UOM/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Schlumberger/UOM&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Schlumberger/UOM/?branch=master)
[![Build Status](https://travis-ci.com/Schlumberger/UOM.svg?token=qgnSxUFcykzzPyjostSM&branch=master)](https://travis-ci.com/Schlumberger/UOM)
[![codecov](https://codecov.io/gh/Schlumberger/UOM/branch/master/graph/badge.svg?token=mUH2Yzsxmd)](https://codecov.io/gh/Schlumberger/UOM)
[![CodeQL](https://github.com/Schlumberger/UOM/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Schlumberger/UOM/actions/workflows/codeql-analysis.yml)
[![CircleCI](https://circleci.com/gh/Schlumberger/UOM/tree/master.svg?style=svg)](https://circleci.com/gh/Schlumberger/UOM/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/Schlumberger/UOM/badge.svg?branch=master)](https://coveralls.io/github/Schlumberger/UOM?branch=master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![Coverage Status](https://coveralls.io/repos/github/Schlumberger/UOM/badge.svg?branch=master)](https://coveralls.io/github/Schlumberger/UOM?branch=master)
<!--
## Build package

```sh
pip3 install wheel
python3 setup.py bdist_wheel
``` -->

## What is it?

Python unit of measure (UOM) conversion tool

The conversion factors and unit symbols are based on the Energistics UOM
1.0
(<https://www.energistics.org/energistics-unit-of-measure-standard/>)
extended with a
few extra unit aliases and \"unitless\" particular unit that cannot be converted.

The units are case sensitives.

## Where to get it

The source code is hosted on GitHub at: <https://github.com/Schlumberger/UOM>

Binary installers for the latest released version are available at the Python
Package Index (PyPI).

```sh
pip install uom
```

## Usage

Please find a few examples of possible utilization:

Find conversion factors to be applied to convert from one unit to another

```Python
from uom import conversion_factors

scale, offset = conversion_factors(source='m', target='ft')
```

Convert a value from one unit to another

```Python
from uom import convert_value

print(convert(value=10, source='m', target='ft'))
```

Return the base SI (
<https://en.wikipedia.org/wiki/International_System_of_Units>) unit.
If you are using unit alias you can find the compatible Energistics UOM symbol

```Python
from uom import base_unit, unit_alias

print(base_unit('kft.lbf'))
print(unit_alias('kft.lbf'))
```

If you have suggestions for improvement or you found bugs,
please don't hesitate to put them in the issue list.
