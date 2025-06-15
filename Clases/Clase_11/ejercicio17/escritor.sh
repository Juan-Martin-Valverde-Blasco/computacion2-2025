i=0
while true; do
    echo "Mensaje $i desde escritor (PID $$)" > /tmp/mi_fifo
    ((i++))
    sleep 1
done
