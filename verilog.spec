Summary: Icarus Verilog
Name: verilog
Version: 0.4
Release: x
Copyright: GPL
Group: Applications/Engineering
Source: ftp://icarus.com/pub/eda/verilog/v0.4/verilog-0.4.tar.gz
URL: http://www.icarus.com/eda/verilog/index.html
Packager: Stephen Williams <steve@icarus.com>

BuildRoot: /tmp

# This provides tag allows me to use a more specific name for things
# that actually depend on me, Icarus Verilog.
Provides: iverilog

%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including a C++ simulation. It strives to be
true to the IEEE-1364 standard.

%prep
%setup -n verilog-0.4

%build
./configure --prefix=/usr
make CXXFLAGS=-O

%install
make prefix=$RPM_BUILD_ROOT/usr install

%files

%attr(-,root,root) %doc COPYING README.txt BUGS.txt ieee1364-notes.txt netlist.txt t-dll.txt vpi.txt vvm.txt xnf.txt xilinx-hint.txt
%attr(-,root,root) %doc examples/*

%attr(-,root,root) /usr/bin/iverilog
%attr(-,root,root) /usr/lib/ivl/ivl
%attr(-,root,root) /usr/lib/ivl/ivlpp
%attr(-,root,root) /usr/lib/ivl/system.vpi
%attr(-,root,root) /usr/lib/ivl/iverilog.conf
%attr(-,root,root) /usr/lib/libvvm.a
%attr(-,root,root) /usr/include/ivl_target.h
%attr(-,root,root) /usr/include/vpi_priv.h
%attr(-,root,root) /usr/include/vpi_user.h
%attr(-,root,root) /usr/include/vvm.h
%attr(-,root,root) /usr/include/vvm_calltf.h
%attr(-,root,root) /usr/include/vvm_func.h
%attr(-,root,root) /usr/include/vvm_gates.h
%attr(-,root,root) /usr/include/vvm_nexus.h
%attr(-,root,root) /usr/include/vvm_signal.h
%attr(-,root,root) /usr/include/vvm_thread.h
%attr(-,root,root) /usr/man/man1/iverilog.1
