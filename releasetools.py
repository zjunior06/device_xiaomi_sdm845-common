# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017-2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_Assertions(info):
  AddTrustZoneAssertion(info, info.target_zip)
  return

def AddImage(info, basename, dest):
  path = "IMAGES/" + basename
  if path not in info.input_zip.namelist():
    return

def AddImageRadio(info, basename, dest):
  name = basename
  path = "RADIO/" + name
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.Print("Patching {} image...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def OTA_InstallEnd(info):
  AddImage(info, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo")
  AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")

# Firmware
  AddImageRadio(info, "abl_a.elf", "/dev/block/bootdevice/by-name/abl_a")
  AddImageRadio(info, "abl_b.elf", "/dev/block/bootdevice/by-name/abl_b")
  AddImageRadio(info, "cmnlib64.img", "/dev/block/bootdevice/by-name/cmnlib64_a")
  AddImageRadio(info, "aop.img", "/dev/block/bootdevice/by-name/aop_a")
  AddImageRadio(info, "devcfg.img", "/dev/block/bootdevice/by-name/devcfg_a")
  AddImageRadio(info, "qupfw.img", "/dev/block/bootdevice/by-name/qupfw_a")
  AddImageRadio(info, "tz.img", "/dev/block/bootdevice/by-name/tz_a")
  AddImageRadio(info, "storsec.img", "/dev/block/bootdevice/by-name/storsec_a")
  AddImageRadio(info, "keymaster.img", "/dev/block/bootdevice/by-name/keymaster_a")
  AddImageRadio(info, "bluetooth.img", "/dev/block/bootdevice/by-name/bluetooth")
  AddImageRadio(info, "xbl.img", "/dev/block/bootdevice/by-name/xbl_a")
  AddImageRadio(info, "modem.img", "/dev/block/bootdevice/by-name/modem")
  AddImageRadio(info, "xbl_config.img", "/dev/block/bootdevice/by-name/xbl_config_a")
  AddImageRadio(info, "dsp.img", "/dev/block/bootdevice/by-name/dsp")
  AddImageRadio(info, "cmnlib.img", "/dev/block/bootdevice/by-name/cmnlib_a")
  AddImageRadio(info, "hyp.img", "/dev/block/bootdevice/by-name/hyp_a")
  return
