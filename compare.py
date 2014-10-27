import sys, json, subprocess, os, glob
filename = str(sys.argv[1])
a = str(filename).index('data')
dev_name = str(filename)[a:a+6]
b = str(filename).index('f-dpmp')
serv_name = str(filename)[b:b+8]
path = os.path.abspath(filename)
####declare global variables####
localpath_dict = {}
pnfpath_dict = {}
corrupted_file = []
missing_file = []
denied_file = []
denied_pnf_dict = {}
corrupted_pnf_dict = {}
corrupted_local_dict = {}
corrupted_local_pnf = {}
#savepath = str('/asgc_ui_home/chchao/task_checksum/'+serv_name+'/'+dev_name+'/'+serv_name+'_'+dev_name)
savepath = str(path)+'/'+serv_name+'_'+dev_name + '_'
####functions####
def compare_size():
    for local_name in corrupted_local_pnf:
        subprocces.call("lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/"+localname)

def save_missing_info():
    with open(savepath + 'missing_files', 'w') as FO:
        for file in missing_file:
            FO.write(file)

def save_corrupt_info():
    with open(savepath + 'corrupt_files', 'w') as FO1:
        for file in corrupted_file:
            FO1.write(file)
    with open(savepath + 'corrupted_local_dict.json', 'w') as FO2:
        json.dump(corrupted_local_dict, FO2)
    with open(savepath + 'corrupted_pnf_dict.json', 'w') as FO3:
        json.dump(corrupted_pnf_dict, FO3)
    with open(savepath + 'corrupted_local_pnf.json', 'w') as FO3:
        json.dump(corrupted_local_pnf, FO3)

def save_corrupt_info_extra():
    with open(savepath + 'corrupted_pnfname', 'w') as FO1:
        with open(savepath + 'corrupted_localname', 'w') as FO2:
            for file in corrupted_local_pnf:
                FO2.write(str(file)+'\n')
                FO1.write(str(corrupted_local_pnf[file])+'\n')

def save_denied_info():
    with open(savepath + 'denied_files', 'w') as FO:
        for file in denied_file:
            FO.write(file)
    with open(savepath + 'denied_pnf_dict.json', 'w') as FO2:
        json.dump(denied_pnf_dict, FO2)

def compare():
    os.chdir(path)
    #print os.getcwd()
    #print '\''+ str(savepath)+'*\''
    #print glob.glob('f-dpmp*')
    #print glob.glob('*localpath*')
    with open(glob.glob('*localpath*')[0], 'r') as file1:
        with open(glob.glob('*localsum*')[0], 'r') as file2:
            with open(glob.glob('*pnfsum*')[0], 'r') as file3:
                with open(glob.glob('*pnfpath*')[0], 'r') as file4:

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
                            corrupted_local_pnf[filename] = pnf_filename

def main():
    compare()
    save_corrupt_info()
    save_missing_info()
    save_denied_info()
    save_corrupt_info_extra()

#if __main__=='__main__':
main()
