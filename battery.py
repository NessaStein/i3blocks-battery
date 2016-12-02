#!/usr/bin/env python3
import subprocess

battery = subprocess.check_output([ "acpi" ], universal_newlines=True)
if not battery:
    output = '<span font="FontAwesome" color="#ffffff">\f12a Error</span>'
else:
    battery_information = battery.split("\n")[0].split(", ")
    state = battery_information[0].split(":")[1]
    percent = int(battery_information[1].rstrip("%"))
    class Status(object):
        color = ""
        icon = 0
        percent = ""
        def __init__(self, color, icon, percent):
            self.color = color
            self.icon = icon
            self.percent = percent
    def status_view(percent):
        if percent <= 10:
            return Status("#FF3300", "\uf244", percent)
        if percent <= 25:
            return Status("#FFCC00", "\uf243", percent)
        if percent <= 50:
            return Status("#FFFFFF", "\uf242", percent)
        if percent <= 75:
            return Status("#FFFFFF", "\uf241", percent)
        return Status("#FFFFFF", "\uf240", percent)
    status = status_view(percent)
    output =  '<span font="FontAwesome" color=' + '"' + status.color + '"' + '>' + status.icon + '<span font="Roboto">' + str(status.percent) + '%</span></span>'
print(output)
if percent < 10:
    exit(33)
