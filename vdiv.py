import argparse
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
        r = "{:.1f}".format(r)
        return r

def error_max(vin_ideal, vout_ideal, r1, r2, tol):
    """Worst case scenario error"""
    err0 = abs(vout_ideal - vin_ideal * r1 / (r1 + r2))
    err1 = abs(vout_ideal - vin_ideal * r1 / (r1 + ((1-tol) / (1+tol)) * r2))
    err2 = abs(vout_ideal - vin_ideal * r1 / (r1 + ((1+tol) / (1-tol)) * r2))
    return max((err0, err1, err2))


def main():
    # standard resistor values series
    e12_series = [100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820]
    e24_series = [100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300,
                  330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910]
    e48_series = [100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169,
                  178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301,
                  316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536,
                  562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953]
    e96_series = [100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130,
                  133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174,
                  178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232,
                  237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309,
                  316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412,
                  422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549,
                  562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732,
                  750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976]
    e192_series = [100, 101, 102, 104, 105, 106, 107, 109, 110, 111, 113, 114,
                   115, 117, 118, 120, 121, 123, 124, 126, 127, 129, 130, 132,
                   133, 135, 137, 138, 140, 142, 143, 145, 147, 149, 150, 152,
                   154, 156, 158, 160, 162, 164, 165, 167, 169, 172, 174, 176,
                   178, 180, 182, 184, 187, 189, 191, 193, 196, 198, 200, 203,
                   205, 208, 210, 213, 215, 218, 221, 223, 226, 229, 232, 234,
                   237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 271,
                   274, 277, 280, 284, 287, 291, 294, 298, 301, 305, 309, 312,
                   316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 357, 361,
                   365, 370, 374, 379, 383, 388, 392, 397, 402, 407, 412, 417,
                   422, 427, 432, 437, 442, 448, 453, 459, 464, 470, 475, 481,
                   487, 493, 499, 505, 511, 517, 523, 530, 536, 542, 549, 556,
                   562, 569, 576, 583, 590, 597, 604, 612, 619, 626, 634, 642,
                   649, 657, 665, 673, 681, 690, 698, 706, 715, 723, 732, 741,
                   750, 759, 768, 777, 787, 796, 806, 816, 825, 835, 845, 856,
                   866, 876, 887, 898, 909, 920, 931, 942, 953, 965, 976, 988]

    # resistor orders of magnitude
    r_factors = range(7)

    #argparser
    parser = argparse.ArgumentParser(description='Calculate the resitor values \
            for a voltage divisor.')
    parser.add_argument('vin_ideal', metavar='Vin', type=float, \
            help = 'input voltage (V)')
    parser.add_argument('vout_ideal', metavar = 'Vout', type=float, \
            help = 'output voltage (V)')
    parser.add_argument('-c', dest = 'max_current', \
            type=float, default = 100, help = 'maximum current (mA)')
    parser.add_argument('-e', dest = 'err_tol', type=float, \
            default = 0.5, help = 'tolerated error (V)')
    parser.add_argument('-s', dest = 'e_series', type=str, default = 'e24', \
            choices = ['e12', 'e24', 'e48', 'e48', 'e96', 'e192'], \
            help = 'E series')

    args = parser.parse_args()

    # get desired values
    vin_ideal = args.vin_ideal
    vout_ideal = args.vout_ideal
    err_tol = args.err_tol
    e_series = args.e_series
    max_current = args.max_current

    # get resistor series according to user choice
    if e_series == 'e192':
        r_series = [x / 100.0 for x in e192_series]
        r_tol = 0.005
    elif e_series == 'e96':
        r_series = [x / 100.0 for x in e96_series]
        r_tol = 0.01
    elif e_series == 'e48':
        r_series = [x / 100.0 for x in e48_series]
        r_tol = 0.02
    elif e_series == 'e12':
        r_series = [x / 100.0 for x in e12_series]
        r_tol = 0.10
    else:
        r_series = [x / 100.0 for x in e24_series] # e24 = default series
        r_tol = 0.05

    # compute resistor values
    r_values = []
    for j in r_factors:
        for i in r_series:
            r = i * 10**j
            r_values.append(r)

    # compute combinations
    r_comb_list = []
    for r1 in r_values:
        for r2 in r_values:
            vout = vin_ideal * r1 / (r1 + r2)
            current = 1000 * vout / r1
            error = error_max(vin_ideal, vout_ideal, r1, r2, r_tol)
            if error <= err_tol and current <= max_current:
                r_comb_list.append((format_r(r1),
                                    format_r(r2),
                                    "{0:.2f}".format(vout),
                                    "{0:.6f}".format(error),
                                    "{0:.4%}".format(error / vout_ideal),
                                    "{0:.4f}".format(current)))

    # sort by error
    r_comb_list = sorted(r_comb_list, key=lambda x: x[3])

    # print in a pretty table
    table = texttable.Texttable()

    table.set_deco(texttable.Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't', 'e', 't', 't'])
    table.set_cols_align(['r', 'r', 'r', 'r', 'r', 'r'])

    r_comb_rows = [["R1", "R2", "Vout (V)", "Error (V)", "Error (%)", "Current (mA)"]]
    for tu in r_comb_list:
        r_comb_rows.append(list(tu))

    table.add_rows(r_comb_rows)

    print table.draw()

if __name__ == "__main__":
    main()
