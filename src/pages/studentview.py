from dash import html, register_page, dcc, dash_table
import dash_bootstrap_components as dbc
from src.data import student_list, course_list, teacher_list 
from src.callbacks.studentview_callbacks import * 
from src.graphs import attendance_barchart
from datetime import datetime
import dash_ag_grid as dag 

register_page(__name__, path="/student-view", name="Student View")

# Components -- Left Column -- Student Dropdown
student_filter_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Dropdown(
                    id={'type': 'dynamic-input', 'index': 'student-select'},
                    options=student_list(), 
                    value='A', 
                    placeholder='Select a student...', 
                    style={'color':'black'}
                )
            ]
        )
    ],
    className="mb-3 dark-dropdown"
)
# Components -- Left Column -- Student Schedule
default_schedule = [{'Block': '1-1', 'Course': None, 'Teacher': None},
                    {'Block': '1-2', 'Course': None, 'Teacher': None},
                    {'Block': '1-3', 'Course': None, 'Teacher': None},
                    {'Block': '1-4', 'Course': None, 'Teacher': None},
                    {'Block': '2-1', 'Course': None, 'Teacher': None},
                    {'Block': '2-2', 'Course': None, 'Teacher': None},
                    {'Block': '2-3', 'Course': None, 'Teacher': None},
                    {'Block': '2-4', 'Course': None, 'Teacher': None}]

student_schedule_card = dbc.Card(
    [
        dbc.CardHeader('Schedule'),
        dbc.CardBody(
            [
                 dash_table.DataTable(
                id={'type': 'dynamic-output', 'index': 'course-table'},
                columns=[
                    {'name': 'Block', 'id': 'Block'},
                    {'name': 'Course', 'id': 'Course'},
                    {'name': 'Teacher', 'id': 'Teacher'}       
                ],
                data=default_schedule,  
                style_cell={
                    'backgroundColor': "#414141", 
                    'textAlign': 'center', 
                    'fontSize':'0.8rem',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'padding': '5px'
                },
                style_header={
                    'fontWeight': 'bold', 
                    'fontSize':'1rem' , 
                    'backgroundColor': "#242628"
                },
                style_table={
                    'width': '100%',      
                    'overflowX': 'auto' 
                }                                        
            )
            ]
        )
    ],
    className="mb-3"
)
# Components -- Left Column -- WH Insights

workhabit_insights_card = dbc.Card(
    [
        dbc.CardHeader('Work Habit Insights'),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        # 6 Day trend Card
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.Div(
                                        "6-day Trend",
                                        style={
                                            'textAlign': 'center',
                                            'fontSize': '1rem',
                                            'fontWeight': 'bold',
                                            'padding': '10px'
                                        }
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H3(
                                                "",
                                                id={'type': 'dynamic-output', 'index': 'work-habit-icon'},
                                                style={'textAlign': 'center'}
                                            ),
                                            html.Div(
                                                "Trend",
                                                id={"type": "dynamic-output", "index": "work-habit-message"},
                                                style={'textAlign': 'center', 'fontSize':'0.8rem'}
                                            ),
                                        ]
                                    ),
                                ],
                                outline=True,
                                style={'borderColor': 'white', 'borderWidth':'1px'}
                            ),
                            width=6
                        ),

                        # Average Card
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.Div(
                                        "Current Average",
                                        style={
                                            'textAlign': 'center',
                                            'fontSize': '1rem',
                                            'fontWeight': 'bold',
                                            'padding': '10px'
                                        }
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H3(
                                                "",
                                                id={'type': 'dynamic-output', 'index': 'work-habit-icon-avg'},
                                                style={'textAlign': 'center'}
                                            ),
                                            html.Div(
                                                "",
                                                id={'type': 'dynamic-output', 'index': 'work-habit-avg'},
                                                style={'textAlign':'center', 'fontSize':'0.8rem'}
                                            )
                                        ]
                                    ),
                                ],
                                outline=True,
                                style={'borderColor': 'white', 'borderWidth':'1px'}
                            ),
                            width=6
                        ),
                    ],
                    className="g-2"  # spacing between columns
                )
            ]
        )
    ],
    className="mb-3"
)

