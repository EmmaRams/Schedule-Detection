# Schedule-Detection#  Schedule Detection CLI App

A **Python command-line tool** to manage and organize personal schedules by allowing users to add, view, and delete events — with **automatic conflict detection** to prevent overlapping appointments.

---

##  Overview

This project provides a lightweight solution for time management. Whether it's for classes, meetings, or personal tasks, the app helps avoid schedule conflicts and ensures better productivity.

---

##  Features

- **Add Events:** Create events with a title, start and end time, and optional description
- **Conflict Detection:** Automatically checks for time overlaps before adding new events
- **View Schedule:** List all scheduled events sorted by start time
- **Delete Events:** Remove any event by title
- **Persistent Storage:** Events are saved in a local JSON file

---

##  Tech Stack

- Language: **Python 3.7+**
- Libraries: `argparse`, `datetime`, `json`, `bisect`, `os`
- No external dependencies

---

##  Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EmmaRams/schedule-detection-cli.git
   cd schedule-detection-cli
