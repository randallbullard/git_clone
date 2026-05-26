
# Git Clone

## Description
**Git Clone** is a Python script that reads all GitHub repositories available to the authenticated user and downloads them into the current directory.

### Key Features:
- Clones repositories available to the authenticated GitHub user.
- Supports HTTPS and SSH clone URLs.
- Skips repositories when a matching destination directory already exists.

## Prerequisites
- Git installed on your system.
- **Python 3.x** installed.
- An active internet connection.
- Requires **Personal Access Token (PAT)**. PAT is stored as API_KEY in an .env file (not included).
- **Personal Access Token (PAT)** with appropriate scopes required to access target private repositories.

### GitHub PAT Scopes Required:
- `repo` (to access public and private repositories)
- `read:org` (if you want to access private organization repositories)

## Installation
1. Clone the repository containing this script:
    ```bash
    git clone https://github.com/your-username/git_clone_script.git
    ```
2. Navigate to the target directory to save the repo(s):
    ```bash
    cd <TARGET DIRECTORY>
    ```
3. Create and activate a virtual environment. This is recommended so the application uses its own dependency versions instead of whatever is installed globally:
    ```bash
    python -m venv <VIRTUAL_ENV_NAME>
    ```
    ```bash
    source <VIRTUAL_ENV_NAME>/bin/activate
    ```
    On Windows:
    ```powershell
    <VIRTUAL_ENV_NAME>\Scripts\Activate.ps1
    ```
4. Install the application dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the Python script:
```bash
python git_clone.py
```

This will:
- Fetch all repositories (public and private) the authenticated user can access.
- Clone each repository into the current directory.
- Skip repositories when a matching destination directory already exists.

Clone using HTTPS, which is the default:
```bash
python git_clone.py --protocol https
```

Clone using SSH:
```bash
python git_clone.py --protocol ssh
```

Preview clone commands without downloading repositories:
```bash
python git_clone.py --protocol ssh --dry-run
```

## Configuration
A GitHub token is required. The script first checks for `API_KEY` in a `.env` file, then falls back to an existing GitHub CLI login from `gh auth login`.

Example `.env`:
```bash
API_KEY=<PERSONAL_ACCESS_TOKEN>
BASEURL=https://api.github.com
```

### How to Create a Personal Access Token:
1. Go to your GitHub account settings.
2. Navigate to **Developer settings** > **Personal access tokens**.
3. Click on **Generate new token**.
4. Select the required scopes:
    - `repo`: Full control of private repositories.
    - `read:org`: Access private organization repositories (if needed).
5. Generate and **copy** the token (it will only be shown once).

**⚠️ Keep your PAT secure and never share it publicly!**

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.

## License
MIT License

Copyright (c) 2024 Randall Bullard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact
For questions or support, feel free to reach out:
- GitHub: [your-username](https://github.com/randallbullard)
- Email: your.email@example.com
