import dash
from dash.dependencies import Input, Output, State
from dash import html, dash_table, dcc, callback
import dash_bootstrap_components as dbc
from src.config import *
from src.data import student_schedule, workhabit_trend, get_student_note, save_student_note, save_workhabits_data
from src.graphs import attendance_barchart, timespent_barchart, workhabit_timeline
from src.pages.schedule_data import default_schedule
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
            Output({'type': 'dynamic-output', 'index': 'work-habit-avg'}, 'children'), 
            Output({'type': 'dynamic-output', 'index': 'work-habit-icon-avg'}, 'children')
        ],
        Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')
    )
def update_workhabit_card(selected_student):
    if selected_student:
        message, avg, icon_trend, icon_avg = workhabit_trend(selected_student)  
        return message, icon_trend, avg, icon_avg
    return "Trend", "∅", "Score", "∅"
    
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
    
# Update Notes when student is selected
@callback(
    Output({'type': 'note-input', 'index': 'teacher-notes'}, 'value'), 
    Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')
)
def update_notes(student_selected):
    if not student_selected:
        return "Select a student to view/edit notes..."
    else:
        # get to display
        student_note = get_student_note(student_selected)
        if student_note:
            return student_note
        return f"Type notes for {student_selected} here..."

# Update student notes in CSV when save is clicked
@callback(
    [
        Output({'type':'dynamic-output','index':'output-msg-note'}, 'children'),
        Output({'type': 'dynamic-input', 'index': 'save-note-button'}, 'n_clicks')
    ],
    [   
        Input({'type': 'note-input', 'index': 'teacher-notes'}, 'value'),  
        Input({'type': 'dynamic-input', 'index': 'save-note-button'},'n_clicks'),
        Input({'type': 'dynamic-input', 'index': 'student-select'}, 'value')
    ], 
    State({'type': 'note-input', 'index': 'teacher-notes'}, 'value')      
)

def save_notes(note_value, n_clicks, student_selected, current_note_value):
    if student_selected is None or note_value != current_note_value: 
        return '', 0  # clears output message and resets button
    
    if n_clicks > 0: 

        if student_selected and note_value:
            result = save_student_note(student_selected, note_value)
            return result, 0
    return '', 0 

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

# Work Habit Data - User input 
@callback(
    [
        Output({'type': 'user-input', 'index': 'workhabit-table'}, 'rowData'),
        Output({'type': 'dynamic-output', 'index': 'output-msg'}, 'children')
    ],
    [
        Input({'type': 'dynamic-input', 'index': 'add-row-btn'}, 'n_clicks'),
        Input({'type': 'dynamic-input', 'index': 'submit-btn'}, 'n_clicks'),
        Input({'type': 'dynamic-input', 'index': 'date-picker'}, 'date'),
        Input({'type': 'user-input', 'index': 'workhabit-table'}, 'cellValueChanged')
    ],
    State({'type': 'user-input', 'index': 'workhabit-table'}, 'rowData'),
    prevent_initial_call=True
)
def update_table(add_clicks, submit_clicks, date, cell_changed, existing_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        return existing_data, dash.no_update

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Clear message when a cell is edited
    if 'workhabit-table' in triggered_id and cell_changed:
        return dash.no_update, ''

    # Add blank row when clicked
    if 'add-row-btn' in triggered_id:
        existing_data.append({'Student': '', 'Workhabit Score': '', 'Focus': '', 'Support Attendance': ''})
        return existing_data, ''

    # Save submitted data
    elif 'submit-btn' in triggered_id:

        cleaned_data = [row for row in existing_data if any(row.values())] # remove empty rows
        
        # error message for no valid data 
        if not cleaned_data:
            return existing_data, 'No valid data to save.'
        
        saved_message = save_workhabits_data(cleaned_data, date)
        reset_data = [{'Student': '', 'Workhabit Score': '', 'Focus': '', 'Support Attendance': ''}]
        return reset_data, saved_message

    return existing_data, ''