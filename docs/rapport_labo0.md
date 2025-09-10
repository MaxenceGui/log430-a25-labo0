# Rapport Laboratoire 0

## Questions

### Q1 : Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser?

```bash
================================================================================= FAILURES =================================================================================
______________________________________________________________________________ test_addition _______________________________________________________________________________

    def test_addition():
        my_calculator = Calculator()
        testing_value = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, -1),
            (-2, -3, -5),
            (2.5, 3.5, 6.0)
        ]

        for v1, v2, expected in testing_value:
>           assert my_calculator.addition(v1, v2) == expected
E           assert 0 == -1
E            +  where 0 = addition(0, 0)
E            +    where addition = <src.calculator.Calculator object at 0x000002010BA29E50>.addition

src\tests\test_calculator.py:29: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED src/tests/test_calculator.py::test_addition - assert 0 == -1
======================================================================= 1 failed, 5 passed in 0.08s ========================================================================
```

### Q2: Que fait GitLab pendant les étapes de « setup » et « checkout » ?

Pendant le *setup* github effectue les tâches pour reproduire l'environnement d'exécution de l'application.

#### Set up job

```bash
Current runner version: '2.328.0'
Runner Image Provisioner
  Hosted Compute Agent
  Version: 20250829.383
  Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d
  Build Date: 2025-08-29T13:48:48Z
Operating System
  Ubuntu
  24.04.3
  LTS
Runner Image
  Image: ubuntu-24.04
  Version: 20250907.24.1
  Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20250907.24/images/ubuntu/Ubuntu2404-Readme.md
  Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20250907.24
GITHUB_TOKEN Permissions
  Actions: write
  Attestations: write
  Checks: write
  Contents: write
  Deployments: write
  Discussions: write
  Issues: write
  Metadata: read
  Models: read
  Packages: write
  Pages: write
  PullRequests: write
  RepositoryProjects: write
  SecurityEvents: write
  Statuses: write
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@v3' (SHA:f43a0e5ff2bd294095638e18286ca9a3d1956744)
Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Complete job name: build
```

#### Checkout Dépot

