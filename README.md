voltage-divider-compute
=======================

Python script to display all possible voltage divider combinations that can be
used within the constraints fixed through specified parameters.

Usage
-----

In a terminal, on Linux, type the following commands to run the script:

```sh
git clone https://github.com/SyrianSpock/voltage-divider-compute.git
cd voltage-divider-compute
python2 vdiv.py
```

Parameters
----------

You will be asked to enter some parameter values:
* __Input voltage__ is the voltage at the input of the voltage divider in volts
* __Output voltage__ is the voltage wanted at the output in volts
* __Tolerated error__ is the error voltage tolerated on the output in volts
* __Resistance tolerance__ is the tolerance on the resistor value as specified by the manufacturer in %
* __Maximum current__ is the maximal current allowed through the divider in mA

Dependencies
------------

This script uses the `texttable` package.

License
-------

This script is released under the MIT License.
