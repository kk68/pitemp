#!/usr/bin/python
#
# This project is using DHT11 or DHT22 connected to pin GPIO 04 or aka pin 7
# It reqiures jquery.tempgauge.js, which can be donwloaded from https://github.com/akumagamo/jquery-plugin-tempgauge
#
# Enjoy!

import sys
import time
import Adafruit_DHT

now = time.strftime("%c")
htmlfilename = '/var/www/html/index-notrend.html'

#while True:
count = 0
while (count < 1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    convert = temperature * 1.8 + 34
    count = count + 1
mytemp1 = '{0:0.1f}'.format(convert)
html = ''
html = html +  '<!doctype html>\n'
html = html +  '<html>\n'
html = html +  '<head>\n'
html = html +  '<title>Temperature Probe with DHT22</title>\n'
html = html +  '<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>\n'
html = html +  '<script type="text/javascript" src="js/jquery.tempgauge.js"></script>\n'
html = html +  '<script type="text/javascript">\n'
html = html +  '		$(function(){\n'
html = html +  '			if(!(/^\?noconvert/gi).test(location.search)){\n'

if convert >= 77:
   html = html +  '				$(".tempGauge0").tempGauge({maxTemp:102, minTemp:32, width:150, borderWidth:2, showLabel:true, showScale : true, fillColor:"red"});\n'
elif convert >= 75:
   html = html +  '                              $(".tempGauge0").tempGauge({maxTemp:100, minTemp:32, width:200, borderWidth:2, showLabel:true, showScale : true, fillColor:"yellow"});\n'
else:
   html = html +  '                              $(".tempGauge0").tempGauge({maxTemp:100, minTemp:32, width:200, borderWidth:2, showLabel:true, showScale : true, fillColor:"green"});\n'

html = html +  '			}\n'
html = html +  '		});\n'
html = html +  '</script>\n'
html = html +  '</head>\n'
html = html +  '<body>\n'
html = html +  '<div class="tempGauge0">' + mytemp1 + '&deg;F</div>\n'
html = html +  '<div>\n'
html = html +  ("Last update: %s"  % now )
html = html +  '</div>\n'
html = html +  '</body>\n'
html = html +  '</html>\n'

f = open(htmlfilename, 'w')
f.write(html)
f.close()
