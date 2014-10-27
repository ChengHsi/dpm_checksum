while read line
do
    name=$line
    checksum="Checksum"
    raw_result=$(lcg-ls -l srm://f-dpm001.grid.sinica.edu.tw/$name)
    string_raw_result=($raw_result)
    #if echo "$string_raw_result" | grep -q "$checksum"; then
    #    raw_result2='echo "$raw_result"| tail -c 19'
    #    y=$(eval $raw_result2)
    #    result=${y:0:8}
    #    echo $result; 
    #elif ["$raw_result" -eq ""]; then
    #    echo "file not found";
    #else
    #    echo "no checksum";     
    #fi
    echo ${string_raw_result[4]}
   
    #result=${get_raw_result2:0:8}
    #echo "$raw_result"|awk '{print $NF}'
    
done < $1
