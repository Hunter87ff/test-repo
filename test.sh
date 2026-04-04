MAX_RUNS=1
while [ $MAX_RUNS -gt 0 ]; do
    sudo ttyd -p 8000 -W bash
    sleep 500000000
    ((MAX_RUNS--))
done