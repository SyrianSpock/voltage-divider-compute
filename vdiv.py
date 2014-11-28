import numpy as np

# standard resistor values
r_values = np.array([1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
                     3.0,3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
                     8.2, 9.1])
# resistor orders of magnitude
r_factors = np.array([0, 1, 2, 3, 4, 5, 6])

# get desired values
vin_ideal = float(raw_input('Input voltage (V): '))
vout_ideal = float(raw_input('Output voltage (V): '))
err_tolerance = float(raw_input('Tolerated error (V): '))

# compute all possible combinations
r_comb_list = []
for i in r_values:
    for j in r_factors:
        for k in r_values:
            for l in r_factors:
                r1 = i * 10**j
                r2 = k * 10**l
                vout_est = vin_ideal * r1 / (r1 + r2)
                error = np.linalg.norm(vout_est - vout_ideal)
                if error <= err_tolerance:
                    r1 = float("{0:.2f}".format(r1))
                    r2 = float("{0:.2f}".format(r2))
                    error = float("{0:.4f}".format(error))
                    error_pct = "{0:.4f}".format(error * 100 / vout_ideal) + '%'
                    r_comb_list.append((r1, r2, error, error_pct))

# sort and print possible combinations
r_comb_list.sort()

for i in r_comb_list:
    print i
