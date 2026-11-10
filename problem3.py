import numpy as np
import matplotlib.pyplot as pp

data = np.loadtxt('fismflux20020824.dat', skiprows=1)

# Column 61 is the 56th bin (6 date/time columns + 55)
bin56 = data[:, 61]

# Time of day in hours (columns 3, 4, 5 = hour, minute, second)
time = data[:, 3] + data[:, 4]/60 + data[:, 5]/3600

    
pp.figure(figsize=(10, 5))
pp.plot(time, bin56, color='red', label='Bin 56')
pp.title('EUV Spectrum Bin 56')
pp.xlabel('Time of day (hours)')
pp.ylabel('Irradiance(W/m$^2$/nm)')
pp.legend()
pp.savefig('problem3.png', dpi=300)
