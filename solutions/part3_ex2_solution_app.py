# PART 3 - Exercise 2 - Solution
# //////////////////////////////
from pathlib import Path
from shiny.express import input, render, ui, app_opts, expressify

# Set the www folder for static assets
app_opts(static_assets=Path(__file__).parent / "www")


# Needed for PART 2 only (not present in PART 1) ---
@expressify
def myTab(tab, image, text):
    with ui.nav_panel(tab):
        with ui.layout_columns(col_widths=[3, 9]):
            with ui.card():
                ui.img(src=image)
            with ui.card():
                ui.p(text)


# ----

with ui.navset_card_tab(id="tab"):
    # Solution for PART 1 ---
    # Tab 1
    with ui.nav_panel("YOUNG"):
        with ui.layout_columns(col_widths=[3, 9]):
            with ui.card():
                ui.img(src="young.jpg")
            with ui.card():
                ui.p("How it all began ...")
    # Tab 2
    with ui.nav_panel("ADULT"):
        with ui.layout_columns(col_widths=[3, 9]):
            with ui.card():
                ui.img(src="adult.jpg")
            with ui.card():
                ui.p("How it all began ...")
    # ---

    # PART 2 ...
    # Tab 3
    myTab("OLD", "old.jpg", "... what I have become")
    # ---
