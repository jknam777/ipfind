[app]
title = ExternalIPApp
package.name = externalipapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 24
android.archs = armeabi-v7a, arm64-v8a
# Permissions (internet needed)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
