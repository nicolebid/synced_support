from dash.dependencies import Input, Output, State
from src.data import teacher_list, student_list, student_deadlines, teacher_roster, teacher_tasks, save_deleted_changes, save_checked_changes
import pandas as pd 
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
from datetime import datetime, timedelta
from src.config import *
 
def register_callbacks(app):
    
    # dropdown for teacher/student selection (filter 1)
    @app.callback(
        [
            Output({'type': 'dynamic-input', 'index': 'select-item'}, 'options'),
            Output({'type': 'dynamic-input', 'index': 'select-item'}, 'placeholder')
        ],
        Input({'type': 'dynamic-input', 'index': 'select-type'}, 'value')
    )

    # dropdown for name selection (filter 2)
    def update_dropdown(selected_type=None):
        if selected_type == 'Teacher':
            options = teacher_list()
            placeholder = "Select a teacher"
        elif selected_type == 'Student':
            options = student_list()
            placeholder = "Select a student"
        else:
            options = []
            placeholder = ""
        return options, placeholder

    # Task table updates 
    task_default_df = pd.DataFrame([['','','','']]*3)
    @app.callback(
        Output({'type': 'dynamic-input', 'index': 'dynamic-task-tables'}, 'children'), 
        [
            Input({'type': 'dynamic-input', 'index': 'select-type'}, 'value'), 
            Input({'type': 'dynamic-input', 'index': 'select-item'}, 'value'), 
        ],
        prevent_initial_call=True

    )
    def update_content_t2col2(role, name):

        if role == 'Student' and name:
            table_data, selected_indicies = student_deadlines(name)

            return html.Div([
                dash_table.DataTable(
                    id={'type':'dynamic-input', 'index':'student-task-table'}, 
                    columns=[{'name':'Due', 'id':'Due'}, 
                             {'name':'Task', 'id':'Task'}, 
                             {'name':'Course', 'id':'Course'}, 
                             {'name':'Teacher', 'id':'Teacher'}, 
                             {'name':'Block', 'id':'Block'}], 
                    data=table_data,
                    row_selectable='multi', 
                    row_deletable=True, 
                    selected_rows=selected_indicies, 
                    style_cell={'backgroundColor': "#414141", 
                                'textAlign': 'center', 
                                'fontSize':'0.7rem',
                                'whiteSpace': 'normal',
                                 'height': 'auto',
                                 'padding': '5px'
                                },
                    style_header={'fontWeight': 'bold', 'fontSize':'1rem' },
                    style_table={
                        'width': '100%',      
                        'overflowX': 'auto' 
                    }

                ), 
                html.Div([
                    # Output message
                    html.Div(id={'type':'dynamic-output','index':'output-student-task'}, style={'marginRight':'10px','fontSize':'0.7rem'}),

                    # Save button
                    dbc.Button('Save', id={'type': 'dynamic-input', 'index': 'save-student-tasks'}, n_clicks=0, 
                            style={'marginTop': '10px','fontSize':'0.8rem'})
                ], style={
                    'display': 'flex',
                    'justifyContent': 'flex-end',  
                    'marginTop': '10px', 
                    'alignItems': 'center'
                })     
            ])

        elif role == 'Teacher' and name: 

            teacher_roster_dict = teacher_roster(name)
            start = datetime.today() - timedelta(weeks=70)
            end = datetime.today() + timedelta(weeks=3)

            start_str = start.strftime('%Y-%m-%d')
            end_str = end.strftime('%Y-%m-%d')

            teacher_task_dict = teacher_tasks(name, start_str, end_str)
            return html.Div([
                # Table
                html.Div([
                    dash_table.DataTable(
                        columns=[{'name': col, 'id': col} for col in teacher_roster_dict.keys()], 
                        data=[{col: '\n'.join(map(str, students)) for col, students in teacher_task_dict.items()},
                            {col: '\n'.join(map(str, students)) for col, students in teacher_roster_dict.items()}],
                        style_data={'whiteSpace': 'pre-line'},
                        style_cell={'backgroundColor': "#414141", 
                                        'textAlign': 'center', 
                                        'fontSize':'0.8rem',
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'padding': '5px'
                        },
                        style_header={'fontWeight': 'bold', 'fontSize':'1rem' },
                        style_table={
                                'width': '100%',      
                                'overflowX': 'auto' 
                        },  
                    )
                ],
                    className='mb-3'
                ),
            # Date 
            html.Div([
                        dcc.DatePickerRange(
                            id={'type': 'dynamic-input', 'index': 'date-picker-tasks'},
                            start_date_placeholder_text="Start date",
                            end_date_placeholder_text="End date",
                            start_date=start_str,
                            end_date=end_str, 
                            style={'marginBottom':'10px'}
                        ),
                    ],  
                    ),
            ])
        else:
            return html.Div([
                dash_table.DataTable(
                    id='default-table',
                    columns=[{'name': '', 'id': ''}, {'name': '', 'id': ''}, {'name': '', 'id': ''}],
                    data=task_default_df.to_dict('records'),
                    style_table={'height': '200px', 'width': '100%'},
                    style_cell={'backgroundColor': "#414141", 
                                'textAlign': 'center', 
                                'fontSize':'0.8rem',
                                'whiteSpace': 'normal',
                                 'height': 'auto',
                                 'padding': '5px'
                },
                )
            ])
# FIX 1) BELOW
    # Adjust Teacher Assigned Task table when date range is changed
    # @app.callback(
    #     Output({'type': 'dynamic-input', 'index': 'teacher-task-table'}, 'data'),
    #     [
    #         Input({'type': 'dynamic-input', 'index': 'start-date'}, 'data'),
    #         Input({'type': 'dynamic-input', 'index': 'end-date'}, 'data'),
    #         Input({'type': 'dynamic-input', 'index': 'select-item'}, 'value'),  # Teacher selected
    #     ],
    #     prevent_initial_call=True
    # )
    # def update_teacher_task_table(start_date, end_date, teacher_name):
    #     print('Triggered')
    #     if not teacher_name or not start_date or not end_date:
    #         return dash.no_update  # If no teacher or no dates, do not update

    #     # Fetch and filter teacher task data based on the selected date range
    #     teacher_task_dict = teacher_tasks(teacher_name, start_date, end_date)

    #     # Format the teacher's task data to match the table structure
    #     table_data = [{col: '\n'.join(map(str, students)) for col, students in teacher_task_dict.items()}]

    #     return table_data
# FIX two delete "changes saved from student task table "

    # saves user updates on student task table   
    @app.callback(
        Output({'type': 'dynamic-output', 'index': 'output-student-task'}, 'children'),
        Input({'type': 'dynamic-input', 'index': 'save-student-tasks'}, 'n_clicks'),
        State({'type': 'dynamic-input', 'index': 'student-task-table'}, 'data'),
        State({'type': 'dynamic-input', 'index': 'student-task-table'}, 'derived_virtual_selected_rows'),
        State({'type': 'dynamic-input', 'index': 'select-item'}, 'value'), 
        prevent_initial_call=True
    )
    def save_task_updates(n_clicks, data, selected_rows_ind, student_name):
        # current csv
        df_tasks = pd.read_csv(STUDENT_TASKS)
        df_student_tasks  = df_tasks[df_tasks['Student'] == student_name]
        msg = ""
                
        # update status of deleted rows in csv
        if len(df_student_tasks) > len(data):
            msg = save_deleted_changes(data, student_name)
        
        # update status of selected rows in csv
        if selected_rows_ind is not None:
            selected_rows_data = [data[i] for i in selected_rows_ind]
            msg = save_checked_changes(selected_rows_data, student_name)
        return msg