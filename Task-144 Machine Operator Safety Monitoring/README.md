# Task-144 Machine Operator Safety Monitoring

## Overview
Automated safety zone monitoring pipeline built using **YOLOv8** and **ByteTrack** to detect and log worker safety violations in real-time across industrial workplace video feeds.

## Features & Implementation
* **Object Detection & Tracking:** Leverages YOLOv8 and ByteTrack to track workers and machinery operators in defined zones.
* **Breach Logging:** Automatically detects safety zone boundaries and logs violation timestamps into a CSV report.
* **Evidence Collection:** Captures frame snapshots during breach events for auditing.

## Deliverables & Repository Structure
* `Task_144_Safety_Monitoring.ipynb` - Core model implementation and pipeline notebook.
* `safety_breach_report.csv` - Detailed CSV report of recorded safety breaches.
* `snapshots/` - Sample evidence image frames captured during violations.

## Summary of Results
* **Processed Feeds:** 3 Video Streams
* **Total Breaches Logged:** 43 Safety Violation Events
