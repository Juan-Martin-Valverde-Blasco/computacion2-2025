while read linea; do
    echo "Lector recibió: $linea"
done < /tmp/mi_fifo
