import dash_bootstrap_components as dbc
from datetime import datetime
import pandas as pd 
import dash_ag_grid as dag
from collections import OrderedDict
from dash import dash_table, html, dcc
from .data import  student_list, upcoming_deadlines, save_workhabits_data, teacher_list, course_list
from .graphs import attendance_barchart, workhabit_timeline, timespent_barchart

