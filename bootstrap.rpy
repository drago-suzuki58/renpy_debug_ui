init python:
    _debug_ui_script_pos_filename = ""
    _debug_ui_script_pos_lineno = 0
    _debug_ui_visible = True
    _debug_ui_hotkey ="K_INSERT"
    _debug_ui_font_path = "renpy_debug_ui/assets/fonts/MPLUS1p-Regular.ttf"
    _debug_ui_headers = {
        "collapsed": False,
        "readme_collapsed": False,
        "lang_collapsed": False,
        "script_collapsed": False
    }

    def track_say_statements(statement_name):
        global _debug_ui_script_pos_filename, _debug_ui_script_pos_lineno

        targets = [
            "say", "say-bubble", "say-nvl", "say-centered", "menu", "menu-nvl", "menu-with-caption", "menu-nvl-with-caption"
        ]
        if any(statement_name.startswith(t) for t in targets):
            filename, lineno = renpy.get_filename_line()
            _debug_ui_script_pos_filename = filename
            _debug_ui_script_pos_lineno = lineno

    def toggle_debug_ui():
        global _debug_ui_visible
        _debug_ui_visible = not _debug_ui_visible
        renpy.restart_interaction()

    config.statement_callbacks.append(track_say_statements)
    config.overlay_screens.append('debug_ui_display')


# base styles
style debug_ui is default:
    background Frame("#1e1e2edd", 12, 12)
    xalign 0.0
    yalign 0.0
    xmargin 12
    ymargin 12
    xsize 500

style debug_ui_accordion is default:
    font _debug_ui_font_path
    size 16
    background Frame("#2d3748", 8, 8)
    hover_background Frame("#4a5568", 8, 8)
    insensitive_background Frame("#718096", 8, 8)
    xpadding 4
    xmargin 0
    ymargin 2
    xfill True

style debug_ui_accordion_text is default:
    font _debug_ui_font_path
    color "#e2e8f0"
    hover_color "#90cdf4"
    insensitive_color "#a0aec0"
    size 16
    bold True

style debug_ui_text is default:
    font _debug_ui_font_path
    color "#cbd5e0"
    size 14
    text_align 0.0
    xsize 460

style debug_ui_button is default:
    background Frame("#3182ce", 6, 6)
    hover_background Frame("#2b77cb", 6, 6)
    insensitive_background Frame("#718096", 6, 6)
    xpadding 8
    ypadding 3
    xmargin 3
    ymargin 2

style debug_ui_button_text is default:
    font _debug_ui_font_path
    color "#ffffff"
    hover_color "#bee3f8"
    insensitive_color "#a0aec0"
    size 14

style debug_ui_section is default:
    background Frame("#2a2d3a", 6, 6)
    xfill True


# custom styles
style debug_ui_title_accordion is debug_ui_accordion:
    background Frame("#4651AD", 4, 4)
    hover_background Frame("#5B63C4", 4, 4)

style debug_ui_title_accordion_text is debug_ui_accordion_text:
    color "#e2e8f0"
    hover_color "#90cdf4"
    size 16
    bold True


# screens
screen debug_ui_display():
    key _debug_ui_hotkey action Function(toggle_debug_ui)

    if _debug_ui_visible:
        button:
            style "debug_ui"
            focus_mask True
            action NullAction()
            vbox:
                spacing 6
                xfill True

                textbutton ("▼" if _debug_ui_headers["collapsed"] else "▲") + " " + "Debug UI" action ToggleDict(_debug_ui_headers, "collapsed") style "debug_ui_title_accordion"

                if not _debug_ui_headers["collapsed"]:
                    vbox:
                        spacing 8
                        xfill True

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
                    spacing 4
                    xpos 12
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
                    spacing 4
                    xpos 12
                    for code in renpy.known_languages():
                        textbutton code action Language(code) style "debug_ui_button" xsize 100

screen debug_ui_script_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4
            use debug_ui_header("script_collapsed", "Script Position")
            if not _debug_ui_headers["script_collapsed"]:
                vbox:
                    spacing 3
                    xpos 12
                    text "File: [_debug_ui_script_pos_filename]" style "debug_ui_text"
                    text "Line: [_debug_ui_script_pos_lineno]" style "debug_ui_text"


# components
screen debug_ui_header(collapsed, header_text):
    textbutton ("▼" if _debug_ui_headers[collapsed] else "▲") + " " + header_text action ToggleDict(_debug_ui_headers, collapsed) style "debug_ui_accordion"
