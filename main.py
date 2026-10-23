import flet as ft

def main(page: ft.Page):
    page.title = "TradeFlow AI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    bot_status = ft.Text("Statut : Arrêté 🔴", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.RED_400)
    balance_text = ft.Text("Solde : $1,000.00", size=22, weight=ft.FontWeight.BOLD)
    log_view = ft.ListView(expand=1, spacing=5, padding=10, auto_scroll=True)

    def toggle_bot(e):
        if bot_status.value.find("Arrêté") != -1:
            bot_status.value = "Statut : En cours d'exécution 🟢"
            bot_status.color = ft.colors.GREEN_400
            start_stop_btn.text = "Arrêter le Bot"
            start_stop_btn.bgcolor = ft.colors.RED_700
            log_view.controls.append(ft.Text(">>> Bot démarré avec succès. Analyse du marché...", color=ft.colors.GREEN_300))
        else:
            bot_status.value = "Statut : Arrêté 🔴"
            bot_status.color = ft.colors.RED_400
            start_stop_btn.text = "Démarrer le Bot"
            start_stop_btn.bgcolor = ft.colors.GREEN_700
            log_view.controls.append(ft.Text(">>> Bot arrêté par l'utilisateur.", color=ft.colors.RED_300))
        page.update()

    start_stop_btn = ft.ElevatedButton(
        text="Démarrer le Bot",
        icon=ft.icons.PLAY_ARROW,
        bgcolor=ft.colors.GREEN_700,
        color=ft.colors.WHITE,
        on_click=toggle_bot,
        width=200
    )

    page.add(
        ft.Column([
            ft.Text("🤖 TradeFlow AI", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_400),
            ft.Divider(),
            balance_text,
            bot_status,
            ft.Container(height=10),
            start_stop_btn,
            ft.Divider(),
            ft.Text("Journal des activités :", weight=ft.FontWeight.BOLD),
            ft.Container(
                content=log_view,
                bgcolor=ft.colors.BLACK12,
                border_radius=10,
                height=200,
                padding=10,
            )
        ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
