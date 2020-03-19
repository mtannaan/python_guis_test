#!/usr/bin/env bash
pyinstaller \
    --onefile \
    --runtime-tmpdir `pwd`/tmp \
    main_pyqt.py