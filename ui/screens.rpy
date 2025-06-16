# screens
screen debug_ui_display():
    layer "debug_ui_layer"

    key debug_ui.hotkey action Function(debug_ui.toggle_visibility)

    if debug_ui.visible:
        button:
            style "debug_ui"
            focus_mask True
            action NullAction()

            vbox:
                spacing 6

                textbutton ("[DBG]▼" if debug_ui.accordions["collapsed"] else "[DBG]▲") + " " + "Debug UI" action ToggleDict(debug_ui.accordions, "collapsed") style "debug_ui_title_accordion"
                if not debug_ui.accordions["collapsed"]:
                    vbox:
                        spacing 8

                        use debug_ui_readme()
                        use debug_ui_language_section()
                        use debug_ui_script_section()
                        use debug_ui_information_section()


screen debug_ui_readme():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("readme_collapsed", "[DBG]Debug UI Readme")
            if not debug_ui.accordions["readme_collapsed"]:
                vbox:
                    text "[DBG]This is a Debug UI for Ren'Py games." style "debug_ui_text"
                    text "[DBG]Press the hotkey (default: Insert) to toggle the visibility of this UI." style "debug_ui_text"
                    textbutton "[DBG]Close" action Function(debug_ui.toggle_visibility) style "debug_ui_button"

screen debug_ui_language_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("lang_collapsed", "[DBG]Language Settings")
            if not debug_ui.accordions["lang_collapsed"]:
                vbox:
                    textbutton "[DBG]Default Language" action Language(None) style "debug_ui_button"
                    for code in renpy.known_languages():
                        textbutton DBG + code action Language(code) style "debug_ui_button"

screen debug_ui_script_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("script_collapsed", "[DBG]Script Position")
            if not debug_ui.accordions["script_collapsed"]:
                vbox:
                    text "[DBG]File: [debug_ui.script_pos_filename]" style "debug_ui_text"
                    text "[DBG]Line: [debug_ui.script_pos_lineno]" style "debug_ui_text"

screen debug_ui_information_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("information_collapsed", "[DBG]Information Metrics")
            if not debug_ui.accordions["information_collapsed"]:
                python:
                    try:
                        renderer_info = renpy.get_renderer_info()
                        renderer_name = renderer_info.get("renderer", "Unknown") if renderer_info else "Unknown"
                        physical_size_x, physical_size_y = renpy.get_physical_size()
                    except:
                        renderer_name = "Unknown"

                vbox:
                    text "[DBG]Screen" style "debug_ui_text" size 20
                    text "[DBG]Screen Size: [config.screen_width]x[config.screen_height]" style "debug_ui_text"
                    text "[DBG]Window Size: [physical_size_x]x[physical_size_y]" style "debug_ui_text"
                    text "[DBG]Renderer: [renderer_name]" style "debug_ui_text"
                    text "[DBG]Fullscreen: [preferences.fullscreen]" style "debug_ui_text"

                    text "[DBG]System" style "debug_ui_text" size 20
                    text "[DBG]Ren'Py: [renpy.version_string]" style "debug_ui_text"
                    text "[DBG]Platform: [renpy.platform]" style "debug_ui_text"


# components
screen debug_ui_accordion(collapsed, header_text):
    textbutton ("[DBG]▼" if debug_ui.accordions[collapsed] else "[DBG]▲") + " " + header_text action ToggleDict(debug_ui.accordions, collapsed) style "debug_ui_accordion"
