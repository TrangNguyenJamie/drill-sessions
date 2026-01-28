# Session 01. Command Line Interface (CLI) and Git
Command Line Interface (CLI) is about how we communicate with our computers. Perhaps you are more familiar with working with GUI (Graphical User Interface)s. Web sites and desktop applications with beautiful designs, buttons, text boxes, dropdowns, or even tools such as face detection applications - these are a few examples of GUIs. On the contrary, through CLI, you face a monotone-styled (usually colored in black) window called "terminal", and type in a bunch of texts called "commands", and then wait for your machine to make some changes either locally or remotely. 

[Git](https://git-scm.com/) is a CLI tool for controlling your software being developed, called a Version Control System (VCS). There are other VCS tools such as Perforce, but nowadays the most popular and well-known tool is Git, and many platforms and software support Git. VCS, in a word, is about versioning the current state of your software under development. For example, you want to fix the current state of the software which works perfectly in a production environment. 

## Why do you need CLI and Git?
As a professional software engineer, you need to know how to deal with the CLI, as it is a *Lingua franca* in the software engineering world. You could get by only using some GUI tools, and sometimes using GUI tools is more productive. Nevertheless, knowing CLI is essential to develop and run software, and even using GUI tools requires some knowledge of CLI tools which they are based on.

Git or VCS in a large sense, is also essential for software development. You can track the history of the development of a software, and then roll back if the latest version (called `HEAD` in Git) is not working properly. Or you can make a new change based on the latest version of the software, but without changing a bit of the code in the latest version.

## Exercises
If not instructed otherwise, please make your answer right next to `Answer:` for each of the questions. 

### 1. CLI
The following material is recommended as a reference, but not limited to:
- [Linux Journey](https://labex.io/lesson/the-shell)

1. Turn on a terminal program on your machine. Type in `whoami` in the terminal. What do you see?
- Answer: My username of the current session each machine. e.g.:
    + Window PowerShell/Command Prompt: ```rna\trang.nguyen```
    + WSL: root

2. Move to the cloned repository of the drill sessions in your machine (namely, move to the directory `drill-sessions`). As specified in the main `README.md` of the repo, it is located in your `$HOME` directory. If you don't know what is `$HOME` directory, it is the very first directory that your terminal starts at. Type in `pwd`. What do you see?
- Answer: The path of the current directory. e.g.:
    + ```/C/Users/trang.nguyen/.../drill-sessions```

3. Make a new directory under `sessions/session-01/` with the name `mydir` and create an empty text file `mytext.txt` under it. 
- Which command did you use to move into `sessions/session-01/`? Answer: ```cd sessions/session-01/```
- Which command did you use to create `mydir`? Answer: ```mkdir mydir```
- Which command did you use to create `mytext.txt`? Answer: ```touch mydir/mytext.txt```

4. Copy `mydir` and `mytext.txt` all together under the same `session-01/` directory with the name `copy_mydir`, but with using only one line of command. What did you use?
- Answer: ```cp -r mydir copy_mydir```

5. Move the file `mytext.txt` under `copy_mydir`, and type in `ls` under `sessions/session-01/` directory. What do you see?
- Answer: ```README.md  copy_dir/  mydir/```
    + Assumption: move file mydir/mytext.txt -> copy_mydir/mytext.txt, overwrite the file in copy_mydir
     + ```mv -i mydir/mytext.txt copy_dir```




### 2. Git
Consider the following references first:
- [Atlassian Tutorial](https://nulab.com/learn/software-development/git-tutorial/): A bit advanced and with some depth, but worth reading for understanding concepts.
- [Interactive Git Tutorial](https://learngitbranching.js.org/): Very useful tutorial for understanding concepts. Highly recommended.

These are advanced materials. Not recommended on the first read:
- [MIT's Missing Semester](https://missing.csail.mit.edu/2026/version-control/): Bit advanced, but good to know the theory behind.
- [MIT's CS 6.102](https://web.mit.edu/6.102/www/sp25/): The three chapters Git 1 ~ 3 are bit verbose but worth reading for understanding the concepts.

You might already know a few Git commands. But let's revise basic commands while going through the exercises:

1. What is your current branch?
- Answer:  main

2. If you already make a branch dedicated to this session, good job! But if it is still `main`, let's make a new branch. Name your branch `{{your_name}}-session-01` based on the current `main` branch.

Now run either `git branch` or `git status` to check your current branch. What is your current branch?
- Answer: `jamie-session-01`
    + git checkout -b jamie-session-01

3. Run `git status` in `sessions/session-01/`. What do you see?
- Answer: _Changes not staged for commit_,  including modified file (README.md) and untracked files

4. Add the changes to the stage. Run `git add .` and re-run `git status`. What do you see?
- Answer: _Changes to be committed_, including files mentioned in above question.

5. Now make your changes (kind of) permanent. Make a commit with a message `feat: add answers to the session 01 exercises`. Now you re-run `git status`. What do you see?
- Answer: _On branch jamie-session-01
        nothing to commit, working tree clean_


6. Run `git log --oneline`. What do you see?
- Answer:
    + It show the commit history on the ranch jamie-session-01,not on main. The main is up to date with origin/main that includes earlier commits such as session instructions, README update, initial commit.
    ```46e3987 (HEAD -> jamie-session-01) feat: add answers to the session 01 exercises
    52c8c70 (origin/main, origin/HEAD, main) Merge pull request #1 from UponTheSky/session-01
    2f3ee85 session-01: add session instruction
    b898464 chore: add a few more explanations to the main README
    3857c36 chore: add the main instruction
    f2bf959 Initial commit```
7. Push your changes to your remote repository. But what is your current remote repository(s)? Run `git remote -v`. What do you see?
- Answer:
        ```origin  https://github.com/TrangNguyenJamie/drill-sessions.git (fetch)
        origin  https://github.com/TrangNguyenJamie/drill-sessions.git (push)```

8. Once you push your changes, make a PR and ask for a review. 

9. Read about the following commands. We won't cover them in detail in this session, but you'll encounter them from time to time. Please summarize what each of the commands do.
- `git commit --amend`: 
    + What: Overwrites the latest commit of the working branch (e.g. editting the commit message, adding new changes, rmoving changes from the commit)
    + When: Fix the last commit before pushing
    + Example:
        `git add forgotten_file.txt`
        `git commit --amend`
- `git restore`: 
    + What: Discards changes in the working directory or unstaged files, restore them to a previous state 
    + When: Undo local file changes without affecting commit history
    + Example:
        `git restore myfile.txt`    # throw away local changes, restore myfile.text to the last commited ver
        `git restore --staged`      # remove file from the staging area, when acidentally ran `git add` but don't want to lose the changes
- `git reset`: 
    + What: Moves the current branch pointer (HEAD) to another commit and optionally changes the staing area and working dir
    + When: Undo commits or unstage changes locally
    + Example:
        `git reset --soft HEAD~1`   # Back to 1 commit before the current commit, changes of 'undo commit' still in Staging Area
- `git revert`:
    + What: Create a new commit that reverts the changes of a specific commit
    + When: Undo a commit safely
    + Example:
        `git revert 46e3987`
- `git rebase`:
    + What: Reapplies commits on top ò another base commit,rewriting commit history
    + When: Keep a clean, linear commit history or update a feature branch with the latest main
    + Example:
        `git rebase main`
