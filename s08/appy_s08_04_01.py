#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/05 15:34:31 (CST) daisuke>
#

# importing numpy module
import numpy

# input file name
file_input = 'cmb_cobe.data'

# numpy arrays for storing data
data_freq_kayser = numpy.array ([])
data_intensity   = numpy.array ([])
data_residual    = numpy.array ([])
data_uncertainty = numpy.array ([])
data_galspec     = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading data file
    for line in fh:
        # skip if the line starts with '#'.
        if (line[0] == '#'):
            continue
        # splitting the data
        (freq_kayser_str, intensity_str, residual_str, uncertainty_str,
         galspec_str) = line.split ()
        # conversion from string into float
        freq_kayser = float (freq_kayser_str)
        intensity   = float (intensity_str)
        residual    = float (residual_str)
        uncertainty = float (uncertainty_str)
        galspec     = float (galspec_str)
        # appending data to numpy arrays
        data_freq_kayser = numpy.append (data_freq_kayser, freq_kayser)
        data_intensity   = numpy.append (data_intensity, intensity)
        data_residual    = numpy.append (data_residual, residual)
        data_uncertainty = numpy.append (data_uncertainty, uncertainty)
        data_galspec     = numpy.append (data_galspec, galspec)

# printing extracted data
print (f'Frequency in Kayser:')
print (f'{data_freq_kayser}')
print (f'Intensity in MJy/sr:')
print (f'{data_intensity}')
