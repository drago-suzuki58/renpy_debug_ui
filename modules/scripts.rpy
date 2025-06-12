# Debug UI Tracking
init python:
    _debug_ui_script_pos_filename = ""
    _debug_ui_script_pos_lineno = 0

    def track_say_statements(statement_name):
        global _debug_ui_script_pos_filename, _debug_ui_script_pos_lineno

        targets = [
            "say", "say-bubble", "say-nvl", "say-centered", "menu", "menu-nvl", "menu-with-caption", "menu-nvl-with-caption"
        ]
        if any(statement_name.startswith(t) for t in targets):
            filename, lineno = renpy.get_filename_line()
            _debug_ui_script_pos_filename = filename
            _debug_ui_script_pos_lineno = lineno

    config.statement_callbacks.append(track_say_statements)
