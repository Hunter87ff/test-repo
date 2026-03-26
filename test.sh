MAX_RUNS=1
while [ $MAX_RUNS -gt 0 ]; do
    sudo systemctl start ttyd
    sleep 500000000
    ((MAX_RUNS--))
done