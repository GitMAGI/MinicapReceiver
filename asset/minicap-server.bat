::C:\android-sdk\tools\android-ndk-r14b\
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707

::To Restart The Device
::\android-sdk\platform-tools\adb.exe shell am broadcast -a android.intent.action.BOOT_COMPLETED

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 forward tcp:1717 localabstract:minicap

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 push "libs/armeabi-v7a/minicap" "/data/local/tmp/"
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 push "jni/minicap-shared/aosp/libs/android-23/armeabi-v7a/minicap.so" "/data/local/tmp/"
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell chmod 777 /data/local/tmp/minicap

::To Get Help
:: real_with x real_height @ virtual_with x virtual_height
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -h

::To Test Resolution
:: real_with x real_height @ virtual_with x virtual_height
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0 -t

::PORTRAIT
:: real_with x real_height @ virtual_with x virtual_height
::C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@270x480/0

::LANDSCAPE
:: real_with x real_height @ virtual_with x virtual_height
C:\android-sdk\platform-tools\adb.exe -s 07ea9707 shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1920x1080@480x270/0

C:\android-sdk\platform-tools\adb.exe -s 07ea9707 forward --remove tcp:1717