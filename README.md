# Drill Sessions
For those who want to dive into Software Engineering.

## Prerequisites
- We assume that your machine is either macOS, Linux, or WSL, as the sessions will work in Unix environments. 
    - If you can't use even WSL, you should consider using [Git Bash](https://gitforwindows.org/)
- Visual Studio Code will be our IDE. At the moment we don't consider other IDEs.
- [Install Git and do additional setup for your GitHub account](https://docs.github.com/en/get-started/git-basics/set-up-git). We don't enforce how you authenticate your local Git for GitHub. Choose the one that is easiest for you.
- You don't have to install Python separately for now. We will use [`uv`](https://docs.astral.sh/uv/) in later sessions.

## How to get started
1. Fork this repository and clone the forked one on your machine.
- See how to fork if you're not familiar with it: GitHub: [Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
- When you clone this repository, make sure it is located in your `$HOME` directory. If you don't know what the `$HOME` directory means, just run the following command in your terminal:

```sh
git clone ~/{{your_forked_repository_git_address}}
```

2. Read through each `README.md` of the individual sessions under the `/sessions` directory.
Each session consists of three main sections. The first section is a short introduction to tools and concepts. The second one is "Why", which is about why we need to learn the concepts and tools introduced in the session. Lastly, the third one is "Exercises". But rather than listing a bunch of exercises without any context, we will provide necessary materials that will help you solve the problems.

3. Do the exercises specified at the end of the material following the instructions. Make changes on your machine and commit them. 

But make sure that for each session:
- Branch off the `main` branch and name it as `{{your_name}}-session-{{current_session_number}}`, and commit your results on that branch. For example, if your name is `bradley` and the current session is `02`, then the branch name will be `bradley-session-02`. 
- Push your commits and make a PR (Pull Request) to your forked repository.
- Invite `@sungjuyea-rna` to your forked repository and ask for review.
- Once it is approved, merge to the `main` branch.
