from setuptools import setup
PRC = "load-display pandagles2\naux-display pandagles\nnotify-level warning"
setup(
    name="StickmanWorld", version="0.1.0",
    options={"build_apps": {
        "application_id": "org.stickmanworld.game",
        "android_version_code": 1,
        "android_min_sdk_version": 21,
        "platforms": ["android"],
        "gui_apps": {"StickmanWorld": "main.py"},
        "plugins": ["pandagles2", "pandagles"],
        "extra_prc_data": PRC,
    }},
    classifiers=["Topic :: Games/Entertainment"],
)
