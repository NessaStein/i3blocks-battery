#!/usr/bin/env python3
import subprocess

battery = subprocess.check_output([ "acpi" ], universal_newlines=True)
if not battery:
    output = '<span font="FontAwesome" color="#ffffff">\f12a Error</span>'
else:
    battery_information = battery.split("\n")[0].split(", ")
    state = battery_information[0].split(":")[1]
    percent = int(battery_information[1].rstrip("%"))
    time = battery_information[2].split(" ")[0]
    class Status(object):
        color = ""
        icon = ""
        percent = ""
        time = ""
        def __init__(self, color, icon, percent, time):
            self.color = color
            self.icon = icon
            self.percent = str(percent)
            self.time = time
    def status_view(percent):
        if percent <= 3:
            subprocess.call(['notify-send', time])
            return Status("#FF3300", "\uf244", percent, time)
        if percent <= 5:
            return Status("#FF3300", "\uf244", percent, time)
        if percent <= 15:
            return Status("#FF3300", "\uf243", percent, time)
        if percent <= 25:
            return Status("#FFCC00", "\uf243", percent, time)
        if percent <= 50:
            return Status("#FFFFFF", "\uf242", percent, time)
        if percent <= 75:
            return Status("#FFFFFF", "\uf241", percent, time)
        return Status("#FFFFFF", "\uf240", percent, time)
    def state_view(state):
        if state == "Discharging": return ""
        if state == "Charging": return "\f1e6"
        return "1"
    status = status_view(percent)
    template = '<span font="FontAwesome"><span style="margin-rigth: -10px">{}</span><span color="{}">{}</span><span font="Roboto">{}<span>[{}]</span></span></span>'
    # output = template.format(state_view(state), status_view(percent))
    output = template.format(state_view(state), status.color, status.icon, str(status.percent), status.time)
print(output)
