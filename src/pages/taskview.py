from dash import html, register_page, dcc, dash_table
import dash_bootstrap_components as dbc
from src.data import upcoming_deadlines

register_page(__name__, path="/task-view", name="Task View")

# Components -- Left Column -- Filter drop downs
filter_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Dropdown(
                    id={'type': 'dynamic-input', 'index': 'select-type'},
                    options=[
                        {'label': 'Student', 'value': 'Student'},
                        {'label': 'Teacher', 'value': 'Teacher'}
                    ],
                    placeholder='Select Student or Teacher...', 
                    className="mb-3", 
                    style={'color': 'black'},
                ),
                dcc.Dropdown(
                    id={'type': 'dynamic-input', 'index': 'select-item'}, 
                    placeholder='Select name',
                    style={'color': 'black'},
                ),
            ]
        )
    ],
    className="mb-3"
)
# Components -- Left Column -- Upcoming Deadlines 
upcoming_deadlines_card = dbc.Card(
    [
        dbc.CardHeader("Upcoming Deadlines"),
        dbc.CardBody(
            [
               dash_table.DataTable(
                    id={'type': 'dynamic-output', 'index': 'deadlines-table'},
                    columns=[
                        {'name': 'Due', 'id': 'Due'}, 
                        {'name': 'Task', 'id': 'Task'},  
                        {'name': 'Course', 'id': 'Course'}, 
                        {'name': 'Teacher', 'id': 'Teacher'},
                        {'name': 'Block', 'id': 'Block'}
                    ],
                    data=upcoming_deadlines(), 
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
                    }
                )
            ]
        )
    ]
)
# Components -- Right Column -- Task Table
task_table_card = dbc.Card(
    [
        dbc.CardHeader("Task Table"),
        dbc.CardBody(
            [
               html.Div(id={'type': 'dynamic-input', 'index': 'dynamic-task-tables'})
            ]
        )
    ],
    className="mb-3"
)
# Components -- Right Column -- New Task Entry 
## COMPLETE HERE------------------------------------------
##
new_task_card = dbc.Card(
    [
        dbc.CardHeader("New Task Entry"),
        dbc.CardBody(
            [
              
            ]
        )
    ],
    className="mb-3"
)

# ---------------------------------------------------------

# Main Layout 
layout = dbc.Container(
    [
        dbc.Row(
            [
                # Left Column
                dbc.Col(
                    [
                        filter_card, 
                        upcoming_deadlines_card
                    ],
                    xs=12,
                    md=3
                ),
                # Right Column
                dbc.Col(
                    [
                        task_table_card, 
                        new_task_card
                    ],
                    xs=12, 
                    md=9
                ),
            ],
            className="g-3"
        )
    ], 
    fluid=True, 
    className = 'py-1'
)