from lec_3_my_module import earth_mass as em
from lec_3_my_module import gravity_constant as gc
from lec_3_my_module import sigma_steff_bolk as sgm

g = 500 * gc / 10 **2 
print(g)

x = em * gc * sgm
print(x)