# Components -- Middle Column -- Workhabits Graphs
workhabit_graphs_card = dbc.Card(
    [
        dbc.CardHeader("Study Habits"),
        dbc.CardBody(
            [
                html.Div([
                    html.Div(
                        [
                            html.Div("Work Habits", style={'whiteSpace': 'nowrap', 'marginRight': '9px'}),
                            dbc.Switch(
                                id={'type': 'dynamic-input', 'index': 'graph-toggle'},
                                value=False,
                                style={"width": "auto", 'paddingTop': '3px'}
                            ),
                            html.Div("Time Spent", style={'whiteSpace': 'nowrap', 'marginLeft': '3px'}),
                        ],
                        style={
                            'fontSize': '0.8rem',
                            'display': 'flex',
                            'alignItems': 'center',    
                            'justifyContent': 'flex-end',
                            'width': '100%'
                        }
                    ),
                    
                    dcc.Graph(
                        id={'type': 'dynamic-output', 'index': 'graph-output'},
                        config={'displayModeBar':False},
                        style={'width':'100%', 'height':'35.5vh'} 
                    ), 
                ], 
                ),
            ]
        )
    ],
    className="mb-3"
)

# Components -- Middle Column -- Notes
notes_card = dbc.Card(
    [
        dbc.CardHeader("Notes"),
        dbc.CardBody(
            [
                dbc.Textarea(
                    id={'type': 'note-input', 'index': 'teacher-notes'}, 
                    placeholder='Type your notes here...', 
                    style={'width':'100%', 
                           'fontSize':'0.8rem', 
                           'height':'100%', 
                           'minHeight':'150px', 
                           'backgroundColor': '#242628',
                            'border': '0.75px solid #FFFFFF',  
                            'color': 'white',
                    }
                ), 
                html.Div([
                # Output message
                    html.Div(id={'type':'dynamic-output','index':'output-msg-note'}, 
                            style={'fontSize':'0.7rem', 'marginTop':'10px', 'marginRight':'10px'}),
                    dbc.Button(
                        'Save', 
                        id={'type': 'dynamic-input', 'index': 'save-note-button'},
                        n_clicks=0, 
                        style={'fontSize':'0.7rem', 'marginTop':'10px'} 
                    ),   
                ], 
                style={
                    'display': 'flex',               
                    'justifyContent': 'flex-end',      
                    'alignItems': 'center',            
                    'width': '100%', 
                    'marginLeft':'auto'                  
                })
            ]
        )
    ],
    className="mb-3"
)

# Components -- Right Column -- Attendance Graphs
initial_attendance_graph = attendance_barchart()  

attendance_graph_card = dbc.Card(
    [
        dbc.CardHeader("Attendance"),
        dbc.CardBody(
            [ 
                html.Div(
                        [
                            html.Div("Overall ", style={'display': 'inline-block', 'whiteSpace': 'nowrap', 'marginRight': '9px'}),
                            dbc.Switch(
                                id={'type': 'dynamic-input', 'index': 'attendance-toggle'},
                                value=False,
                                style={"width": "auto", 'paddingTop': '3px'}
                            ),
                            html.Div("Courses", style={'whiteSpace': 'nowrap', 'marginLeft': '3px'}),
                        ],
                        style={
                            'fontSize': '0.8rem',
                            'display': 'flex',
                            'alignItems': 'center',    
                            'justifyContent': 'flex-end',
                            'width': '100%'
                        }
                ),
                dcc.Graph(
                    id={'type': 'dynamic-output', 'index': 'attendance-graph'},
                    figure=initial_attendance_graph,
                    config={'displayModeBar': False},
                    style={'flex-grow': '1', 'height':'35.5vh'}  
                )
            ]
        )
    ],
    className="mb-3"
)

# Components -- Right Column -- Daily Workhabit Entry 
initial_workhabit_data = [{'Student': '', 'Workhabit Score': '', 'Focus': '', 'Support Attendance': ''}]
# User input options
students_dict = student_list()
students = [i['label'] for i in students_dict]

