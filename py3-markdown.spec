### RPM external py3-markdown 3.3.3
## IMPORT build-with-pip3

%define pip_name Markdown

%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*