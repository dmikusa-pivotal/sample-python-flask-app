# Python Flask Cloud Foundry Sample App 

A small Python & Flask sample app that can be run on Cloud Foundry.

## Usage

To deploy, just run `cf push` from the root directory.

## Details

The app is deployed to Cloud Foundry and the Python buildpack will run. This installs the version of Python listed in `runtime.txt` and all the dependencies listed in `requirements.txt`. It then sees the `Procfile` and uses this command to start the application.

The `Procfile` is using `gunicorn`, which is preferred for production setups. If you don't want to use `gunicorn`, you could simply replace the command there with `python app.py` to run the app directly.

The `config.py` file is enabling DEBUG mode for Flask. You don't normally want to do this, but it's helpful for this example so it's enabled.

The `app.py` code has various endpoints you can use for debugging & exploration. See the comments in the code for explanations of what they do.