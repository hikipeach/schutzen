# schutzen
An CLI password manager that stores your username and password for a given website in a symmetric encrypted vault.

## Table of Contents
- Features
- Installation
- Usage
- Technologies Used
- Contributing

## Features
- Multiple accounts can be stored for a website.
- Master password is hashed using a key derivation algorithm.
- Secure login by comparing the hashes.
- Made a mistake? No Problem. You can update the website you have entered, along with usernames and password.
- You can delete an account associated with a website.
- Sometimes we want to start all over. You can clear all accounts saved for a website.
- If you run into a problem, there is a log file that tells you information running during your program, error messages with debugging.
- Need a better password? Use our password generator. It is saved to your clipboard by default.

## Technologies Used
- Python
- bcrypt, json, os and logging

## Contributing
### Branch Workflow
A branch workflow is used for this project to contribute.
#### Branches
##### Main
- Used for releases
- Represents production code
##### Develop
- Stores completed features 
- Used for the next release
##### Features
- Naming convention feature/feature-name
- Only used for adding new features
- Merged into the develop branch using a pull request
#### Release
- Naming convention release/version-number
- Bug fixes should only be made on this branch
- NO new features
- Final testing occurs
- Version numbers are given

### Instructions
1. Create a new branch for the feature you are working using `git branch feature/{feature-name}`
2. Switch to the new branch.
3. Commit when you are complete one section of your code.
4. When you are finished your feature, push your changes to your branch.
5. Send a pull-request to the **develop** branch.
