import sys, time, datetime,optparse, os
filename=sys.argv[1]
path = os.path.abspath(filename)
b = str(path).index('f-dpmp')
serv_name = str(path)[b:b+8]
a = str(path).index('data')
dev_name = str(path)[a:a+6]
dates = []
file_lines = []
#savepath = str('/asgc_ui_home/chchao/task_checksum/new_'+serv_name+'/'+dev_name+'/'+serv_name+'_'+dev_name)
#path = os.path.abspath(filename)
c = str(path).index('filelist')
savepath = str(path)[:c-1]
timestamp = str(path)[c+8:]
print savepath

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def date_generator(year, month):
    start_date = datetime.date(year, month, 1)
    if month != 12:
        end_date = datetime.date(year, month+1, 1)
    else:
        end_date = datetime.date(year+1, 1, 1)
    for single_date in daterange(start_date, end_date):
        dates.append(time.strftime("%Y-%m-%d", single_date.timetuple())+'/')

def select():
    global file_lines
    selected_lines = []
    with open(str(filename), 'r') as file01:
        for line in file01:
            for date in dates:
                if date in line:
                    selected_lines.append(line.split(' '))
    file_lines = selected_lines

def write_selected(option, opt, value, parser):
    date_generator(2012, 8)
    date_generator(2012, 9)
    date_generator(2013, 2)
    select()
    a = str(filename).index('data')

    with open(savepath + "_selected_filelist", 'w') as FO:
        for line in file_lines:
            FO.write(str(line))

def split():
    counter = 1
    if not file_lines:
        with open (savepath + "_localpath" + timestamp, 'w') as FO1:
            with open(savepath + '_pnfpath' + timestamp, 'w') as FO2:
                with open(str(filename), 'r') as file01:
                    for line in file01:
                        line = line.split(' ')
                        print counter
                        line[0] = str(line[0]).replace(serv_name + '.grid.sinica.edu.tw:', '')
                        FO2.write(str(line[1].rstrip())+'\n')
                        FO1.write(str(line[0].rstrip())+'\n')
                        counter += 1
    else:
        with open (savepath + "_selected_localpath" + timestamp, 'w') as FO1:
            with open(savepath + '_selected_pnfpath' + timestamp, 'w') as FO2:
                for line in file_lines:
                    print counter
                    line[0] = str(line[0]).replace(serv_name + '.grid.sinica.edu.tw:', '')
                    FO2.write(str(line[1].rstrip())+'\n')
                    FO1.write(str(line[0].rstrip())+'\n')
                    counter += 1

def main():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--write_select", action="callback", callback=write_selected, default=False, help="select a list of file instead of using the whole list")
    (opt,args) = parser.parse_args()
    #print dates
    split()

if __name__ == '__main__':
    main()

