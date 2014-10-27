#dpm_checksum
============

disintegrated scripts used to verify dpm checksums


##Example of use:
checking data01 on f-dpmp23

with two filelist readily availble : data01/f-dpmp23\_data01\_localpath data01/f-dpmp23\_data01\_pnfpath

###1.On local Machines:
`root@f-dpmp23$ bash save\_localsum.sh data01/f-dpmp23\_data01_localpath`

creates data01/f-dpmp23\_data01\_localsum

###2.On UI:
`xxx@asgc-ui02$ python get\_pnf\_sum.py data01/f-dpmp23\_data01\_pnfpath`

creates data01/f-dpmp23\_data01\_pnfsum

###3.some machine with both file
with files in $PWD/f-dpmp23/data01:

`xxx@asgc-ui02$ python compare.py f-dpmp23/data01`

return three kinds of results: missing, denied, corrupted






