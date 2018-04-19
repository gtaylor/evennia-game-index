Evennia Game Index
==================

This repository contains a not-quite-complete directory listing for Evennia_
games. The idea is to write an optional contrib for Evennia that will let
admin list their games.

This will start out very crude. If adoption is positive, we'll add things
like authentication and some common protections against bad stuff.

For now... naive and simple!

Install
-------

- Push access to a Google App Engine project is needed (evennia-game-index by default).
- Get the Google Cloud SDK (GoogleCloud_) and install according to platform.
- Initialize with `gcloud init` using the relevant Google account and project.
- If google-game-index is the default project, use `gcloud app deploy app.yaml` to deploy, otherwise
  use `--project PROJECT_ID` to specify the project to deploy to.

Support
-------

Limited. But PRs are welcome if there are things not working. 

License
-------

Everything not under the `lib` directory is licensed under the 3-Clause
BSD License.

.. _Evennia: http://evennia.com
.. _GoogleCloud: https://cloud.google.com/sdk
