CookieCutter Pip-Project
========================

A cookiecutter template for python projects intended to be pip-installed

[cookiecutter](https://github.com/audreyr/cookiecutter)

Inspired by: [sloria](https://github.com/sloria/cookiecutter-flask.git)


Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/wdm0006/cookiecutter-pipproject.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.


Publishing your project to pypi
-------------------------------

There are two ways to publish your project:

 * the manual way, outlined [here](http://www.willmcginnis.com/2015/11/12/create-a-pip-installable-python-package-in-2-minutes/)
 * and with pypi-publisher [ppp](https://github.com/wdm0006/pypi-publisher)
 
Goals
-----

The goal of this project is simply to take some of the boiler plate out of creating a new python project. It is intended
to stay pretty minimal, but contains everything needed to make a project that includes:

 * Sphinx documentation
 * Installable via pip in pypi
 * Testing via Nose and Coverage

In the future, we may include some other things like:

 * basic travic ci configuration
 * anything else you think might make sense (open up an issue with ideas).
 
Contributing
------------

The intent of this project is to stay fairly lean, but if you have any suggestions or would like to help out, please let me know.

License
-------

BSD licensed.