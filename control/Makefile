
# checks only those control files that belong to this package
check: /usr/share/YaST2/control/control.rng
	xmllint --relaxng /usr/share/YaST2/control/control.rng --noout *.xml

# generate the control.TWMicroOS.xml file
control.TWMicroOS.xml: control.MicroOS.xsl control.MicroOS.xml
	xsltproc control.MicroOS.xsl control.MicroOS.xml > control.TWMicroOS.xml

clean:
