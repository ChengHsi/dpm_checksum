import sys, json
filename = str(sys.argv[1])
a = str(filename).index('data')
dev_name = str(filename)[a:a+6]
b = str(filename).index('f-dpmp')
serv_name = str(filename)[b:b+8]

####declare global variables####
localpath_dict = {}
pnfpath_dict = {}
corrupted_file = []
missing_file = []
denied_file = []
denied_pnf_dict = {}
corrupted_pnf_dict = {}
corrupted_local_dict = {}
savepath = str('/asgc_ui_home/chchao/task_checksum/'+serv_name+'/'+dev_name+'/'+serv_name+'_'+dev_name+'_selected_')

####functions####
def save_missing_info():
    with open(savepath + '_missing_files', 'w') as FO: 
        for file in missing_file:
            FO.write(file)
def save_corrupt_info():
    with open(savepath + '_corrupt_files', 'w') as FO1:
        for file in corrupted_file:
            FO1.write(file)
    with open(savepath + 'corrupted_local_dict.json', 'w') as FO2:
        json.dump(corrupted_local_dict, FO2)    
    with open(savepath + 'corrupted_pnf_dict.json', 'w') as FO3:
        json.dump(corrupted_pnf_dict, FO3)
def save_denied_info():
    with open(savepath + '_denied_files', 'w') as FO:
        for file in denied_file:
            FO.write(file)
    with open(savepath + 'denied_pnf_dict.json', 'w') as FO2:
        json.dump(denied_pnf_dict, FO2)



with open(savepath+'_localpath', 'r') as file1:    
    with open(savepath+'_localsum', 'r') as file2:
        with open(savepath+'_pnfsum', 'r') as file3:
            with open(savepath+'_pnfpath', 'r') as file4:
 
                for checksum, filename, pnf_sum, pnf_filename in zip(file2, file1, file3, file4):       
                    checksum = str(checksum.rstrip())
                    filename = str(filename.rstrip())
                    pnf_sum = str(pnf_sum.rstrip())
                    pnf_filename = str(pnf_filename.rstrip())
                    localpath_dict[checksum] = filename
                    pnfpath_dict[pnf_sum] = pnf_filename

                    if (pnf_sum == "file not found" or checksum == "Error_ac"):
                        print "file missing on server or disk: " + pnfpath_dict[str(pnf_sum)]
                        missing_file.append(pnf_sum+" "+pnf_filename+"\n"+checksum+" "+filename+"\n\n")
                    elif pnf_sum == "no checksum":
                        print "cannot get checksum(denied?):"+ pnfpath_dict[str(pnf_sum)]
                        denied_file.append(pnf_sum+" "+pnf_filename+"\n"+checksum+" "+filename+"\n\n")
                        denied_pnf_dict[pnf_filename] = pnf_sum    
                    elif (pnf_sum != checksum):
                        print "corrupted file: " + pnfpath_dict[str(pnf_sum)] + " local checksum: " + checksum + " Server checksum " + pnf_sum
                        corrupted_file.append(pnf_sum+" "+pnf_filename+"\n"+checksum+" "+filename+"\n\n")
                        corrupted_pnf_dict[pnf_filename] = pnf_sum
                        corrupted_local_dict[filename] = checksum
                save_corrupt_info()
                save_missing_info()
                save_denied_info()