```bash
Run actions/checkout@v3
  with:
    repository: MaxenceGui/log430-a25-labo0
    token: ***
    ssh-strict: true
    persist-credentials: true
    clean: true
    sparse-checkout-cone-mode: true
    fetch-depth: 1
    fetch-tags: false
    lfs: false
    submodules: false
    set-safe-directory: true
Syncing repository: MaxenceGui/log430-a25-labo0
Getting Git version info
  Working directory is '/home/runner/work/log430-a25-labo0/log430-a25-labo0'
  /usr/bin/git version
  git version 2.51.0
Temporarily overriding HOME='/home/runner/work/_temp/0c509cc8-f46b-40c3-b422-c6f3b661e883' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/log430-a25-labo0/log430-a25-labo0
Deleting the contents of '/home/runner/work/log430-a25-labo0/log430-a25-labo0'
Initializing the repository
  /usr/bin/git init /home/runner/work/log430-a25-labo0/log430-a25-labo0
  hint: Using 'master' as the name for the initial branch. This default branch name
  hint: is subject to change. To configure the initial branch name to use in all
  hint: of your new repositories, which will suppress this warning, call:
  hint:
  hint: 	git config --global init.defaultBranch <name>
  hint:
  hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
  hint: 'development'. The just-created branch can be renamed via this command:
  hint:
  hint: 	git branch -m <name>
  hint:
  hint: Disable this message with "git config set advice.defaultBranchName false"
  Initialized empty Git repository in /home/runner/work/log430-a25-labo0/log430-a25-labo0/.git/
  /usr/bin/git remote add origin https://github.com/MaxenceGui/log430-a25-labo0
Disabling automatic garbage collection
  /usr/bin/git config --local gc.auto 0
Setting up auth
  /usr/bin/git config --local --name-only --get-regexp core\.sshCommand
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
  /usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
  /usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
Fetching the repository
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +63afb1a1e69dc7f28fdeef103ada792eb243e97d:refs/remotes/origin/main
  remote: Enumerating objects: 34, done.
  remote: Counting objects:   2% (1/34)
  remote: Counting objects:   5% (2/34)
  remote: Counting objects:   8% (3/34)
  remote: Counting objects:  11% (4/34)
  remote: Counting objects:  14% (5/34)
  remote: Counting objects:  17% (6/34)
  remote: Counting objects:  20% (7/34)
  remote: Counting objects:  23% (8/34)
  remote: Counting objects:  26% (9/34)
  remote: Counting objects:  29% (10/34)
  remote: Counting objects:  32% (11/34)
  remote: Counting objects:  35% (12/34)
  remote: Counting objects:  38% (13/34)
  remote: Counting objects:  41% (14/34)
  remote: Counting objects:  44% (15/34)
  remote: Counting objects:  47% (16/34)
  remote: Counting objects:  50% (17/34)
  remote: Counting objects:  52% (18/34)
  remote: Counting objects:  55% (19/34)
  remote: Counting objects:  58% (20/34)
  remote: Counting objects:  61% (21/34)
  remote: Counting objects:  64% (22/34)
  remote: Counting objects:  67% (23/34)
  remote: Counting objects:  70% (24/34)
  remote: Counting objects:  73% (25/34)
  remote: Counting objects:  76% (26/34)
  remote: Counting objects:  79% (27/34)
  remote: Counting objects:  82% (28/34)
  remote: Counting objects:  85% (29/34)
  remote: Counting objects:  88% (30/34)
  remote: Counting objects:  91% (31/34)
  remote: Counting objects:  94% (32/34)
  remote: Counting objects:  97% (33/34)
  remote: Counting objects: 100% (34/34)
  remote: Counting objects: 100% (34/34), done.
  remote: Compressing objects:   3% (1/27)
  remote: Compressing objects:   7% (2/27)
  remote: Compressing objects:  11% (3/27)
  remote: Compressing objects:  14% (4/27)
  remote: Compressing objects:  18% (5/27)
  remote: Compressing objects:  22% (6/27)
  remote: Compressing objects:  25% (7/27)
  remote: Compressing objects:  29% (8/27)
  remote: Compressing objects:  33% (9/27)
  remote: Compressing objects:  37% (10/27)
  remote: Compressing objects:  40% (11/27)
  remote: Compressing objects:  44% (12/27)
  remote: Compressing objects:  48% (13/27)
  remote: Compressing objects:  51% (14/27)
  remote: Compressing objects:  55% (15/27)
  remote: Compressing objects:  59% (16/27)
  remote: Compressing objects:  62% (17/27)
  remote: Compressing objects:  66% (18/27)
  remote: Compressing objects:  70% (19/27)
  remote: Compressing objects:  74% (20/27)
  remote: Compressing objects:  77% (21/27)
  remote: Compressing objects:  81% (22/27)
  remote: Compressing objects:  85% (23/27)
  remote: Compressing objects:  88% (24/27)
  remote: Compressing objects:  92% (25/27)
  remote: Compressing objects:  96% (26/27)
  remote: Compressing objects: 100% (27/27)
  remote: Compressing objects: 100% (27/27), done.
  remote: Total 34 (delta 0), reused 23 (delta 0), pack-reused 0 (from 0)
  From https://github.com/MaxenceGui/log430-a25-labo0
   * [new ref]         63afb1a1e69dc7f28fdeef103ada792eb243e97d -> origin/main
Determining the checkout info
Checking out the ref
  /usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
  Switched to a new branch 'main'
  branch 'main' set up to track 'origin/main'.
/usr/bin/git log -1 --format='%H'
'63afb1a1e69dc7f28fdeef103ada792eb243e97d'
```

### Q3 : Quel approache et quelles commandes avez-vous exécutées pour automatiser le déploiement continu de l'application dans la machine virtuelle ?

### Q4 : : Quel type d'informations pouvez-vous obtenir via la commande « top » ?
