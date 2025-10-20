from dash import html, register_page, dcc, dash_table
import dash_bootstrap_components as dbc
from src.data import student_list 
from src.callbacks.studentview_callbacks import * 


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
                    style={'color': 'black'},
                )
            ]
        )
    ],
    className="mb-3"
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
                                                id={'type': 'dynamic-output', 'index': 'work-habit-avg'},
                                                style={'textAlign':'center'},
                                                className="card-title"
                                            ),
                                            html.Div(
                                                'Out of 4',
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

            ]
        )
    ],
    className="mb-3"
)

# Components -- Right Column -- Attendance Graphs
attendance_graph_card = dbc.Card(
    [
        dbc.CardHeader("Attendance"),
        dbc.CardBody(
            [

            ]
        )
    ],
    className="mb-3"
)

# Components -- Right Column -- Daily Workhabit Entry 
workhabit_entry_card = dbc.Card(
    [
        dbc.CardHeader("Daily Workhabit Entry"),
        dbc.CardBody(
            [

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