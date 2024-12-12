import marimo

__generated_with = "0.9.31"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    name = "Jess"
    return (name,)


@app.cell
def __(name):
    name.upper()
    return


@app.cell
def __():
    import pandas as pd

    last_names = ["Connor", "Connor", "Reese"]
    first_names = ["Sarah", "John", "Kyle"]
    df = pd.DataFrame(
        {
            "first_name": first_names,
            "last_name": last_names,
        }
    )
    df
    return df, first_names, last_names, pd


@app.cell
def __(mo):
    ## Markdown
    mo.md("""
    This is a markdown text
    ### H3
    """)
    return


@app.cell
def __(mo):
    ## Text Input
    username = mo.ui.text(placeholder="Username").form()
    username
    return (username,)


@app.cell
def __(username):
    username.value
    return


@app.cell
def __(mo):
    password = mo.ui.text(placeholder="Pass",kind="password").form()
    password 
    return (password,)


@app.cell
def __(password):
    password.value 
    return


@app.cell
def __(mo):
    # Text Area
    message = mo.ui.text_area(label="Message").form()
    message
    return (message,)


@app.cell
def __(message, mo):
    mo.md(f"""
    ### Your Messages
    {message.value}
    """)
    return


@app.cell
def __(mo):
    # Number
    age = mo.ui.number(label="Age",start=10,stop=110)
    age
    return (age,)


@app.cell
def __(age):
    age.value
    return


@app.cell
def __(mo):
    # Date Input
    date = mo.ui.date()
    date
    return (date,)


@app.cell
def __(date):
    date.value
    return


@app.cell
def __(mo):
    date_time = mo.ui.datetime()
    date_time 
    return (date_time,)


@app.cell
def __(date_time):
    date_time.value
    return


@app.cell
def __(mo):
    import datetime as dt 
    date_range = mo.ui.date_range(
        start=dt.date(2024, 1, 1), stop=dt.date(2024, 12, 31)
    )
    date_range
    return date_range, dt


@app.cell
def __(mo):
    # Radio & Checkbox
    gender = mo.ui.radio(options=["male", "female", "other"], value="male", label="choose one",inline=True)
    gender
    return (gender,)


@app.cell
def __(mo):
    # Checkbox
    is_active = mo.ui.checkbox(label="Active")
    is_active
    return (is_active,)


@app.cell
def __(mo):
    # Sliders
    height = mo.ui.slider(label="Height",start=50,stop=200)
    height
    return (height,)


@app.cell
def __(mo):
    weight = mo.ui.range_slider(label="Weight",start=50,stop=200)
    weight 
    return (weight,)


@app.cell
def __(mo):
    mass = mo.ui.number(label="Mass")
    return (mass,)


@app.cell
def __(mass):
    mass
    return


@app.cell
def __(height, mass):
    def bmi(mass,height):
        return mass.value/height.value*2
    bmi_value = bmi(mass,height)
    bmi_value
    return bmi, bmi_value


@app.cell
def __(mo):
    ct_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="increment"
    )
    ct_button
    return (ct_button,)


@app.cell
def __(ct_button):
    ct_button.value
    return


@app.cell
def __(pd):
    ### Data
    data = [{'Name': 'Tom', 'Age': 20},
            {'Name': 'nick', 'Age': 21},
            {'Name': 'krish', 'Age': 19},
            {'Name': 'jack', 'Age': 18}]

    df2 = pd.DataFrame(data)
    return data, df2


@app.cell
def __(df2):
    df2
    return


@app.cell
def __(df2, mo):
    # Render as a table
    table = mo.ui.table(data=df2,pagination=True,page_size=2)
    table
    return (table,)


@app.cell
def __(df2, mo):
    # Render as a dataframe
    mo.ui.dataframe(df2)
    return


@app.cell
def __(df, mo):
    # Render as data explorer
    mo.ui.data_explorer(df)
    return


@app.cell
def __(mo):
    ### Media
    mo.image(src="image.png",rounded=True,caption="This is an image")
    return


