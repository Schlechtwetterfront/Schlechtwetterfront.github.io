from subprocess import run
from dataclasses import dataclass
from pathlib import Path
from os import chdir, remove, path

@dataclass
class Repo:
    name: str
    url: str
    branch: str

REPOS = [
    Repo('main', 'https://github.com/Schlechtwetterfront/Schlechtwetterfront.github.io.git', 'master'),
    Repo('xsizetools', 'https://github.com/Schlechtwetterfront/xsizetools.git', 'gh-pages'),
    Repo('ze_filetypes', 'https://github.com/Schlechtwetterfront/ze_filetypes.git', 'gh-pages'),
    # Repo('softcry', 'https://github.com/Schlechtwetterfront/softcry.git', 'gh-pages'), # Archived -> read-only
]

REPO_BASE = 'ghpages'

def publish():
    generated_base_dir = Path(path.realpath(__file__)).parent.parent
    root = generated_base_dir.parent / REPO_BASE

    def p(s):
        print('\n' + s)

    for repo in REPOS:
        print('-' * 80)
        p(f'# REPO {repo.name}')

        generated_path = generated_base_dir / repo.name
        repo_path = root / repo.name

        # 1. Ensure repo exists
        if not repo_path.exists():
            p(f'# Cloning...')

            run(f'git clone {repo.url} {repo_path}').check_returncode()

            chdir(repo_path)

            run(f'git config user.name Schlechtwetterfront')
            run(f'git config user.email schlchtwtrfrnt@gmail.com')
        else:
            p(f'# Changing to repo dir {repo_path}...')
            chdir(repo_path)

        # 2. Checkout gh pages branch
        p(f'# Checking out branch {repo.branch}...')
        run(f'git checkout {repo.branch}').check_returncode()

        # 3. Pull latest changes
        p(f'# Pulling...')
        run(f'git pull origin {repo.branch}').check_returncode()

        # 4. Move over new files
        p(f'# Moving files...')
        for filepath in generated_path.glob('*.html'):
            target_path = repo_path / filepath.parts[-1]
            print(f'== {filepath}')
            print(f'-> {target_path}')

            if target_path.exists():
                remove(target_path)

            filepath.rename(target_path)

        if repo.name == 'main':
            file_name = 'css/subpage-style.css'
            css_path = generated_base_dir / file_name
            target_path = repo_path / file_name

            if css_path.exists():
                print(f'== {css_path}')
                print(f'-> {target_path}')

                if target_path.exists():
                    remove(target_path)
                
                css_path.rename(target_path)
        
        # 5. Add, commit, push
        p(f'# Pushing...')
        run(f'git add .')
        run(f'git commit -m "Update docs"')
        run(f'git push origin {repo.branch}')

if __name__ == '__main__':
    publish()