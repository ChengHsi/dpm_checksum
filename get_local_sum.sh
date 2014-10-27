while read line
do
    name=$line
    raw_result=$(xrdadler32 $name)
    result=${raw_result:0:8}
    echo $result
done < $1
