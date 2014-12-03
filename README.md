voltage-divider-compute
=======================

Python script to display all possible voltage divider combinations that can be
used within the constraints fixed through specified parameters.


Usage example
-------------

In a terminal, on Linux, type the following commands to run the script for
example:
```sh
git clone https://github.com/SyrianSpock/voltage-divider-compute.git
cd voltage-divider-compute
git submodule init
git submodule update
python vdiv.py 3.3 1.8 -s e192 -e 0.01 -c 10 -l 10
```

In this example, the __input voltage__ is 3.3V, __output voltage__ is 1.8V.
Then we specify optional arguments: we want to use the e192 series, we tolerate
0.1V error on the __output voltage__, we want 10mA as __maximum current__ and
we only want the script to display 10 possible combinations.

The output should look like:
```sh
 R1      R2     Vout (V)   Error (V)   Error (%)   Current (mA)
===============================================================
180.0   150.0       1.80      0.0082     0.4548%        10.0000
198.0   165.0       1.80      0.0082     0.4548%         9.0909
240.0   200.0       1.80      0.0082     0.4548%         7.5000
246.0   205.0       1.80      0.0082     0.4548%         7.3171
252.0   210.0       1.80      0.0082     0.4548%         7.1429
258.0   215.0       1.80      0.0082     0.4548%         6.9767
336.0   280.0       1.80      0.0082     0.4548%         5.3571
 1.2K    1.0K       1.80      0.0082     0.4548%         1.5000
 1.3K    1.1K       1.80      0.0082     0.4548%         1.4286
 1.3K    1.1K       1.80      0.0082     0.4548%         1.3636
```

For more details refer to the help menu:
```sh
python vdiv.py -h
```


Parameters
----------

You will be asked to enter some parameter values:
* __Input voltage__ is the voltage at the input of the voltage divider in volts
* __Output voltage__ is the voltage wanted at the output in volts
* __Tolerated error__ is the error voltage tolerated on the output in volts
* __E serie__ specifies the E serie (e12, e24, e48, e96, e192) to choose, which defines the possible resistor values as well as their tolerance
* __Maximum current__ is the maximal current allowed through the divider in mA
* __Maximum lines__ is the maximal number of lines displayed

Dependencies
------------

This script uses the `texttable` package.

License
-------

This script is released under the MIT License.
