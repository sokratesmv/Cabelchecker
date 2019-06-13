cd /home/pi
python3  listen-for-shutdown.py &
while true; do
    cd /home/pi/Cabelchecker
    python3 Prog.py
done
