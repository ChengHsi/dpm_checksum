#dpm_checksum
============

disintegrated scripts used to verify dpm checksums

============
##Example of use:
checking data01 on f-dpmp23,
with two filelist readily availble : data01/f-dpmp23_data01_localpath data01/f-dpmp23_data01_pnfpath
============
##On local Machines:
###root@f-dpmp23$ bash save_localsum.sh data01/f-dpmp23_data01_localpath
creates data01/f-dpmp23_data01_localsum
============
##On ui:
###xxx@asgc-ui02$ python get_pnf_sum.py data01/f-dpmp23_data01_pnfpath
creates data01/f-dpmp23_data01_pnfsum
============
##some machine with both file
with files in $PWD/f-dpmp23/data01
###xxx@asgc-ui02$ python compare.py f-dpmp23/data01
return three kinds of results: missing, denied, corrupted






