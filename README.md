voltage-divider-compute
=======================

Python script to compute all possible voltage dividers combinations that can be
used for the constraints.

Usage
-----

In a terminal, on Linux:

```sh
git clone https://github.com/SyrianSpock/voltage-divider-compute.git
cd voltage-divider-compute
python vdiv.py
```

You will be asked to enter some parameter values:
* __Input voltage__ is the voltage at the input of the voltage divider in volts
* __Output voltage__ is the voltage wanted at the output in volts
* __Tolerated error__ is the error voltage tolerated on the output in volts
