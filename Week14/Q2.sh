#!/bin/bash

# Create a health check report
REPORT="/tmp/system_health_report.txt"
echo "System Health Check Report" > $REPORT
echo "=========================" >> $REPORT

# Check CPU usage
echo "CPU Usage:" >> $REPORT
top -bn1 | grep "Cpu(s)" >> $REPORT

# Check memory usage
echo -e "\nMemory Usage:" >> $REPORT
free -h >> $REPORT

# Check disk space
echo -e "\nDisk Space:" >> $REPORT
df -h >> $REPORT

# Output the report
cat $REPORT
