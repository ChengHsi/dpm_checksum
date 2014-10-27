#dpm_checksum

disintegrated scripts used to verify dpm checksums


##Example of use:
checking data01 on f-dpmp23

with two filelist named as : data01/f-dpmp23\_data01\_localpath data01/f-dpmp23\_data01\_pnfpath

###1.On local Machines:
`root@f-dpmp23$ bash save_localsum.sh data01/f-dpmp23_data01_localpath`

creates data01/f-dpmp23\_data01\_localsum

###2.On UI:
`xxx@asgc-ui02$ python get_pnf_sum.py data01/f-dpmp23_data01_pnfpath`

creates data01/f-dpmp23\_data01\_pnfsum

###3.Some machine with both file
with files in $PWD/f-dpmp23/data01:

`xxx@asgc-ui02$ python compare.py f-dpmp23/data01`

return three kinds of results: missing, denied, corrupted






