#! /usr/bin/env bash

file_name=$(date +%Y%m%d_%H:%M)

adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png ${HOME}/${file_name}.png
adb shell rm /sdcard/screen.png
