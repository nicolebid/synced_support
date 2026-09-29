from dash import html, register_page, dcc, dash_table
import dash_bootstrap_components as dbc
from src.data import upcoming_deadlines, student_list, course_list, teacher_list
import dash_ag_grid as dag 
from src.callbacks.taskview_callbacks import * 

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
                    className="mb-3"                   
                ),
                dcc.Dropdown(
                    id={'type': 'dynamic-input', 'index': 'select-item'}, 
                    placeholder='Select name',
                    className="mb-3"
                ),
                html.Div([
                    dcc.DatePickerRange(
                        id={'type':'dynamic-input', 'index':'date-picker-tasks'},
                        start_date=(FROZEN_TODAY - timedelta(weeks=3)).strftime('%Y-%m-%d'),
                        end_date=(FROZEN_TODAY + timedelta(weeks=3)).strftime('%Y-%m-%d'), 
                        
                    )
                ],id={'type':'dynamic-input', 'index':'teacher-date-picker-container'}, style={'display':'none'})
            ]
        )
    ],
    className="mb-3"
)

# Components -- Left Column -- Upcoming Deadlines 
upcoming_deadlines_card = dbc.Card(
    [
        dbc.CardHeader("All Upcoming Deadlines (Within 4 Weeks)"),
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

                                },
                    style_header={'fontWeight': 'bold', 'fontSize':'1rem' , 'backgroundColor': "#242628", },
                    style_table={
                        'width': '100%',      
                        'overflowX': 'auto', 
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
initial_deadlines_data = [{'Task': '', 'Course': '', 'Block': '', 'Teacher': '', 'Due':''}]

# User input options
students_dict = student_list()
students = [i['label'] for i in students_dict]
teachers_dict = teacher_list()
teachers = [i['label'] for i in teachers_dict]
courses_dict = course_list()
courses = [i['label'] for i in courses_dict]

new_task_card = dbc.Card(
    [
        dbc.CardHeader("New Task Entry"),
        dbc.CardBody(
            [
                html.Div([
                    # Table input
                    dag.AgGrid(
                        id={'type': 'user-input', 'index': 'deadlines-table'}, 
                        columnDefs=[
                            {'headerName': 'Task', 'field': 'Task', 'editable': True, 'flex':2, 'minWidth':150},
                            {'headerName': 'Course', 'field': 'Course', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": courses },'flex':2, 'minWidth':120},
                            {'headerName': 'Block', 'field': 'Block', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": ['1-1','1-2','1-3','1-4','2-1','2-2','2-3','2-4'] }, 'flex':1, 'minWidth':80},
                            {'headerName': 'Teacher', 'field': 'Teacher', 'editable': True, 
                            'cellEditor':'agSelectCellEditor', "cellEditorParams": {"values": teachers}, 'flex':2, 'minWidth':120},
                            {'headerName': 'Due', 'field': 'Due', 'editable': True, "cellDataType": "dateString", 'flex':1, 'minWidth':90}
                        ],
                        rowData=initial_deadlines_data, 
                        defaultColDef={
                            'sortable': False,
                            'filter': False,
                            'resizable': False,
                            'wrapHeaderText': True,
                            'suppressMovable': True,
                            'cellStyle': {
                                'fontSize': '0.8rem',
                                'color': 'white',
                                'textAlign': 'center',
                                'padding': '5px',
                            },
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
                        className="ag-theme-alpine-dark",
                    ),

                    # Button - add row/submit data
                    html.Div([
                        # Output message
                        html.Div(id={'index':'output-msg-deadlines','type':'dynamic-output'}, style={'marginRight':'10px', 'fontSize':'0.7rem'}), 
                        dbc.Button("Add Row", id={'type': 'dynamic-input', 'index': 'add-row-deadlines'}, n_clicks=0, style={'marginRight':'10px', 'fontSize':'0.7rem'}),
                        dbc.Button("Submit", id={'type': 'dynamic-input', 'index': 'submit-deadlines'}, n_clicks=0, style={'fontSize':'0.7rem'})
                    ], style={
                        'display': 'flex',
                        'justifyContent': 'flex-end',  
                        'marginTop': '10px', 
                        'alignItems': 'center'} 
                    ), 
                    dcc.Store(id={'index':'csv-write-flag','type':'dynamic-output'}, data=False)                    
                ],
                    style={"overflowX": "auto",  "width": "100%"} 
                ),
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