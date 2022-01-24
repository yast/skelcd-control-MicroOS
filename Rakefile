require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

# this package uses the date versioning in master (for openSUSE Tumbleweed),
# replace the standard yast task implementation
Rake::Task[:'version:bump'].clear
namespace :version do
  desc "Update version in the package/skelcd-control-MicroOS.spec file"
  task :bump do
    spec_file = "package/skelcd-control-MicroOS.spec"
    spec = File.read(spec_file)

    # parse the current version, it can be in <date> or <date>.<release> format
    _, version, release = spec.match(/^\s*Version:\s*(\w+)(?:\.(\w+))?$/).to_a
    # use the UTC time to avoid conflicts when updating from different time zones
    date = Time.now.utc.strftime("%Y%m%d")

    # add a release version if the package has been already updated today
    new_version = if version == date
      # if the release was missing it starts from 1
      "#{date}.#{release.to_i + 1}"
    else
      "#{date}"
    end

    puts "Updating to #{new_version}"
    spec.gsub!(/^\s*Version:.*$/, "Version:        #{new_version}")
    File.write(spec_file, spec)
  end
end

CONTROL_SCHEMA = "/usr/share/YaST2/control/control.rng".freeze
XSL_FILE = "control/control.MicroOS.xsl".freeze
DEFAULT_OPENSUSE_CONTROL="/usr/lib/skelcd/CD1/control.xml"
OPENSUSE_CONTROL = ENV["OPENSUSE_CONTROL"] || DEFAULT_OPENSUSE_CONTROL
TARGET_XML = "control/control.TWMicroOS.xml".freeze
BASE_XML = "control/control.MicroOS.xml"

file TARGET_XML => [ XSL_FILE, BASE_XML ] do
    # the location is relative to the input file, change the CWD so relative
    # paths work correctly
    Dir.chdir("control") do
      abort "Missing file #{OPENSUSE_CONTROL}" unless File.exist?(OPENSUSE_CONTROL)
    end

    sh "xsltproc", "--stringparam", "openSUSE_control_file", OPENSUSE_CONTROL,
      "--output", TARGET_XML, XSL_FILE, BASE_XML
end

desc "Build the TWMicroOS XML (set the base XML file via $OPENSUSE_CONTROL, default: #{DEFAULT_OPENSUSE_CONTROL})"
task :build => TARGET_XML.to_sym

desc "Validate the built XML"
task :"test:validate" => TARGET_XML do
  begin
    # prefer using jing for validation
    sh "jing", CONTROL_SCHEMA, TARGET_XML
    puts "OK"
  rescue Errno::ENOENT
    # fallback to xmllint
    sh "xmllint", "--noout", "--relaxng", CONTROL_SCHEMA, TARGET_XML
  end
end

desc "Remove the generated XML file"
task :clean do
  rm TARGET_XML if File.exist?(TARGET_XML)
end

