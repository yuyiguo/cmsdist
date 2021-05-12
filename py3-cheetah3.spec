### RPM external py3-cheetah3 3.2.6.post2
## IMPORT build-with-pip3

%define pip_name Cheetah3

Requires: python3 py3-markdown.spec

%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*



