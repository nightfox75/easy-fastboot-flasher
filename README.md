# EASY FASTBOOT FLASHER
The easy way to install new Android OS on your device.

This is GUI-based tool for Windows to help peoples install new custom or original OS on unlocked devices in minutes.

# ADVANTAGES
- Simple design
- Easy to use
- Fully automatic
- SDK Platform Tools by Google is included in program, so you don't need to install it

# INSTALLATION
1. Unlock your devices bootloader. You can find out how to do it here: https://source.android.com/docs/setup/build/running, under "Unlocking the bootloader";
2. Install Google's USB Driver. You can download it from here: https://dl.google.com/android/repository/usb_driver_r13-windows.zip;
3. Download the latest release of EASY FASTBOOT FLASHER. You can find it in Releases.

# USAGE
1. Connect your device to the PC and reboot it into fastboot mode;
2. Run latest release of EASY FASTBOOT FLASHER;
3. Reboot your device into fastboot mode. There are different ways to do this. You can find this information on Google for your device;
4. In application select your image file you want to install. Click "Select file..." or type your full file path into label for typing;
5. (Advanced) If you want to safely install new Android OS on your device, you can checkmark "Disable AVB Verification" checkbox to disable AVB and/or "Perform factory reset" checkbox to erase your data;
6. Click "Start" button to start process. Application may freeze during installing moment, so that's not a problem.

# TROUBLESHOOTING
- If you see the text "waiting-for-device", but you've already connected your device, try to reconnect it, check if your device in fastboot mode and USB driver is installed and ready to use.
- If your commands have been skipped by the program, that means you've not selected file for flashing. Check is that right.
- If some functions is not working, Platform Tools is not responding or program (or Platform Tools) has been crashed - inform me about that in Issues tab using tag "bug". 

# PRECAUTIONARY MEASURES
- This is a new software that can have problems and bugs.
- Using not compatible Android image and/or other software can harm your device. Please use at your own risk.

# CREDITS
Thankfully to Google's SDK Platform Tools, this program can flash Android images.
