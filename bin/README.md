You can place any script that use the RS module here, it will pick up by setuptools when installing with pip, just edit `setup.py` with the following:

    setup(
        # ...
        scripts=["bin/example.py"],
        # ...
        )
