genrule(
    name = "Zephyr",
    srcs = glob([
        "src/backend_view.py",
        "requirements.txt",
        "static/**",
        "templates/**",
        "frontend/css/**",
        "frontend/js/**",
        "frontend/zephyr.html",
    ]),
    outs = ["output.txt"],
    cmd = """
    if [ ! -d "zenv" ]; then
        python3 -m venv zenv
    fi
    source zenv/bin/activate
    pip install Flask
    pip install pywebview
    pip install pyinstaller
    rm -rf build dist
    pyinstaller --onefile --add-data='frontend/css:frontend/css' --add-data='frontend/js:frontend/js' --add-data='frontend/zephyr.html:frontend' --workpath=/tmp --distpath=./dist -n Zephyr src/backend_view.py
    ./dist/Zephyr
    """,
    visibility = ["//visibility:public"],
)
