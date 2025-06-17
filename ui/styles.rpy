# base styles
style debug_ui is default:
    background Frame("#1e1e2edd", 12, 12)
    xsize 500
    xalign 0.0
    yalign 0.0
    xmargin 12
    ymargin 12
    ymaximum 600

style debug_ui_accordion is default:
    font debug_ui.font_path
    size 16
    bold True
    background Frame("#2d3748", 8, 8)
    hover_background Frame("#4a5568", 8, 8)
    insensitive_background Frame("#718096", 8, 8)
    xpadding 4
    xmargin 0
    ymargin 2
    xfill True

style debug_ui_accordion_text is default:
    font debug_ui.font_path
    size 16
    bold True
    color "#e2e8f0"
    hover_color "#90cdf4"
    insensitive_color "#a0aec0"

style debug_ui_text is default:
    font debug_ui.font_path
    size 14
    color "#cbd5e0"
    xsize 460
    xalign 0.0
    xpos 20

style debug_ui_button is default:
    background Frame("#3182ce", 6, 6)
    hover_background Frame("#2b77cb", 6, 6)
    insensitive_background Frame("#718096", 6, 6)
    xpadding 8
    ypadding 3
    xmargin 20
    ymargin 2
    xfill True

style debug_ui_button_text is default:
    font debug_ui.font_path
    size 14
    color "#ffffff"
    hover_color "#bee3f8"
    insensitive_color "#a0aec0"
    xalign 0.5

style debug_ui_section is default:
    background Frame("#2a2d3a", 6, 6)
    xfill True

style debug_ui_textinput is default:
    font debug_ui.font_path
    size 16
    xfill True
    yfill True
    background "#00000080"

style debug_ui_textinput_floating is default:
    background Frame("#2a2d3a", 6, 6)
    xfill True
    xalign 0.5
    yalign 0.5
    xmaximum 400

style debug_ui_textinput_section is default:
    background Frame("#2a2d3a", 6, 6)
    xfill True
    xmargin 20
    ymargin 10

style debug_ui_textinput_input is input:
    font debug_ui.font_path
    size 18
    color "#ffffff"


# custom styles
style debug_ui_title_accordion is debug_ui_accordion:
    background Frame("#4651AD", 4, 4)
    hover_background Frame("#5B63C4", 4, 4)

style debug_ui_title_accordion_text is debug_ui_accordion_text:
    color "#e2e8f0"
    hover_color "#90cdf4"


# Override styles
style vscrollbar:
    base_bar Frame("#4a5568", 8, 8)
    thumb Frame("#3182ce", 8, 8)
    hover_thumb Frame("#63b3ed", 8, 8)
    xsize 8
    unscrollable "insensitive"
