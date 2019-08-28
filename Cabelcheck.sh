cd /home/pi
python3  listen-for-shutdown.py &
cd /home/pi/Cabelchecker
while true; do
    python3 Prog.py
done
