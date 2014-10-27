have_sum="ADLER"
while read line
do
    name=$line
    raw_result=$(lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/$name)
    if echo "$raw_result" | grep -q "$have_sum"; then    
        raw_result2='echo "$raw_result"| tail -c 19'
        y=$(eval $raw_result2)
        result=${y:0:8}
        echo $raw_result
    elif ["$raw_result" == ""]
    then 
        echo "file not found"
    else
        echo "no checksum"
    #result=${get_raw_result2:0:8}
    fi
done < $1
