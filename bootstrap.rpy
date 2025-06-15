# Debug UI Config
init 10 python:
    config.statement_callbacks.append(debug_ui.track_say_statements)
    config.overlay_during_with = True
    config.always_shown_screens.append('debug_ui_display')
    config.top_layers.append('debug_ui_layer')
