# 'Scale and convert images using PIL'

A final project for 'Automating Real-World Tasks with Python' course.

**Oliver Frolovs, 2020**

This is free and unencumbered software released into the public domain.

## Environment

To set up the development environment, I created the project on the GitHub first. I asked it to add a `.gitignore` for Python and a `README` file. 

I then cloned the repository into my local machine:

```Shell
$ git clone https://github.com/olliefr/google-cert-python-project.git

...

$ cd google-cert-python-project
```

Then I set up a *virtual environment*, using Python 3.8 `venv` module.

```Shell
google-cert-python-project$ python3 -m venv env
```

Activated the environment:

```Shell
google-cert-python-project$ source env/bin/activate
(env) $
```

Installed the Pillow library and recorded the project's dependencies in `requirements.txt:

```Shell
(env) $ pip install pillow

...

(env) $ pip freeze > requirements.txt
```

At this point the environment is ready for writing code.

## Testing

* I generated a few 192x192 test images in JPEG format, using [Lorep Ipsum for Pictures](https://picsum.photos/) service.
* I converted these JPEG images to TIFF format using the [Image Converter](https://www.microsoft.com/en-us/p/image-converter/9pgn31qtzq26)

The resulting test directory is `images_test/`

## Code

The script is named `process.py` as in *to process images*. Since the task description was not terribly precise, and I did not have the test data until I logged into the deployment instance, I had to make changes to the script to make it work on the deployment instance. The main difference was that I had assumed that the source files are going to have file extensions, while the deployed image versions actually had not. 

Nevertheless, I had successfully completed the task.

## Further development

If it were a *real* project, rather than a one-off data conversion script, I would have added unit tests, and set up *Continuous Integration* and *Continious Deployment* facilities.

&mdash; Oliver Frolovs, 2020