@app.cell
def __(mo):
    # Video
    mo.video(
        src="https://v3.cdnpk.net/videvo_files/video/free/2013-08/large_watermarked/hd0992_preview.mp4",
        controls=False,
    )
    return


@app.cell
def __(mo):
    # PDF 
    mo.pdf(
        src="https://arxiv.org/pdf/2104.00282.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell
def __(mo):
    ### Files: Upload
    mo.ui.file()
    return


@app.cell
def __(mo):
    # Multiple Files
    f = mo.ui.file(filetypes=[".png", ".jpg"], multiple=True)
    f
    return (f,)


@app.cell
def __(f):
    f.name()
    return


@app.cell
def __(f, mo):
    mo.image(src=f.contents())
    return


@app.cell
def __(f):
    f.value[0].name
    return


@app.cell
def __(mo):
    download_txt = mo.download(
        data="Hello, marimo!".encode("utf-8"),
        filename="hello.txt",
        mimetype="text/plain",
    )
    download_txt
    return (download_txt,)


@app.cell
def __(mo):
    mo.ui.file_browser()
    return


@app.cell
def __(mo):
    ### Composite UI 
    custom_form = mo.ui.array([mo.ui.slider(1,20),
    mo.ui.text()])
    custom_form
    return (custom_form,)


@app.cell
def __(custom_form):
    custom_form.value
    return


@app.cell
def __(mo):
    # Tabs
    tab1 = mo.ui.date()

    tab2 = mo.md("You can show arbitrary content in a tab.")

    tabs = mo.ui.tabs({
        "Heading 1": tab1,
        "Heading 2": tab2
    })
    tabs 
    return tab1, tab2, tabs


@app.cell
def __(mo):
    mo.accordion({"LLM": mo.md("""Large Language Model"""),"SLM":mo.md("Small Language Model")})
    return


@app.cell
def __(mo):
    mo.sidebar(
        [
            mo.md("# marimo"),
            mo.nav_menu(
                {
                    "#home": f"{mo.icon('lucide:home')} Home",
                    "#about": f"{mo.icon('lucide:user')} About",
                    "#contact": f"{mo.icon('lucide:phone')} Contact",
                    "Links": {
                        "https://twitter.com/marimo_io": "Twitter",
                        "https://github.com/marimo-team/marimo": "GitHub",
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return


@app.cell
def __(mo):
    # Stateless Layout UI Element
    mo.carousel([mo.md("This is a stateless"), mo.ui.text_area()])
    return


@app.cell
def __(mo):
    mo.center(mo.md("THis is center"))
    return


@app.cell
def __(mo):
    mo.left(mo.md("THis is center"))
    return


@app.cell
def __(mo):
    mo.right(mo.md("THis is center"))
    return


@app.cell
def __(mo):
    mo.hstack([mo.md("THis is center"),mo.md("THis is hstack")])
    return


@app.cell
def __(mo):
    mo.vstack([mo.md("THis is center"),mo.md("THis is vstack")])
    return


@app.cell
def __():
    ### Plot
    # import altair as alt
    # import marimo as mo
    # from vega_datasets import data

    # chart = (
    #     alt.Chart(data.cars())
    #     .mark_point()
    #     .encode(
    #         x="Horsepower",
    #         y="Miles_per_Gallon",
    #         color="Origin",
    #     )
    # )

    # chart = mo.ui.altair_chart(chart)
    return


@app.cell
def __(mo):
    ## Status
    with mo.status.progress_bar(total=10) as bar:
        for i in range(10):
            ...
            bar.update()
    return bar, i


@app.cell
def __(mo):
    for i2 in mo.status.progress_bar(range(10)):
        print(i2)
    return (i2,)


@app.cell
def __(mo):
    mo.status.spinner(title="Loading Marimo")
    return


@app.cell
def __(mo):
    ### diagrams
    mo.mermaid('''
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    ''')
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
