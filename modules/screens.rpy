# screens
screen debug_ui_display():
    layer "debug_ui_layer"

    key _debug_ui_hotkey action Function(toggle_debug_ui)

    if _debug_ui_visible:
        button:
            style "debug_ui"
            focus_mask True
            action NullAction()

            vbox:
                spacing 6

                textbutton ("▼" if _debug_ui_headers["collapsed"] else "▲") + " " + "Debug UI" action ToggleDict(_debug_ui_headers, "collapsed") style "debug_ui_title_accordion"
                if not _debug_ui_headers["collapsed"]:
                    vbox:
                        spacing 8

                        use debug_ui_readme()
                        use debug_ui_language_section()
                        use debug_ui_script_section()


screen debug_ui_readme():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_header("readme_collapsed", "Debug UI Readme")
            if not _debug_ui_headers["readme_collapsed"]:
                vbox:
                    text "This is a Debug UI for Ren'Py games." style "debug_ui_text"
                    text "Press the hotkey (default: Insert) to toggle the visibility of this UI." style "debug_ui_text"
                    textbutton "Close" action Function(toggle_debug_ui) style "debug_ui_button"

screen debug_ui_language_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_header("lang_collapsed", "Language Settings")
            if not _debug_ui_headers["lang_collapsed"]:
                vbox:
                    textbutton "Default Language" action Language(None) style "debug_ui_button"
                    for code in renpy.known_languages():
                        textbutton code action Language(code) style "debug_ui_button"

screen debug_ui_script_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_header("script_collapsed", "Script Position")
            if not _debug_ui_headers["script_collapsed"]:
                vbox:
                    text "File: [_debug_ui_script_pos_filename]" style "debug_ui_text"
                    text "Line: [_debug_ui_script_pos_lineno]" style "debug_ui_text"


# components
screen debug_ui_header(collapsed, header_text):
    textbutton ("▼" if _debug_ui_headers[collapsed] else "▲") + " " + header_text action ToggleDict(_debug_ui_headers, collapsed) style "debug_ui_accordion"
