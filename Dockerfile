FROM yastdevel/ruby
# install the openSUSE control.xml, we need to copy some parts to Kubic
RUN zypper --non-interactive in --no-recommends skelcd-control-openSUSE
COPY . /usr/src/app
