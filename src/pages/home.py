from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from src.callbacks.home_callbacks import *

# Register the page at path "/"
register_page(__name__, path="/", name="Home")

layout = html.Div(
    [
        html.H1(
                [
                    html.Span(
                        "Welcome to",
                        style={
                            "display": "block",
                            "fontSize": "22px",
                            "fontWeight": "400",
                            "color": "#B5B8C0",
                            "marginBottom": "6px",
                        },
                    ),
                    html.Span(
                        "Synced Support",
                        style={
                            "fontSize": "48px",
                            "fontWeight": "600",
                            "color": "#FFFFFF",
                        },
                    ),
                ],
            style={
                "textAlign": "center",
                "lineHeight": "1.2",
                "marginTop": "100px",
            },
        ),
        html.P(
            "A dashboard for Learning Support Teachers to track their students' deadlines, schedules, attendance, and work habits.",
            className="text-center text-light mb-5"
        ),

        dbc.Modal(
            [
                dbc.ModalHeader("Log In", close_button=False),
                dbc.ModalBody(
                    [
                        dbc.Input(
                            id="login-username",
                            placeholder="Username",
                            type="text",
                            className="mb-3"
                        ),
                        dbc.Input(
                            id="login-password",
                            placeholder="Password",
                            type="password",
                            className="mb-3"
                        ),
                        dbc.Button(
                            "Log In",
                            id="login-button",
                            n_clicks=0,
                            className="w-100 mb-3"
                        ),
                        html.Div(id="login-message", className="text-center", style={"fontSize": "0.9rem"}),
                        dbc.Button(
                            "Enter Demo",
                            id="enter-demo-button",
                            color="primary",
                            n_clicks=0,
                            className="w-100"
                        ),
                    ]
                ),
            ],
            id="landing-modal",
            is_open=True,
            backdrop="static",
            keyboard=False,
            centered=True,
        ),     
        dbc.Row(
            dbc.Col(
                [
                                   
                    html.Div(
                        [
                            html.P(
                                "What's inside? Explore the tabs in the upper right corner. Click below for a description of the components on each tab.",
                                className="text-center text-light mb-3"
                            ),

                            dbc.Card(
                                [
                                    dbc.Button(
                                        "Student View Tab",
                                        id="collapse-button-studentview",
                                        className="text-start w-100 shadow-none text-decoration-none",
                                        n_clicks=0,
                                    ),
                                    dbc.Collapse(
                                        dbc.CardBody([
                                            html.P(
                                                "Select a student and view insight on their day-to-day picture, including: schedule, attendance, and support-block progress.",
                                                className="mb-2"
                                            ),
                                            html.Ul([
                                                html.Li("Schedule: the student's daily class blocks and teachers."),
                                                html.Li("Work Habit Insights: a current average work habit score and a 6-class trend showing whether focus is improving, declining, or steady. Work habit score is out of 4; on-task=4, mostly on-task=2, equally on/off-task=2, mostly off-task=1, off-task=0."),
                                                html.Li("Study Habits Charts: 1) Work Habits: a trend line of work habit scores over time. 2) Time Spent: A breakdown of which subjects the student spends support time on."),
                                                html.Li("Notes: quick reminders you can add, edit, or delete for a student (e.g. an upcoming test)."),
                                                html.Li("Attendance: a bar chart of attendance by course or overall."),
                                                html.Li("Daily Entry: log a student's support-block attendance, work habit score, and subject worked on."),
                                            ], style={"fontSize": "0.9rem"})
                                        ]),
                                        id="card-collapse-studentview",
                                        is_open=False,
                                    )
                                ],
                                className="mb-3"
                            ),

                            dbc.Card(
                                [
                                    dbc.Button(
                                        "Task View Tab",
                                        id="collapse-button-taskview",
                                        className="text-start w-100 shadow-none text-decoration-none",
                                        n_clicks=0,
                                    ),
                                    dbc.Collapse(
                                        dbc.CardBody([
                                            html.P(
                                                "For insight on upcoming deadlines and overdue work for students.",
                                                className="mb-2"
                                            ),
                                            html.Ul([
                                                html.Li("All Upcoming Deadlines: every task due in the next 4 weeks, across all teachers."),
                                                html.Li("Task Table: filter by student to track what they have/haven't completed, or by teacher to see what's coming up for their class."),
                                                html.Li("New Task Entry: add a new assignment, which updates the shared task data."),
                                            ], style={"fontSize": "0.9rem"})
                                        ]),
                                        id="card-collapse-taskview",
                                        is_open=False,
                                    )
                                ],
                                className="mb-4"
                            ),
                        ],
                        style={
                            "border": "1px solid rgba(255, 255, 255, 0.4)",
                            "borderRadius": "12px",
                            "padding": "15px 25px",
                            "maxWidth": "1000px",
                            "margin": "40px auto",
                        }
                    ),                   
               
                ],
                width=12,
                md=8,
                className="mx-auto"
            )
        ),
    ],
    className="text-light"
)