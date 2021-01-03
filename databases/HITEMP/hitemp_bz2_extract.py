# # =============================================================================
# #   hitemp_bz2_extract.py
# #   R. J. Hargreaves, Center for Astrophysics | Harvard & Smithsonian, DEC 2019
# #   Please visit https://hitran.org/hitemp/ for details on HITEMP files
# # =============================================================================
# #   Usage    : python hitemp_bz2_extract.py <filename.par.bz2> <numin> <numax>
# #   Required : <filename.par.bz2>
# #   Optional : <numin>, <numax>
# #   Example  : python hitemp_bz2_extract.py 05_HITEMP2019.par.bz2 1500.0 2500.0
# # =============================================================================
import sys
import os
import bz2

print('\n  >> Please visit https://hitran.org/hitemp/ for details on HITEMP files' )
print('  >> ---------------------------------------------------------------------' )
# # =============================================================================
# #   CHECK USER SUPPLIED FILENAME AND LIMITS
# # =============================================================================
def filenamecheck(inputname):
    if '.par.bz2' in inputname:
        bz2_fn = inputname
    else:
        print('  !! ERROR:' )
        print('  !! Incorrect file extension, try <filename.par.bz2>' )
        exit()
    return bz2_fn

if len(sys.argv) == 2:
    complete_file = 1  # Used to set arbitrary minimum/maximum file limits
    bz2_fn = filenamecheck(sys.argv[1])
    print('  >> Extracting complete HITEMP line list, this may take a few minutes...' )
    
elif len(sys.argv) == 4:
    complete_file = 0  # Used to set arbitrary minimum/maximum file limits
    bz2_fn = filenamecheck(sys.argv[1])
    try:
        min_val = float(sys.argv[2])
    except ValueError:
        print('  !! ERROR:' )
        print('  !! Minimum wavenumber not a number' )
        exit()
    try:
        max_val = float(sys.argv[3])
    except ValueError:
        print('  !! ERROR:' )
        print('  !! Maximum wavenumber not a number' )
        exit()
    print('  >> Extracting HITEMP line list between '+str(min_val)+' and '+str(max_val)+' cm-1, this' )
    print('  >> may take a few minutes...' )
else:
    print('  !! ERROR:' )
    print('  !! The maximum or minimum wavenumber appears to be missing.' )
    print('  !! To extract full line list, try... ' )
    print('  !!    python hitemp_bz2_extract.py <filename.par.bz2> ' )
    print('  !! Or to extract specified wavenumber range, try...' )
    print('  !!    python hitemp_bz2_extract.py <filename.par.bz2> <numin> <numax>' )
    exit()


# # =============================================================================
# #   READ BZIP2 HITEMP FILE AND EXTRACT LINES WITHIN RANGE
# # =============================================================================
bz_fi    = bz2.BZ2File(bz2_fn, "r")
if complete_file == 1: 
    out_name = bz2_fn[0:-8]+'_all.par'
    min_val =     0.0 # arbitrary minimum file limit
    max_val = 50000.0 # arbitrary maximum file limit
else:
    out_name = bz2_fn[0:-8]+'_'+str(min_val)+'-'+str(max_val)+'.par'
out_file = open(out_name,'w')


line_count         = 0
extract_line_count = 0 
for line in bz_fi:
    nu_val      = float(line[3:15])
    line_count += 1
    if nu_val <= max_val:
        if line_count % 1000 == 0:
            print('  >> Checking lines:'+str('{:9d}'.format(line_count) )+" lines", end='\r') 
        if (nu_val >= min_val):
            extract_line_count += 1
            if b'\r\n' in line[-2:]:  
                out_file.write(line[:-2].decode("utf-8")+'\n' )
            else:  
                out_file.write(line.decode("utf-8") )
    else:
        break
        
bz_fi.close()
out_file.close()

if extract_line_count == 0:
    print('  >> Complete - Saved to file   : '+out_name )
    print('  >> WARNING  - 0 lines extracted' )
    print('  >>          - Please refer to the HITEMP website for line list coverage' )
else:
    print('  >> Complete - Saved to file   : '+out_name )
    print('  >>          - Lines extracted : '+str(extract_line_count) )
        

