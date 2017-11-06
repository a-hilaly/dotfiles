
macOS_tools = """
Tools
KernelEventAgent
/usr/sbin/KernelEventAgent handles one of the core system services (events such as file systems being mounted and unmounted, low disk space, network connections going down, etc.)

SystemStarter
/sbin/SystemStarter is run during system initialization to handle "startup items". See "Mac OS X System Startup" for details.

aexml
/usr/sbin/aexml forwards XMLRPC and SOAP requests to the AppleEvent manager for further dispatching. More documentation is available on the Apple Developer Web Site.

appleping
/usr/bin/appleping exercises the AppleTalk network by sending packets to a named host.

ardbgd
/usr/sbin/ardbgd is the daemon for the Apple Remote Debugging Service.

asr
/usr/sbin/asr (Apple Software Restore) efficiently copies disk images and volumes, and can also accurately clone volumes.

bless
/usr/sbin/bless is used to set volume bootability characteristics for Macintoshes. The command can be used to select a folder on a mounted volume to act as the blessed system folder, and optionally update Open Firmware to boot from that volume. It can also be used to format and setup a volume for the first time. Finally, it can be used to query the folder(s) that are blessed on a volume. Try the following (non-destructive) commands:


    % sudo bless -verbose -info /
    ...
    % sudo bless -verbose -plist -info /

blued
/usr/sbin/blued is the Bluetooth daemon.

cac_*
/usr/sbin/cac_* are scripts related to CAC (Common Access Card) support. A CAC can be thought of as a SmartCard that combines multiple cards (functions) into one. A CAC can enable physical access to buildings and controlled places, enable computer network and system access and serve as the primary platform for the PKI token.

cmpdylib
/usr/bin/cmpdylib compares two dynamic shared libraries for compatibility.

createhomedir
/usr/sbin/createhomedir creates and populates local home directories.

ddb
ddb is a debugging mechanism that can be compiled into Mac OS X, similar to BSD's kdb. While gdb can be used over Ethernet (through a kernel stub), ddb is compiled into the kernel and is used over a serial line. Most importantly, ddb requires an actual built-in hardware serial line on the debug target. Fortunately, gdb should suffice for almost all debugging needs unless one is trying to debug an Ethernet driver itself, say.

ddb is not present by default on Mac OS X. It must be compiled from source (xnu/osfmk/ddb in the CVS tree).

defaults
/usr/bin/defaults is used to access (read, write and delete) Mac OS X user defaults from the command line. For example, the following will print out Desktop background settings (including the pathname for the desktop background image, if any):


    % defaults read com.apple.desktop Background

dev_mkdb
/usr/sbin/dev_mkdb creates a hash access method database (based on Berkeley DB) in /var/run/dev.db. This database contains the name of all devices under /dev.

diskarbitrationd
/usr/sbin/diskarbitrationd is a daemon that listens for connections from clients, notifies clients of the appearance of disks and filesystems, and governs the mounting of filesystems and claiming of disks amongst clients.

disktool
/usr/sbin/disktool is a command line utility for disk arbitration. It can be used to rename, eject, mount or unmount disks and volumes.

diskutil
/usr/sbin/diskutil is a utility for managing disks and volumes. It can be used to perform operations such as enabling/disabling HFS+ journaling, verifying and repairing permissions, erasing disks (including optical media), partitioning, creating and managing RAID sets etc. You typically need root access to use this utility.

ditto
/usr/bin/ditto copies files and directories to a destination directory. ditto can be used to "thin" "fat" (multiple-architecture) exectuables. It can also copy files selectively based on the contents of a BOM ("Bill of Materials"). One of the most useful features of ditto is that it can preserve resource fork and HFS meta-data information when copying files.

drutil
/usr/bin/drutil is a command line tool that uses the DiscRecording framework to interact with attached CD/DVD burning devices.

dscl
/usr/bin/dscl is the Directory Service command line utility.

dsperfmonitor
/usr/bin/dsperfmonitor is a directory tool for testing plugin performance in Directory Services.

dynamic_pager
/sbin/dynamic_pager is started during system initialization to manage swap files. See Mac OS X System Startup for details.

fdisk
/usr/sbin/fdisk displays or changes the DOS partition table found in the bootsector of x86 bootable disks.

fixPrecomp
/usr/bin/fixPrecomp is a tool for "fixing" precompiled header warnings that occur when headers get out-of-sync with their precompiled versions - after a system update, say.

fixproc
/usr/bin/fixproc is a Perl script that "fixes" a named process by performing the specified action (which can be check, kill, restart, exist or fix).

fs_usage
/usr/bin/fs_usage presents an ongoing display of system call usage information pertaining to file system activity. By default this includes all system processes except the running fs_usage process, Terminal, telnetd, sshd, rlogind, tcsh, csh and sh.

fstat
/usr/bin/fstat identifies open files (including sockets).

heap
/usr/bin/heap lists all the malloc-allocated buffers in the specified process's heap.

hdiutil
/usr/bin/hdiutil uses the DiskImages framework to manipulate disk image files.

hlfsd
/usr/sbin/hlfsd is the home-link file system daemon. It implements a file system containing a symbolic link to a subdirectory within a user's home directory, depending on the user which accessed that link.

installer
/usr/sbin/installer is the Mac OS X system software and package installer tool.

install_name_tool
/usr/bin/install_name_tool changes the dynamic shared library install names recorded in a Mach-O binary.

ioalloccount
/usr/sbin/ioalloccount displays some accounting of memory allocated by IOKit allocators, including object instances, in the kernel. This is useful for tracking memory leaks.

ioclasscount
/usr/sbin/ioclasscount displays the instance count, offset by the number of direct subclasses that have at least one instance allocated, for the classes specified. This is useful for tracking leaks.

ioreg
/usr/sbin/ioreg displays the IOKit registry. Try ioreg -l, for example, and you can see detailed registry information (including object properties) - such as details of various temperature sensors in the system (on the I2C bus).

iostat
/usr/sbin/iostat displays kernel I/O statistics on terminal, disk and cpu operations.

ipconfig
/usr/sbin/ipconfig can be used to get the number of network interfaces active (the ifcount argument), and also to retrieve various options associated with these interfaces. For example, "ipconfig getoption en1 lease_time" prints the DHCP lease time of en1 if applicable. Finally, ipconfig can also be used to set an interface for BOOTP, DHCP etc.

kdump
/usr/bin/kdump displays the kernel trace files produced with ktrace in human readable format.

kextcache
/usr/sbin/kextcache creates or updates kext caches, which are used to speed up kernel extension loading operations and to prepare kexts for inclusion in such media as device ROM.

kextload
/sbin/kextload can be used to explicitly load kernel extensions, validate them to see that they can be loaded by other mechanisms, such as kextd, and to generate symbol files for debugging the kext in a running kernel.

kextstat
/usr/sbin/kextstat displays the status of any kernel extensions currently loaded in the kernel.

kextunload
/sbin/kextunload is used to terminate and unregister IOKit objects associated with a kernel extension and to unload the code and personalities for that kext.

kgmon
/usr/sbin/kgmon generates a dump of the operating system's profile buffers for later analysis by gprof.

ktrace
/usr/bin/ktrace enables kernel trace logging for the specified processes, causing trace data to be logged to a file. Traced kernel operations include system calls, namei translations, signal processing and I/O.

latency
/usr/bin/latency is used for monitoring scheduling and interrupt latency. The tool can also be used to set real time or timeshare scheduling policies.

ld
/usr/bin/ld is the (Mach) object file link editor.

leaks
/usr/bin/leaks examines a specified process for malloc-allocated buffers which are not referenced by the program.

lipo
/usr/bin/lipo creates or operates on multi-architecture ("fat") files. It can list the architecture types in a fat file, create a single fat file from one or more input files, thin out a single fat file to a specified architecture type, and extract, replace and/or remove architecture types from the input file.

lockfile
/usr/bin/lockfile can be used to create one or more (conditional) semaphore files, with the provision of waiting for a specified number of seconds and a specified number of retries.

lsbom
/usr/bin/lsbom interprets the contents of binary bom (bill-of-materials) files. bom is a file system used by the Mac OS X installer to determine which files to install, remove, or upgrade.

lsof
/usr/sbin/lsof lists information about files opened by processes.

lsvfs
/usr/bin/lsvfs lists known (currently loaded) virtual file systems.

mDNSResponder
/usr/sbin/mDNSResponder (Multicast DNS Responder) listens for and responds to DNS-format query packets sent via Multicast to UDP port 5353.

mach_init
/sbin/mach_init is a daemon that maintains various mappings between service names and the Mach ports that provide access to those services.

malloc_history
/usr/bin/malloc_history inspects a given process and lists the malloc allocations performed by it. It relies on information provided by the standard malloc library when debugging options have been turned on.

mig
/usr/bin/mig (Mach Interface Generator) is used to compile procedural interfaces to Mach's message-based APIs, based on descriptions of those APIs.

mkbom
/usr/bin/mkbom creates a bom (bill-of-materials) given a directory.

mkextunpack
/usr/sbin/mkextunpack extracts the contents of a multikext (mkext) archive.

netstat
/usr/sbin/netstat symbolically displays the contents of various network-related data structures.

nibindd
/usr/sbin/nibindd is a daemon that is responsible for finding, creating and destroying NetInfo servers.

nibtool
/usr/bin/nibtool is used for printing, verifying and updating nib files.

nicl
/usr/bin/nicl is a general-purpose utility for operating on NetInfo databases. Its commands allow one to create, read and manage NetInfo data.

nidomain
/usr/sbin/nidomain is an interface to nibindd to which it sends all of its requests about the domains served on a given machine. It can also be used to create and destroy NetInfo databases.

nifind
/usr/bin/nifind finds a directory in the NetInfo hierarchy.

nigrep
/usr/bin/nigrep searches for a regular expression in the NetInfo hierarchy.

niload
/usr/bin/niload loads information from standard input into the given NetInfo domain.

nireport
/usr/bin/nireport prints tables from the NetInfo hierarchy.

niutil
/usr/bin/niutil is used to do arbitrary reads and writes on the given NetInfo domain.

nmedit
/usr/bin/nmedit is used to change global symbols to local symbols. It differs from strip in that it also changes the symbolic debugging information for the global symbols it changes to static symbols so that the resulting object can still be used with a debugger.

notifyd
/usr/sbin/notifyd is a daemon that facilitates processes to exchange stateless notification events.

nvram
/usr/sbin/nvram allows manipulation of Open Firmware non-volatile RAM variables.

objcopy
objcopy is part of binutils that you can download, compile and install. This utility copies the contents of an object file to another, using the GNU BFD (Binary File Descriptor) library to access the object files.

objdump
objdump is part of binutils. It displays information (including disassembly, if required) about one or more object files.

open
/usr/bin/open is a command line utility to open a file (or a directory or URL), just as if you had double-clicked the file's icon.

open-x11
/usr/bin/open-x11 is a wrapper shell script that provides open functionality for X11 applications.

orbd
/usr/bin/orbd is the Object Request Broker Daemon. It is a tool to enable clients to transparently locate and invoke persistent objects on servers in the CORBA environment.

osacompile
/usr/bin/osacompile compiles the given files, or standard input if non are listed, into a single output script.

osalang
/usr/bin/osalang prints information about installed OSA (Open Script Architecture) languages.

osascript
/usr/bin/osascript executes the given script file, or standard input if none is given. Scripts may be plain text or compiled scripts.

otool
/usr/bin/otool displays specified parts of object files or libraries (similar to ldd on Linux).

pagestuff
/usr/bin/pagestuff displays information about the specified logical pages of a file conforming to the Mach-O executable format.

pax
/bin/pax is a tool for reading, writing, and listing members of an archive file. It is also used to copy directory hierarchies. pax supports various archive formats such as cpio, bcpio, sv4cpio, sv4crc, tar, and ustar.

pbcopy
/usr/bin/pbcopy is used to copy standard input to the pasteboard buffer.

pbpaste
/usr/bin/pbpaste prints the contents of the pasteboard buffer.

pcscd
/usr/sbin/pcscd is a daemon used to dynamically allocate/deallocate Smart Card reader drivers at runtime and manage connections to the readers. Related utilities include /usr/bin/pcsctest and /usr/bin/pcsctool. These tools are taken from the MUSCLE (Movement for the Use of Smart Cards in a Linux Environment) project, a project to coordinate the development of smart cards and applications under Linux.

pdisk
/usr/sbin/pdisk is a menu driven program which partitions disks using the standard Apple disk partitioning scheme.

plutil
/usr/bin/plutil can be used to check the syntax of property list files, or convert a plist file from one format to another.

pmset
/usr/bin/pmset changes and reads power management settings such as idle sleep timing, wake on administrative access, automatic restart on power loss, etc.

pstat
/usr/sbin/pstat displays open file entry, swap space utilization, terminal state, and vnode data structures.

redo_prebinding
/usr/bin/redo_prebinding is used to redo the prebinding of an executable or dynamic library when one of the dependent dynamic library changes. The input file, executable or dynamic library, must have initially been prebound for this program to redo the prebinding.

say
/usr/bin/say uses the Speech Synthesis manager to convert input text to audible speech and either play it through the sound output device chosen in System Preferences or save it to an AIFF file.

screencapture
/usr/sbin/screencapture captures the screen (a window selection or a mouse selection) to the clipboard or a file (as PDF).

scselect
/usr/sbin/scselect is used to change current network location, or to list defined locations.

sc_usage
/usr/bin/sc_usage displays an ongoing sample of system call and page fault usage statistics for a given process.

scutil
/usr/sbin/scutil is a tool to communicate with configd, read and write from/to the configuration data store etc.

security
/usr/bin/security provides a command line interface to administer Keychains, manipulate keys and certificates, and do most things the Security framework is capable of.

segedit
/usr/bin/segedit extracts and/or replaces the named sections from the specified input file and creates an output.

setregion
/usr/bin/setregion is the command line utility for setting the DVD drive's "region".

sips
/usr/bin/sips is a command line interface to the Scriptable Image Processing Server. The graphical abilities of Mac OS X are exposed through this image processing service. The SIPS architecture contains tools for performing basic image alterations and support various image formats. The goal is to provide quick, convenient, desktop automation of common image processing operations.

slpd
/usr/sbin/slpd is the Service Location Protocol daemon that advertises local services to the network.

slp_reg
/usr/sbin/slp_reg is a tool to register URLs via the Service Location Protocol in order for remote machines to discover locally registered services.

softwareupdate
/usr/sbin/softwareupdate is a command line utility to perform software updates under Mac OS X.

srm
/usr/bin/srm securely (by overwriting, renaming, and truncating before unlinking) removes files or directories.

sw_vers
/usr/bin/sw_vers prints the product name (such as Mac OS X), version and build number.

sysctl
/usr/sbin/sysctl retrieves kernel state and allows processes with appropriate privilege to set kernel state.

system_profiler
/usr/sbin/system_profiler is the command line system profiling utility.

tcpdump
/usr/sbin/tcpdump dumps traffic on a network.

top
/usr/bin/top displays an ongoing sample of system usage statistics (such as cpu utilization, memory usage etc. for each process).

trpt
/usr/sbin/trpt interrogates the buffer of TCP trace records created when a socket is marked for debugging (via setsockopt()) and prints a readable description of these records.

update_prebinding
/usr/bin/update_prebinding tries to synchronize prebinding information for libraries and executables when new files are added to a system. Prebinding information is pre-calculated address information for libraries used by a given executable or library. By pre-determining where a function in another library is destined to be placed, the dynamic linker does not have to resolve symbols at application startup time.

vm_stat
/usr/bin/vm_stat displays Mach virtual memory statistics.

vmmap
/usr/bin/vmmap displays the virtual memory regions allocated in a specified process, indicating how memory is being used, and what the purposes of memory at a given address might be.

vpnd
/usr/sbin/vpnd is the Mac OS X VPN service daemon.

xcode*
/usr/bin/xcode* are Xcode related commands.

xxd
/usr/bin/xxd creates a hex dump of a given file or standard input. It can also convert a hex dump back to its original binary form.
"""

if __name__ == "__main__":
    print(macOS_tools)
