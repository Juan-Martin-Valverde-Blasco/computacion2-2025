declare -A estados

echo "PID   PPID  NOMBRE                ESTADO"
echo "---------------------------------------------"

for pid in /proc/[0-9]*; do
    if [[ -f "$pid/status" ]]; then
        pid_num=$(basename "$pid")
        ppid=$(grep "^PPid:" "$pid/status" | awk '{print $2}')
        name=$(grep "^Name:" "$pid/status" | awk '{print $2}')
        state=$(grep "^State:" "$pid/status" | awk '{print $2}')

        estados[$state]=$((estados[$state]+1))

        printf "%-5s %-5s %-20s %-2s\n" "$pid_num" "$ppid" "$name" "$state"
    fi
done

echo ""
echo "Resumen de estados:"
for estado in "${!estados[@]}"; do
    echo "$estado: ${estados[$estado]}"
done
