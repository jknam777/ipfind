# -*- coding: utf-8 -*-
# ExternalIPApp: Minimal Kivy app that shows your external IP.
#
# Run as Android APK using Buildozer (via GitHub Actions).
# On app start, it fetches https://api.ipify.org and displays the IP.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import threading
import requests

API_URL = "https://api.ipify.org"

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=16, spacing=12, **kwargs)
        self.lbl = Label(text="외부 IP 조회 준비...", font_size="20sp")
        self.btn = Button(text="IP 다시 조회", size_hint=(1, None), height="48dp")
        self.btn.bind(on_release=lambda *_: self.fetch_ip())
        self.add_widget(self.lbl)
        self.add_widget(self.btn)
        Clock.schedule_once(lambda dt: self.fetch_ip(), 0.2)

    def fetch_ip(self):
        self.lbl.text = "조회 중..."
        def task():
            try:
                r = requests.get(API_URL, timeout=8)
                r.raise_for_status()
                ip = r.text.strip()
                Clock.schedule_once(lambda dt: self.set_text(f"현재 공인 IP: [b]{ip}[/b]"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.set_text(f"[color=ff6666]오류: {e}[/color]"), 0)
        threading.Thread(target=task, daemon=True).start()

    def set_text(self, txt):
        self.lbl.markup = True
        self.lbl.text = txt

class ExternalIPApp(App):
    title = "ExternalIPApp"
    def build(self):
        return MainUI()

if __name__ == "__main__":
    ExternalIPApp().run()
