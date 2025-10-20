import dash
from dash.dependencies import Input, Output, State
from dash import html, dash_table, dcc, callback
import dash_bootstrap_components as dbc
from src.config import *
from src.data import student_schedule, workhabit_trend
from src.graphs import attendance_barchart, timespent_barchart, workhabit_timeline
from src.pages.studentview import default_schedule

# Updating student schedule when the student is selected 
@callback(
    Output({'type': 'dynamic-output', 'index': 'course-table'}, 'data'), 
    Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value') 
)
def update_schedule(selected_student):
    if selected_student:
        return student_schedule(selected_student)
    return default_schedule

# Workhabit Insight Cards 
@callback(
        [
            Output({'type': 'dynamic-output', 'index': 'work-habit-message'}, 'children'),
            Output({'type': 'dynamic-output', 'index': 'work-habit-icon'}, 'children'), 
            Output({'type': 'dynamic-output', 'index': 'work-habit-avg'}, 'children')
        ],
        Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')
    )
def update_workhabit_card(selected_student):
    if selected_student:
        message, avg, icon = workhabit_trend(selected_student)  
        return message, icon, avg
    return "Trend", "∅", "∅"

# Update attendance graph based on student and graph type 
@callback(
    Output({'type': 'dynamic-output', 'index': 'attendance-graph'}, 'figure'), 
    [
        Input({'type': 'dynamic-input', 'index': 'attendance-toggle'}, 'value'),
        Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')
    ]  
)
def update_attendance_bar_chart(selected_graph, selected_student):
    if not selected_student:
        return attendance_barchart()
    if selected_graph:
        return attendance_barchart(selected_student, False)
    else:
        return attendance_barchart(selected_student, True)
    
# Updating timeline/barchart graph based on student and graph selection 
@callback(
    Output({'type': 'dynamic-output', 'index': 'graph-output'}, 'figure'),
    [Input({'type': 'dynamic-input', 'index': 'graph-toggle'}, 'value'),
    Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')],
)
def update_graph(selected_graph, selected_student):      
    if selected_graph:  
        return timespent_barchart(selected_student)
    else:  
        return workhabit_timeline(selected_student)