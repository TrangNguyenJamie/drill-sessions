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
- Answer: ```mv 
    + Status quo: The folder tree now is like:

            .
            ├── mydir
            │   └── mytext.txt
            └── copy_mydir
                └── mytext.txt
    + Assumption: 



### 2. Git
Consider the following references first:
- [Atlassian Tutorial](https://nulab.com/learn/software-development/git-tutorial/): A bit advanced and with some depth, but worth reading for understanding concepts.
- [Interactive Git Tutorial](https://learngitbranching.js.org/): Very useful tutorial for understanding concepts. Highly recommended.

These are advanced materials. Not recommended on the first read:
- [MIT's Missing Semester](https://missing.csail.mit.edu/2026/version-control/): Bit advanced, but good to know the theory behind.
- [MIT's CS 6.102](https://web.mit.edu/6.102/www/sp25/): The three chapters Git 1 ~ 3 are bit verbose but worth reading for understanding the concepts.

You might already know a few Git commands. But let's revise basic commands while going through the exercises:

1. What is your current branch?
- Answer:

2. If you already make a branch dedicated to this session, good job! But if it is still `main`, let's make a new branch. Name your branch `{{your_name}}-session-01` based on the current `main` branch.

Now run either `git branch` or `git status` to check your current branch. What is your current branch?
- Answer:

3. Run `git status` in `sessions/session-01/`. What do you see?
- Answer: 

4. Add the changes to the stage. Run `git add .` and re-run `git status`. What do you see?
- Answer:

5. Now make your changes (kind of) permanent. Make a commit with a message `feat: add answers to the session 01 exercises`. Now you re-run `git status`. What do you see?
- Answer:

6. Run `git log --oneline`. What do you see?
- Answer:

7. Push your changes to your remote repository. But what is your current remote repository(s)? Run `git remote -v`. What do you see?
- Answer:

8. Once you push your changes, make a PR and ask for a review. 

9. Read about the following commands. We won't cover them in detail in this session, but you'll encounter them from time to time. Please summarize what each of the commands do.
- `git commit --amend`: 
- `git restore`: 
- `git reset`:
- `git revert`:
- `git rebase`:
