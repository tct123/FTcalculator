import flet as ft
import dataprotection as dn


def main(page: ft.Page):
    page.auto_scroll = True
    dlg = ft.AlertDialog(
        title=ft.Text(dn.heading),
        content=ft.Column(controls=[ft.Text(dn.content)], scroll=True),
        modal=True,
    )
    page.update()

    def github(e):
        page.launch_url("https://github.com/tct123")

    def dataprotection(e):
        page.launch_url("https://tct123.github.io")

    def dataprotectionpopup(e):
        page.open(dlg)

    page.title = "Calculator"

    # page.window_full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        bgcolor=ft.Colors.BLUE,
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="GitHub", icon=ft.Icons.WEB, on_click=github),
                    ft.PopupMenuItem(
                        text="Dataprotection",
                        icon=ft.Icons.WARNING,
                        on_click=dataprotectionpopup,
                    ),
                ]
            )
        ],
    )

    # page.navigation_bar = ft.NavigationBar(
    #    destinations=[
    #        ft.NavigationDestination(icon=ft.Icons.EXPLORE, label="Explore"),
    #        ft.NavigationDestination(icon=ft.Icons.COMMUTE, label="Commute"),
    #        ft.NavigationDestination(icon=ft.Icons.BOOKMARK_BORDER, label="Explore"),
    #    ],
    #    # bgcolor=ft.Colors.RED,
    # )
    result = ft.TextField(
        text_align=ft.TextAlign.RIGHT,
        expand=1,
        read_only=True,
        border=ft.InputBorder.NONE,
    )

    def btnclick(e):
        if e.control.text == "C":
            result.value = ""
        elif e.control.text == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = "Error"
        else:
            result.value += e.control.text
        result.update()

    buttons = ["789/", "456*", "123-", "0.C+", "(=)"]
    page.add(ft.SafeArea(result))
    for row in buttons:
        row_controls = []
        for btntext in row:
            btn = ft.TextButton(text=btntext, on_click=btnclick, expand=1)
            row_controls.append(btn)
        page.add(
            ft.SafeArea(
                ft.Row(
                    controls=row_controls,
                    expand=1,
                )
            )
        )


ft.app(main)
