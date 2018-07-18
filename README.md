# PIPlayer

This project was developed for escaperoom Vila Bretil in the netherlands.
It is a setup for a raspberry pi to start playing a video when a pin is pulled high

## Setup

clone this repo in a folder in your home directory called 'Apps'
navigate to this folder and the working directory should be
```sh
$ pwd
/home/pi/Apps/PIPlayer/
```
Now move the PIPlayer shell script to /etc/init.d and give it the right permissions
```sh
$ sudo mv PIPlayer /etc/init.d
$ sudo chmod 755 /etc/init.d/PIPlayer
```

Make sure the script will be started on boot up
```sh
$ sudo update-rc.d PIPlayer default
```

Now add your video to ~/Videos and name it Video.mp4
and test it out!

Note:
the video will be started when the pin goes low. So if you don't have a pull up on the pin on startup it will started playing immediately and might cause weird behaviour.

