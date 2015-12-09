echo [RACER] STARTING MJPEG STREAMER.......
cd /home/pi/NodeJSDemo/mjpeg-streamer
sudo ./start.sh > /dev/null 2>&1 &
cd ..
sleep 2
echo [RACER] STREAM STARTED
sudo ps ax | grep mjpg_streamer | grep -v grep

echo "--------------------------------------"
echo [RACER] INITIALIZING DRIVER: SEBULBA
cd podracer/hat-invaders
sudo ./invaders &


echo "--------------"
echo [RACER] "RACER READY."
echo "-------------"

sudo python podracer/robot-socket.py
