voltage-divider-compute
=======================

Python script to display all possible voltage divider combinations that can be
used within the constraints fixed through specified parameters.

Usage
-----

In a terminal, on Linux, type the following commands to run the script for
example:
```sh
git clone https://github.com/SyrianSpock/voltage-divider-compute.git
cd voltage-divider-compute
python2 vdiv.py 3.3 1.8 -s e192 -e 0.01 -c 10 -l 10
```

In this example, the __input voltage__ is 3.3V, __output voltage__ is 1.8V.
Then we specify optional arguments: we want to use the e192 series, we tolerate
0.1V error on the __output voltage__, we want 10mA as __maximum current__ and
we only want the script to display 10 possible combinations.

For more details refer to the help menu:
```sh
python2 vdiv.py -h
```


Parameters
----------

You will be asked to enter some parameter values:
* __Input voltage__ is the voltage at the input of the voltage divider in volts
* __Output voltage__ is the voltage wanted at the output in volts
* __Tolerated error__ is the error voltage tolerated on the output in volts
* __E serie__ specifies the E serie (e12, e24, e48, e96, e192) to choose, which defines the possible resistor values as well as their tolerance
* __Maximum current__ is the maximal current allowed through the divider in mA

Dependencies
------------

This script uses the `texttable` package.

License
-------

This script is released under the MIT License.
