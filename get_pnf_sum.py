import sys, subprocess, os
file = sys.argv[1]
path = os.path.abspath(file)
save_path = str(path).replace("pnfpath", "pnfsum")
print 'saving to: ', save_path

with open(str(file), 'r') as file01:
    with open(save_path, 'w') as file02:
        for line in file01:
            command = ['lcg-ls', '-l']
            arguments = [str("srm://f-dpm001.grid.sinica.edu.tw/%s" %line).rstrip(u"\x00\n")]
            command.extend(arguments)
            raw_result = str(subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0])
            if 'ADLER' in raw_result:
                end_position = str(raw_result).find('(ADLER')-1
                start = end_position-8
                result = raw_result[start : end_position]
                print result
                file02.write(str(result)+"\n")
            elif len(raw_result) == 0:
                file02.write("file not found\n")
            else:
                file02.write("no checksum\n")

