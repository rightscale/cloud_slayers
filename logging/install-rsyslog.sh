#! /usr/bin/sudo /bin/bash
/usr/bin/add-apt-repository ppa:adiscon/v8-stable
/usr/bin/apt-get update
/usr/bin/apt-get install rsyslog
cat <<EOF > /etc/rsyslog.conf
#  /etc/rsyslog.conf    Configuration file for rsyslog v3.
#
#                       For more information see
#                       /usr/share/doc/rsyslog-doc/html/rsyslog_conf.html

#  /etc/rsyslog.conf    Configuration file for rsyslog v3.
#
#                       For more information see
#                       /usr/share/doc/rsyslog-doc/html/rsyslog_conf.html
$MaxMessageSize 2k

#
# Preserve FQDN
#
$PreserveFQDN off

#################
#### MODULES ####
#################

$ModLoad imuxsock
$ModLoad imklog
$ModLoad imtcp
$InputTCPServerBindRuleset remote
$InputTCPServerRun 3389

###########################
#### GLOBAL DIRECTIVES ####
###########################

#
# Use default timestamp format.
# To enable high precision timestamps, comment out the following line.
#
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

# Filter duplicated messages
$RepeatedMsgReduction on

#
# Set temporary directory to buffer syslog queue
#
$WorkDirectory /var/spool/rsyslog

#
# Set the default permissions for all log files.
#
$FileOwner root
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022

#
# Include all config files in /etc/rsyslog.d
#
$IncludeConfig /etc/rsyslog.d/*.conf
EOF

cat <<EOF > /etc/rsyslog.d/50-default.conf
# Generated by BASE rsyslog RightScript
# For more information see rsyslog.conf(5) and /etc/rsyslog.conf

$template RemoteHost,"/log/%syslogfacility%/%HOSTNAME%.log"

# Local Logging
$RuleSet local
*.info;mail.none;authpriv.none;cron.none   /var/log/messages
mail.*   -/var/log/maillog
cron.*   /var/log/cron
authpriv.*   /var/log/secure
*.emerg   :omusrmsg:*
uucp,news.crit   /var/log/spooler
local7.*   /var/log/boot.log
# use the local RuleSet as default if not specified otherwise
$DefaultRuleset local


# Remote Logging
$RuleSet remote
*.* ?RemoteHost
EOF
