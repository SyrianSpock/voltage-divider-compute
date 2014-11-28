import numpy as np
import texttable

def format_r(r):
    """Resistor values in human readable format"""
    if r >= 1000000:
        r = "{:.1f}M".format(r / 1000000.0)
        return r
    elif r >= 1000:
        r = "{:.1f}K".format(r / 1000.0)
        return r
    else:
        r = "{:.1f} ".format(r)
        return r

def error_max(vin_ideal, vout_ideal, r1, r2, tol):
    err1 = np.absolute(vout_ideal - vin_ideal * (1+tol)*r1 / ((1+tol) * r1 + (1-tol) * r2))
    err2 = np.absolute(vout_ideal - vin_ideal * (1-tol)*r1 / ((1-tol) * r1 + (1+tol) * r2))

    return max((err1, err2))


# standard resistor values
r_series = np.array([1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
                     3.0,3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
                     8.2, 9.1])
# resistor orders of magnitude
r_factors = np.array([0, 1, 2, 3, 4, 5, 6])

# get desired values
vin_ideal = float(raw_input('Input voltage (V): '))
vout_ideal = float(raw_input('Output voltage (V): '))
err_tolerance = float(raw_input('Tolerated error (V): '))
r_tol = float(raw_input('Resistance tolerance (%): '))/100.0
max_current = float(raw_input('Maximum current (mA): '))

# compute resistor values
r_values = []
for i in r_series:
    for j in r_factors:
        r = i * 10**j
        r_values.append(r)

# compute combinations
r_comb_list = []
for r1 in r_values:
    for r2 in r_values:
        vout = vin_ideal * r1 / (r1 + r2)
        error = np.linalg.norm(vout - vout_ideal)
        current = 1000 * vin_ideal / (r1 + r2)
        if error <= err_tolerance and current <= max_current \
                and error_max(vin_ideal, vout_ideal, r1, r2, r_tol) <= err_tolerance:
            r_comb_list.append((format_r(r1),
                                format_r(r2),
                                "{0:.2e}".format(error),
                                "{0:.2%}".format(error / vout_ideal),
                                "{0:.2f}".format(current)))

# sort by error
r_comb_list = sorted(r_comb_list, key=lambda x: x[2])

# print in a pretty table
table = texttable.Texttable()

table.set_deco(texttable.Texttable.HEADER)
table.set_cols_dtype(['t', 't', 't', 't', 't'])
table.set_cols_align(["r", "r", "r", "r", "r"])

r_comb_rows = [["R1", "R2", "Error (V)", "Error (%)", "Current (mA)"]]
for tu in r_comb_list:
    r_comb_rows.append(list(tu))

table.add_rows(r_comb_rows)

print table.draw()
