# gcp-cloudbuild-gae-flex-angular

A sample Angular project to be deployed to Google Cloud App Engine Flexible Environment using Cloud
Build.

## Deploy from your machine with a few commands

- Clone/fork the repository.
- Edit `cloudbuild.yaml` and remove the `--version=$SHORT_SHA` option. It will work only for Cloud
  Build triggered builds.
- Then:

  ```sh
  gcloud auth login
  gcloud config set project <YOUR-PROJECT-ID>
  gcloud builds submit --config cloudbuild.yaml .
  ```

## Get to know the concepts behind this code

[Continuous Delivery in Google Cloud Platform — Cloud Build with App
Engine](https://medium.com/google-cloud/continuous-delivery-in-google-cloud-platform-cloud-build-with-app-engine-8355d3a11ff5)
@ Google Cloud Community / Medium

## Main differences from the App Engine Standard Environment setup (presented in above article)

1. The `app.yaml` file cannot be stored in the root folder due to an App Engine Flexible Environment
   requirement, so I created a `gae-flex` folder to store it.
1. Since the `gae-flex` folder was created, I decided to put all flex environment stuff there.
1. The `main.py` and `requirements.txt` files are required to setup a basic web server (Flask is not
   the best option to serve static content, but helps to let things clear and running in this
   tutorial).
1. All files generated by `npm build...` command are copied to `gae-flex/static` before deploying
   the application to App Engine. Please refer to `cloudbuild.yaml` for details.

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/gcp-cloudbuild-gae-flex-angular/blob/master/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/gcp-cloudbuild-gae-flex-angular/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please
add a comment saying that you encountered the problem as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/gcp-cloudbuild-gae-flex-angular/blob/master/.github/CONTRIBUTING.md)
before making a pull request.
