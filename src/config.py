import os
from datetime import date

# demo variables
DEMO_MODE = os.environ.get("DEMO_MODE", "false").lower() == "true"
FROZEN_TODAY = date(2026, 9, 16) if DEMO_MODE else date.today()

# Directories
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT_DIR, 'data_demo' if DEMO_MODE else 'data')

# file paths 
STUDENT_DATA = os.path.join(DATA_DIR, 'student.csv')
ATTEND_DATA = os.path.join(DATA_DIR, 'attendance_habits.csv')
DEADLINES_DATA = os.path.join(DATA_DIR, 'master_deadlines.csv')
STUDENT_NOTE = os.path.join(DATA_DIR, 'student_notes.csv')
STUDENT_TASKS = os.path.join(DATA_DIR, 'student_tasks.csv')
