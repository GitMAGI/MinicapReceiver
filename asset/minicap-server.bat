::C:\android-sdk\tools\android-ndk-r14b\
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707

::To Restart The Device
::\android-sdk\platform-tools\adb.exe shell am broadcast -a android.intent.action.BOOT_COMPLETED

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 forward tcp:1717 localabstract:minicap

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 push "libs/armeabi-v7a/minicap" "/data/local/tmp/"
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 push "jni/minicap-shared/aosp/libs/android-23/armeabi-v7a/minicap.so" "/data/local/tmp/"
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell chmod 777 /data/local/tmp/minicap

::Other Minicap Server Options
:: -d <id>:         Display ID
:: -n <name>:       Change the name of the abtract unix domain socket
:: -P <value>:      Display projection (<w>x<h>@<w>x<h>/{0|90|180|270}). Note that 0|90|180|270 are the degrees of the display orientation
:: -Q <value>:      JPEG quality (0-100)
:: -s:              Take a screenshot and output it to stdout. Needs -P
:: -S:              Skip frames when they cannot be consumed quickly enough
:: -t:              Attempt to get the capture method running, then exit
:: -i:              Get display information in JSON format. May segfault
:: -h:              Show help

::To Get Help
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -h

::To Test Resolution
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0 -t

::PORTRAIT
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@270x480/0

::LANDSCAPE
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1920x1080@480x270/0

::PORTRAIT with Quality Manually set and Performance Options
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@270x480/0 -Q 60 -S

::LANDSCAPET with Quality Manually set and Performance Options
:: real_with x real_height @ virtual_with x virtual_height / display_orientation_degrees
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1920x1080@480x270/0 -Q 60 -S

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 forward --remove tcp:1717