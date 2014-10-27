import json, subprocess

#corrupted_local_pnf = {}
corrupted_local_pnf = []
#with open('f-dpmp23/data09/f-dpmp23_data09corrupted_local_pnf.json', 'r') as file01:
#    corrupted_local_pnf = json.load(file01)
with open('f-dpmp23/data09/f-dpmp23_data09corrupted_pnfname', 'r') as file02:
    for line in file02:
        corrupted_local_pnf.append(line)

def compare_size():
    for pnf_name in corrupted_local_pnf:
        arg = str(pnf_name.rstrip()) + '\n'
        cmd = 'lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/%s'
        command = str(cmd %arg)
        #print string.decode(arg)
        #arg = str(corrupted_local_pnf[local_name]).encode()
        #arg = u"test".encode()
        #print type(arg)
        print command
        #print ('lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/%s' % str(arg))
        subprocess.call(command, shell = True) 
        #subprocess.call("lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/%s" % arg,shell=True) 
        #subprocess.Popen(['lcg-ls', '-l' ,'srm://f-dpm001.grid.sinica.edu.tw/%s' % arg], shell=True)
compare_size()
