while True
do
  f=$(find ./custom_tmp -maxdepth 1 -type f | wc -l)
  d=$(find ./custom_tmp -maxdepth 1 -type d | wc -l)
  printf "Contents of custom_tmp: %d files, %d folders\n" $f $(($d-1))
  sleep 10s
done
