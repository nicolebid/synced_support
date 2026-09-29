import dash
from dash import ctx
import dash.html as html
import dash.dcc as dcc
from datetime import datetime, timedelta
import os
from dash.dependencies import Input, Output, State, MATCH
from dash import dash_table
from src.data import student_list, student_schedule, teacher_list, student_deadlines, teacher_roster, teacher_tasks, get_student_note, save_student_note, save_workhabits_data, save_deadlines_data, save_deleted_changes, save_checked_changes, workhabit_trend, upcoming_deadlines
from src.graphs import attendance_barchart, workhabit_timeline, timespent_barchart
from dash import callback_context
from src.config import * 

def register_universal_callbacks(app):

    # Navbar Callback 
    @app.callback(
        Output("navbar-collapse", "is_open"),
        Input("navbar-toggler", "n_clicks"),
        Input("url", "pathname"),
        State("navbar-collapse", "is_open"),
        prevent_initial_call=False,
    )
    def handle_nav(n_clicks, pathname, is_open):
        ctx = dash.callback_context
        # current state for no trigger 
        if not ctx.triggered:
            return is_open
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # if dropdown clicked -> open 
        if triggered_id == "navbar-toggler":
            return not is_open

        # once option clicked -> close 
        if triggered_id == "url":
            return False

        return is_open

    # Logout Callback - resets demo session and sends user back to the landing page
    @app.callback(
        Output("demo-session", "data", allow_duplicate=True),
        Output("url", "pathname"),
        Input("logout-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def handle_logout(n_clicks):
        return False, "/"