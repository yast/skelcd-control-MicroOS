<!--
  Definition of the control.MicroOS.xml -> control.TWMicroOS.xml transformation.
-->

<xsl:stylesheet version="1.0"
  xmlns:n="http://www.suse.com/1.0/yast2ns"
  xmlns:config="http://www.suse.com/1.0/configns"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.suse.com/1.0/yast2ns"
  exclude-result-prefixes="n"
>

  <!-- allow changing the input file with a command line parameter -->
  <xsl:param name="openSUSE_control_file" select="'/usr/lib/skelcd/CD1/control.xml'"/>

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- Add the "extra_urls" part from the normal openSUSE control file -->
  <xsl:template match="n:software">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
      <xsl:copy-of select="document($openSUSE_control_file)/*/n:software/n:extra_urls"/>
    </xsl:copy>
  </xsl:template>

</xsl:stylesheet>