teachers_dict = teacher_list()
teachers = [i['label'] for i in teachers_dict]

courses_dict = course_list()
courses = [i['label'] for i in courses_dict]

workhabit_entry_card = dbc.Card(
    [
        dbc.CardHeader("Daily Attendance & Work Habit Entry"),
        dbc.CardBody(
            [
                # input table
                dag.AgGrid(
                    id={'type': 'user-input', 'index': 'workhabit-table'},
                    columnDefs=[
                            {'headerName': 'Student', 'field': 'Student', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": students }, 
                            'flex':2, 'minWidth':90},
                            {'headerName': 'WH Score', 'field': 'Workhabit Score', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": ["0", "1", "2", "3", "4"]},
                            'flex':2, 'minWidth':100},
                            {'headerName': 'Subject', 'field': 'Focus', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": ["Art", "English", "French", "Math", "Science", "Socials", "Other"]},
                            'flex':2, 'minWidth':90},
                            {'headerName': 'Attendance', 'field': 'Support Attendance', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": ["P", "L", "A", "AE"]}, 
                            'flex':2, 'minWidth':110}
                        ],
                        rowData=initial_workhabit_data,
                        defaultColDef={
                            'sortable': False, 
                            'filter': False, 
                            'resizable': False,
                            'wrapHeaderText': True,
                            'suppressMovable': True, 
                            'cellStyle': {'fontSize': '0.8rem',
                                            'color': 'white',
                                            'textAlign': 'center',
                                            'padding': '5px'},
                        },
                        style={
                            'width': '100%',
                            'backgroundColor': '#414141',
                            'border': '1px solid #555', 
                            'overflowX' : 'auto'
                        }, 
                        dashGridOptions={
                            "domLayout": "autoHeight",
                            'headerHeight': 35,
                            'rowHeight': 28,
                            "stopEditingWhenCellsLoseFocus": True,
                            "suppressHorizontalScroll": False,
                            "suppressColumnVirtualisation": True, 
           
                        },
                    className="ag-theme-alpine-dark mb-3"
                ),

                html.Div([
                # Left: date picker
                dcc.DatePickerSingle(
                    id={'type': 'dynamic-input', 'index': 'date-picker'},
                    placeholder="Select date",
                    date=datetime.today().date(),
                ),

                # message + buttons
                html.Div([
                    html.Div(
                        id={'index': 'output-msg', 'type': 'dynamic-output'},
                        style={'fontSize': '0.7rem', 'marginRight': '10px'}
                    ),
                    dbc.Button("Add Row",
                            id={'type': 'dynamic-input', 'index': 'add-row-btn'},
                            n_clicks=0,
                            style={'marginRight': '8px', 'fontSize': '0.7rem'}),
                    dbc.Button("Submit",
                            id={'type': 'dynamic-input', 'index': 'submit-btn'},
                            n_clicks=0,
                            style={'fontSize': '0.7rem'})
                ],
                    style={'display': 'flex', 'alignItems': 'flex-start'}
                )
                    ],
                        style={
                            'display': 'flex',
                            'justifyContent': 'space-between',
                            'alignItems': 'flex-start',
                            'width': '100%',
                        }
                    )


           

            ]
        )
    ],
    className="mb-3"
)

# Main Layout
layout = dbc.Container(
    [
        dbc.Row(
            [
                # Left Column
                dbc.Col(
                    [
                        student_filter_card, 
                        student_schedule_card, 
                        workhabit_insights_card
                    ],
                    xs=12,
                    md=3
                ),
                # Middle Column
                dbc.Col(
                    [
                        workhabit_graphs_card,
                        notes_card
                    ],
                    xs=12, 
                    md=5
                ),
                # Right Column 
                dbc.Col(
                    [   
                        attendance_graph_card,
                        workhabit_entry_card
                    ], 
                    xs=12,
                    md=4
                )
            ],
            className="g-3"
        )
    ], 
    fluid=True, 
    className = 'py-1'
)