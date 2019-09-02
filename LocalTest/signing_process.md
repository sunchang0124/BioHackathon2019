# Signing process

Signing, for every party, is based on the following input information, and processing steps.

## Input information

* Docker image name: name of the docker image
* Docker image ID: SHA1 hash of the docker image (or image ID)
* Git repository URL: link to git repository where it is claimed this container was built with (to inspect the code)

## Process

1. pull the docker image
2. Check whether the docker image compares to the image ID
3. Pull the git repository
4. Run the docker build script inside the git repository
5. Export the built container as a tarball object (`docker save <imagename>`)
6. Export the pulled container as a tarball object (`docker save <imagename>`)
7. Do a comparison on the (extracted) tarball (diff on tarball and files within)
8. If comparison checks out, perform a code review of the git repository
9. If the code review checks out, sign the docker image ID of the image from the docker registry
10. Provide the signed image ID to the TSE

## TSE

Only execute docker images where the signed image ID (which can be decrypted using the private signing key) corresponds to the current docker image (both name and ID).