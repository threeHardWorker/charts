cp csv/10s_$1_$2.zip ./
unzip 10s_$1_$2.zip
sh 10s.sh $1 $2
sh 10s-bin.sh $1
rm -rf 10s_$1_$2*
