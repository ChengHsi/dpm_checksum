entry="$1"
filename=${entry//path/sum}

/bin/bash ./get_local_sum.sh $1 |tee $filename
#/bin/bash ./get_local_sum.sh $1
