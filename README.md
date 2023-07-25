# ⛔️ DEPRECATED


# Note
Please download tool to use with the matching OS version on Renesas repo https://github.com/renesas/amazon-freertos/releases

# Amazon-FreeRTOS-Tools

Tools to convert userprog.mot file to userprog.rsu file and create the combination of boot_loader.mot and aws_demos.mot to be userprog.mot.
userprog.mot is used for IDT tests as initial firmware. It's very convenience when only flashing at one time for both boot_loader.mot and aws_demos.mot by using userprog.mot. userprog.rsu file is used to upload to S3 for OTA update feature as update firmware.

How to use this tools?
We can use it as GUI and CUI mode. We recommend to use the CUI mode because of its advantage. This is used for IDT tests by setting some arguments. After the build of aws_demos and boot_loader are successfull, CUI mode will create userprog.mot and userprog.rsu.

1. Create userprog.mot file

"path_to_Renesas Secure Flash Programmer.exe" CUI Initial "RX65N(ROM 2MB)/Secure Bootloader=256KB" "sig-sha256-ecdsa" 1 "path_to_boot_loader.mot" "path_to_aws_demos.mot" "path_to_ secp256r1.privatekey" "path_to_userprog.mot"

2. Create userprog.rsu file

"path_to_Renesas Secure Flash Programmer.exe" CUI Update "RX65N(ROM 2MB)/Secure Bootloader=256KB" "sig-sha256-ecdsa" 1 "path_to aws_demos.mot" "path_to_userprog.rsu"

#OTA section for IDT tests 

Python script to change default section setting to EXCEPTVECT/0FFFBFF80,RESETVECT/0FFFBFFFC. The purpose of this script is to support the change of section setting for IDT tests more convenience.

The steps to set the build.bat for IDT tests.
1. python path_to_OTAsection.py --path-aws "path_to_amazon-freertos" (example "D:\test", test folder includes amazon-freertos folder)
2. path_to_eclipsec.exe -nosplash -debug -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data path_to_\devicetester_freertos_win\builddemos -import path_to_aws_demos -cleanBuild all
3. Create userprog.mot file
4. Create userprog.rsu file
