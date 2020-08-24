#! /usr/bin/env python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse


parser = argparse.ArgumentParser(description='Change config to OTA demo and the section')
parser.add_argument('--path-aws', action='store', dest='path_aws',
                    help='Store the path to amazon-freertos')
args = parser.parse_args()

config_file			= str(args.path_aws) + '//amazon-freertos//vendors//renesas//boards//rx65n-rsk//aws_demos//config_files//aws_demo_config.h'
cproject_file       = str(args.path_aws) +  '//amazon-freertos//projects//renesas//rx65n-rsk//e2studio//aws_demos//.cproject'

"""Read aws_demo_config.h """
read_config_file = open(config_file, "r")
new_config_file = ""
for line in read_config_file:
    new_line = line.strip().replace("#define CONFIG_MQTT_DEMO_ENABLED", "#define CONFIG_OTA_UPDATE_DEMO_ENABLED")
    new_config_file += new_line +"\n"
read_config_file.close()

"""Change #define CONFIG_MQTT_DEMO_ENABLED" to "#define CONFIG_OTA_UPDATE_DEMO_ENABLED" """
write_file = open(config_file, "w")
write_file.write(new_config_file)
write_file.close()

"""Read cproject to change section """
read_cproject_file = open(cproject_file, "r")
new_file_cproject = ""
for line in read_cproject_file:
    new_line = line.strip().replace("EXCEPTVECT/0FFFFFF80,RESETVECT/0FFFFFFFC","EXCEPTVECT/0FFFBFF80,RESETVECT/0FFFBFFFC")
    new_file_cproject += new_line +"\n"

"""Change section to EXCEPTVECT = 0FFFBFF80,RESETVECT = 0FFFBFFFC"""
read_cproject_file.close()
write_file = open(cproject_file, "w")
write_file.write(new_file_cproject)
write_file.close()