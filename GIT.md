## GPG
Signing a commit with GPG key

1. Create my GPG key
# <https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key>
# <https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>
# <https://www.nisum.com/nisum-knows/use-public-and-private-keys-for-git-commits-with-gpg>

2. Configure GIT with my GPG key
GITHUB Signing my commits with my private GPG key

   2.1. Get my private key from
        gpg --list-keys
   2.2  git config --global user.email "naftalysh@gmail.com"
   2.3  git config --global user.signingkey my_key
   2.4  git config --global gpg.program "$(which gpg)" # configure the gpg program for git
   2.5  git config commit.gpgsign true # tell git to always sign commits via configuration
   2.6  git commit --amend -S -s # per the last commit

        Write commit message in the following format example: (Max length = 72 characters)
        "
        feat (featureNumber) : commit subject
        Signed-Off-By: Naftaly Shprai <naftalysh@gmail.com>
        "

# Questions
    Q1: Is there a way to add a signature to an already recorded commit?

    A1: (<https://superuser.com/questions/397149/can-you-gpg-sign-old-commits>)
    If not wanting to edit the commit - git rebase --exec 'git commit --amend --no-edit -n -S' -i main
    If wanting to edit the commit - git rebase --exec 'git commit --amend -n -S' -i main

    Q2: How to remove a file from the last commit
    A2: git rm filename-to-remove
        git commit --amend -S -s
        git push -f

## GIT
# Set VS Code as Default Git Editor:
git config --global core.editor "code --wait"

# Verifying the Configuration
git config --global --edit

# To add only tracked files (--update, stages modifications and deletions of tracked files but does not stage new untracked files)
git add -u

## initial branch setup
# Create a new branch where you can save any changes you make during this exercise
git checkout -b branch-name
git push -u origin branch-name

# get remote connected repos
git remote -v

# see all branches
git branch -a

# get git status
git status

# set upstream branch aligned with current local branch
git push -u origin HEAD


# Revert a commit - <https://gist.github.com/gunjanpatel/18f9e4d1eb609597c50c2118e416e6a6>
git revert {commit_id} # Revert the full commit

# Delete the last commit
git reset HEAD^ --hard
git push origin -f

# lint GIT commits
gitlint --commits origin/main..HEAD

# If you want to check whether your rules are properly discovered by gitlint, you can use the --debug flag
# <https://jorisroovers.com/gitlint/user_defined_rules/>

gitlint -d
gitlint --debug --extra-path examples/

# To restore the go.mod and go.sum files from an upstream branch
1. Fetch the Latest Changes from Upstream
   git fetch origin
2. Check Out the Files from Upstream Branch
   git checkout origin/main -- go.mod go.sum
3. Commit the Changes
   git commit -m "Restore go.mod and go.sum from upstream"

# Proposed commit format:
feat(JIRA issue prefix Ex: projectID-JIRANumber): JIRA subject

commit description.

Signed-Off-By: Naftaly Shprai <naftalysh@gmail.com>


# How do I revert git add action?
To revert a git add action, you can use the git reset command with the HEAD option. This will unstage the files that you have added with git add but not committed yet.
Here are the steps to revert a git add action:
1. Check the status of your repository using git status to see which files have been staged with git add.
2. Use the git reset command with the HEAD option to unstage the files that you have added. For example, to unstage a single file named file1.txt,
   run the command:

   git reset HEAD file1.txt

3. To unstage all files that you have added, run the command:
   git reset HEAD
   This will unstage all changes you have added, but not committed.

4. You can verify that the changes have been unstaged by running git status again.
   The files that you unstaged should be listed as "Changes not staged for commit".

   Note: this will only unstage the changes you have added but not committed yet. If you have already committed the changes,
         you will need to use git revert or git reset to undo the commit.

# GIT - To make git ignore the deleted files, you can use the following command:
git rm --cached file1 file2

# GIT sync with PR pull request's state

# Create a new branch based on the pull request
# Step 1: Fetch the pull request with ID 123 into a new branch named new-branch-name
git fetch upstream pull/123/head:new-branch-name

# Step 2: Check out the new branch
git checkout new-branch-name

# This command fetches the pull request with ID 123 from the upstream remote


#
# git clone a branch in a repository into a target directory
git clone -b feature-xyz https://github.com/user/project.git  my-directory
# Cloned feature-xyz branch in https://github.com/user/project.git into  my-directory


# Search a repository org_name/repo_name for PR's from a user username
1. Browse into https://org_name/repo_name.git and and filter by Pool requests
2. In the search panel type - repo:org_name/repo_name  from: username


# explain git statsh

It appears that you meant to ask about git stash. Git stash is a command that allows you to temporarily save changes in your working directory and index (staged changes) that you don't want to commit yet. This is useful when you're in the middle of working on something, but you need to switch to another branch or task without committing the current changes.

Here's a brief overview of how to use git stash:

1. To stash your changes, run the following command:
   git stash

# This will save your changes in a new stash and revert your working directory and index to the last commit.

2. You can also provide a message to describe the stash:
   git stash save "A descriptive message about the stash"

3. To view a list of all stashes, run:
   git stash list

# This will show you a list of stashes with their references, like stash@{0}, stash@{1}, etc.

4. To apply a stash and restore the changes to your working directory, run:
   git stash apply stash@{0}

# Replace stash@{0} with the reference to the stash you want to apply.

5. Alternatively, you can use git stash pop to apply the stash and remove it from the list of stashes:
   git stash pop stash@{0}

6. To remove a stash without applying the changes, run:
   git stash drop stash@{0}

7. To apply and remove all stashes, run:
   git stash clear

# These are the basic commands for using git stash. Remember that stashing is useful when you need to temporarily save changes

# and switch to another task, and then later come back and continue working on the original task.

# ===

# GIT rebase
export GITHUB_TOKEN=""

git checkout main && git pull upstream main && git push origin main
git checkout my_local_branch
git rebase -i main (or git rebase main)

# GH_RATE_REMAINING
GH_RATE_REMAINING=$(curl -s -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/rate_limit | jq ".rate.remaining")
echo $GH_RATE_REMAINING

# GIT log
git log --graph --oneline --decorate
git log --date=local --graph --decorate

### Best practices working with GIT
git clone https://naftalysh:GITHUB_TOKEN@github.com/naftalysh/reponame.git repo-directory-name
cd repo-directory-name
git remote add upstream https://naftalysh:GITHUB_TOKEN@github.com/upstream_orgname/reponame.git
If defined upstream without credentials, we can do it below:
git remote set-url upstream https://naftalysh:GITHUB_TOKEN@github.com/upstream_orgname/reponame.git


Ex:   git remote add upstream https://naftalysh:GITHUB_TOKEN@github.com/naftalysh-org/soc-simulation-project.git
      git remote set-url upstream https://naftalysh:GITHUB_TOKEN@github.com/naftalysh-org/soc-simulation-project.git
      git remote set-url origin https://naftalysh:GITHUB_TOKEN@github.com/naftalysh/soc-simulation-project.git

      git remote add upstream https://naftalysh:$GITHUB_TOKEN@coleam00/bolt.new-any-llm.git
      git remote set-url upstream https://naftalysh:$GITHUB_TOKEN@coleam00/bolt.new-any-llm.git
      git remote set-url origin https://naftalysh:$GITHUB_TOKEN@github.com/naftalysh/bolt.new-any-llm.git


# if main branch is called master then we use "master" else "main"
# Rebase
git checkout master && git pull upstream master && git push origin master

# When creating a new branch for a new task
1. Create the working branch
git checkout -b JIRA-number/jira-subject
2. Create same branch in origin
git push -u origin JIRA-number/jira-subject


3.Work in my local repo in VSCode (continuous ...)
   a. Update some file/s
   b. git add filename
   c. git commit -m "message"
   d. git push

4.After the 1st commit & push, we can create a PR in my GITHUB cloned repo with type/status as "draft"
    After all tests have passed, we can turn the PR to active PR


5.to create a signed commit
git commit -S
An editor opens in VSCode (if was setup)

The content should relate to some JIRA ticket nbe as follows:



6.If don't want to squash commits
git push

7.If want to squash commits
git rebase -i main
Choose the first commit and squash the rest
An editor window will open - update the commit message, close the editor
The commit will be written

8.force push
git push -f


fix|feat|test(JIRA-number): JIRA subject

short description
Signed-Off-By: Naftaly Shprai <naftalysh@gmail.com>



# More on GIT
# put files to be ignored by git into .gitignore
/home/username/repo-folder/.gitignore

# The steps to change a git branch name are:
1. Rename the Git branch locally
   git branch -m new-branch-name

2. Push the new branch to your GitHub or GitLab repo
   (Ex: git push -u origin new-branch-name)

3. Delete the branch with the old name from your remote repo
   (Ex: git push origin --delete nafta-updates)

# Delete Local Branch
To delete the local branch use one of the following:

$ git branch -d <branch_name>
$ git branch -D <branch_name>
The -d option is an alias for --delete, which only deletes the branch if it has already been fully merged in its upstream branch.
The -D option is an alias for --delete --force, which deletes the branch "irrespective of its merged status." [Source: man git-branch]
As of Git v2.3, git branch -d (delete) learned to honor the -f (force) flag.
You will receive an error if you try to delete the currently selected branch.

# Delete Remote Branch
As of Git v1.7.0, you can delete a remote branch using

$ git push <remote_name> --delete <branch_name>
(Ex: git push origin --delete nafta-updates)

# Undo a commit & redo
(<https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git>)

$ git commit -m "Something terribly misguided" # (0: Your Accident)
$ git reset HEAD~ # (1)
[ edit files as necessary ] # (2)
$ git add . # (3)
$ git commit -c ORIG_HEAD # (4)

#

# Reset your local master branch to the upstream version and push it to your origin repository
Assuming that "upstream" is the original repository and "origin" is your fork:

# ensures current branch is main
git checkout main

# pulls all new commits made to upstream/main

git pull upstream main

# this will delete all your local changes to main
git reset --hard upstream/main

# take care, this will delete all your changes on your forked main

git push origin main --force

# in one line - git checkout main && git pull upstream main && git reset --hard upstream/main && git push origin main --force

# Why is .gitignore not ignoring my files? (<https://stackoverflow.com/questions/45400361/why-is-gitignore-not-ignoring-my-files>)

If you already added those files and git is tracking them, the .gitignore file has no effect because it is meant for untracked files. See a good solution here: stackoverflow.com/a/23673910/2430526

"The .gitignore file ensures that files not tracked by Git remain untracked.
Just adding folders/files to a .gitignore file will not untrack them -- they will remain tracked by Git"

Answer1:
.gitignore only ignores files that are not part of the repository yet. If you already git added some files, their changes will still be tracked. To remove those files from your repository (but not from your file system) use git rm --cached on them.

Problem: I did this, but GitHub still wants to track and add them
Solution: git rm -r --cached <FolderName> to recursively remove the cache on a folder

Answer2:
The easiest, most thorough way to do this is to remove and cache all files in the repository, then add them all back. All folders/files listed in .gitignore file will not be tracked. From the top folder in the repository run the following commands:

git rm -r --cached .
git add .

#

# How can I see which Git branches are tracking which remote / upstream branch? (<https://stackoverflow.com/questions/171550/find-out-which-remote-branch-a-local-branch-is-tracking#comment18372080_171550>)

#

Get remote branches:
get remote -v

#which Git branches are tracking which remote / upstream branch?
From origin: git remote show origin
From upstream: git remote show upstream

# git-clone-branch-how-to-clone-a-specific-branch (<https://www.freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch/>)

# Updating a local repository with changes from a GitHub repository
git pull origin master or git pull origin main (depending on your local main branch)



# find the difference between two branches - localBranch and remoteRepo/remoteBranch
git remote add remoteRepo https://github.com/naftalysh/repo_name.git
git fetch remoteRepo
git diff localBranch remoteRepo/remoteBranch

# how programatically I can how many commit behind my branch is to the upstream main?
git fetch upstream main
git rev-list --count HEAD..upstream/main

1. Remove selenium-drivers from the Last Commit
## If you just committed but haven't pushed yet, use:
   git reset --soft HEAD~1
   % This undoes the last commit but keeps the changes staged. Now, remove the folder from staging:
   git reset -- Selenium/selenium-drivers/

   % Then, re-commit only the desired files:
   git commit -m "Updated commit without selenium-drivers"

   % Finally, push the commit:
   git push origin main

2. Remove selenium-drivers After Pushing (Force Push Required)
   If you've already pushed the commit to GitHub, you need to rewrite history:

   % Step 1: Remove the folder from Git
   git rm -r --cached Selenium/selenium-drivers/

   % Step 2: Add it to .gitignore to prevent tracking
   echo "Selenium/selenium-drivers/" >> .gitignore
   git add .gitignore

   % Step 3: Commit the changes
   git commit -m "Removed selenium-drivers from repo and added to .gitignore"

   % Step 4: Force push to overwrite history (if necessary)
   git push origin main --force

   **Force pushing (--force) rewrites history, so only do this if you’re sure! If working in a team, let others know before force-pushing.**

3. Verify That selenium-drivers is No Longer Tracked
   % Run:
   git ls-files | grep selenium-drivers
   or for windows CMD
   git ls-files | findstr selenium-drivers


   % If nothing is listed, the folder is no longer tracked.

Summary
✅ If not pushed, use git reset --soft HEAD~1
✅ If already pushed, use git rm -r --cached + force push
✅ Add .gitignore to prevent tracking in the future


# GITHUB

- Re-running workflows and jobs - GitHub Docs
  <https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs>

  that allows us to rerun CI tests on a repo

# How to list only the names of files that changed between two commits
git diff --name-only SHA1 SHA2
Ex: git diff --name-only SHA1 SHA2

# GIT - Why You Should Use git pull –ff-only
<!-- https://blog.sffc.xyz/post/185195398930/why-you-should-use-git-pull-ff-only -->

git config --global pull.ff only

# When to use 'git pull --rebase'
<!-- https://rednafi.github.io/reflections/when-to-use-git-pull-rebase.html -->
<!-- Whenever your local branch diverges from the remote branch, you can't directly pull from the remote branch and merge it into the local branch. -->

Solution - from the main branch, you can run:
git pull --rebase

This will rebase your local main by adding your local commits on top of the remote commits.

## in github how do I combine commits from a commit with specific sha onwards?
git rebase -i f031fd67647eb36a8a01be681ffca0df0e900dde^
Where f031fd67647eb36a8a01be681ffca0df0e900dde is the sha of the commit from which you want to rebase

## in github how do I combine 3 commits into one?
You can use the git rebase command in interactive mode (-i) to combine multiple commits into one. Please follow these steps:

Run git rebase -i HEAD~3. The HEAD~3 argument indicates the last three commits.

pick 1fc6c95 do something
pick 6b2481b do something else
pick dd1475d fix something

-->
pick 1fc6c95 do something
squash 6b2481b do something else
squash dd1475d fix something

-->
Save and close the file.

-->
An editor window will open for you to change the commit message. By default, it will be a list of all the commit messages of the commits that you're squashing.

-->
Save and close the file.

-->
Git will then combine the three latest commits into one.

Finally, you have to force push the last commit to the repository: git push origin +HEAD.

##


## install gh utility on wsl
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
sudo apt-add-repository https://cli.github.com/packages
sudo apt update
sudo apt install gh

#
# Searching for my PR in my e2e-tests repo
C:\Users\nafta>gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 3114-49C6
Press Enter to open https://github.com/login/device in your browser...
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as naftalysh


# List PRs authored by naftalysh
gh pr list --author naftalysh --repo konflux-ci/e2e-tests --state closed

# List PRs assigned to naftalysh
gh pr list --assignee naftalysh --repo konflux-ci/e2e-tests --state closed


gh pr list --author naftalysh --repo konflux-ci/e2e-tests --state closed

-->
#1075  feat(KONFLUX-2084): refactor-load-test-not-to-conflict-on-entity-names                      naftalysh:KONFLUX-2084/refactor-load-test-not-to-conflict-on-entity-names                  about 8 months ago
#1033  fix(KONFLUX-870): KONFLUX-870-Expose-accurate-resources-metrics                             naftalysh:KONFLUX-870/Expose-accurate-resources-metrics                                    about 10 months ago
#1032  fix(KONFLUX-1090): KONFLUX-1090-Update-offline-token-secrets-in-GitHub                      naftalysh:Fix-KONFLUX-1090/Update-offline-token-secrets-in-GitHub                          about 10 months ago
#990   fix(RHTAP-1897): Refactor-userJourneyThread-method                                          naftalysh:RHTAP-1897/Refactor-userJourneyThread-method-New-PR                              about 10 months ago
#970   fix(RHTAP-1897): Refactor-userJourneyThread-method                                          naftalysh:RHTAP-1897/Refactor-userJourneyThread-method                                     about 11 months ago
#947   fix(RHTAP-1991): Daily-CI-test-does-not-produce-JSON-file                                   naftalysh:RHTAP-1991/Daily-CI-test-does-not-produce-JSON-file                              about 11 months ago
#923   fix(RHTAP-1892): time-skew-between-the-testing-machine-and-the-cluster                      naftalysh:RHTAP-1892/Fix-time-skew-between-the-testing-machine-and-the-cluster             about 1 year ago
#913   feat(RHTAP-1926): Document-how-to-upload-offline-tokens-to-GitHub-sec…                      naftalysh:RHTAP-1926/Document-how-to-upload-offline-tokens-to-GitHub-secrets               about 1 year ago
#911   feat(RHTAP-1923): Update-offline-token-secrets-in-GitHub                                    naftalysh:RHTAP-1923/Update-offline-token-secrets-in-GitHub                                about 1 year ago
#905   fix(RHTAP-1913): Fix-high-error-rate-in-CI                                                  naftalysh:RHTAP-1913/Fix-high-error-rate-in-CI                                             about 1 year ago
#859   feat(RHTAP-1726): Fix-GitHub-action-against-Stage - Update monitoring configuration adj...  naftalysh:RHTAP-1726/Fix-GitHub-action-against-Stage-new                                   about 1 year ago
#848   feat(RHTAP-1726): Fix-GitHub-action-against-Stage                                           naftalysh:RHTAP-1726/Fix-GitHub-action-against-Stage                                       about 1 year ago
#839   feat(RHTAP-1532): Track-integration-test-scenario-resource-creation-time                    naftalysh:RHTAP-1532/Also-track-integration-test-scenario-resource-creation-time           about 1 year ago
#776   test(e2e-tests-pr): pr to tests e2e-tests repo                                              naftalysh:test                                                                             about 1 year ago
#718   feat(RHTAP-1338): Add-random-prefix-to-all-resource-names                                   naftalysh:RHTAP-1338/Add-random-prefix-to-all-resource-names                               about 1 year ago
#715   feat(RHTAP-1336): Collect-monitoring-data-from-the-OCP-Prometheus                           naftalysh:RHTAP-1336/Collect-monitoring-data-from-the-OCP-Prometheus                       about 1 year ago
#700   feat(RHTAP-1337): Properly cleanup in stage                                                 naftalysh:RHTAP-1337/properly-cleanup-in-stage                                             about 1 year ago
#661   feat(RHTAP-1018): load test measure how long the app test took                              naftalysh:RHTAP-1018/Load-test-measure-how-long-the-app-test-took                          about 1 year ago
#631   feat(RHTAP-878): load test should also measure app deployment time                          naftalysh:RHTAP-878/Load-test-should-also-measure-app-deployment-time                      about 1 year ago
#504   feat(RHTAP-868): use-different-component-repos                                              naftalysh:RHTAP-868/use-different-component-repos                                          about 1 year ago
#494   feat(RHTAP-869): collect-pod-logs                                                           naftalysh:RHTAP-869/collect-pod-logs                                                       about 1 year ago
#457   feat(RHTAP-623): load test to generate json file with all the results                       naftalysh:RHTAP-623/loadtest-to-generate-allresults-jsonfile                               about 1 year ago
#404   feat: Stone 831/collect pod logs                                                            naftalysh:STONE-831/collect-pod-logs                                                       about 1 year ago
#393   feat(STONE-768): integrate mvp-demo ginkgo test suit within godog                           naftalysh:STONE-768/Integrate-mvp-demo-ginkgo-testsuit                                     about 1 year ago
#259   test: Added timings support                                                                 naftalysh:HACBS-1142/test-specific-timeouts                                                about 1 year ago
#234   test: Hacbs 1142/test specific timeouts                                                     naftalysh:HACBS-1142/test-specific-timeouts                                                about 2 years ago
#203   test: HACBS-1132-Based-on-the-e2e-test-happy-path-Add-releasePlan-and-ReleasePlanAdmiss...  naftalysh:HACBS-1132/Based-on-the-e2e-test-happy-path-Add-releasePlan-and-ReleasePlanA...  about 2 years ago
#200   test: Hacbs 1130/create and delete namespaces in the new deployment of pre kcp              naftalysh:HACBS-1130/Create-and-Delete-namespaces-in-the-new-deployment-of-Pre-KCP         about 2 years ago
#199   test: Hacbs 1132/based on the e2e test happy path add release plan and release plan adm...  naftalysh:HACBS-1132/Based-on-the-e2e-test-happy-path-Add-releasePlan-and-ReleasePlanA...  about 2 years ago
#195   test: HACBS-1130/Create-and-Delete-namespaces-in-the-new-deployment-of-Pre-KCP              naftalysh:HACBS-1130/Create-and-Delete-namespaces-in-the-new-deployment-of-Pre-KCP         about 2 years ago


###

To have the same GitHub repository available in your **upstream organization** (in addition to your own fork and local copy), you can either **transfer** it or **duplicate** it to the organization, depending on what you want:

---

### **Option 1: Transfer Repository to Organization**
(You **move** the repository from your personal account to the organization)

#### When to use:
- You no longer need to own the repository under your personal account.
- You want to maintain stars, issues, forks, etc.

#### Steps:
1. On GitHub, go to **your forked repository**.
2. Click **Settings** > scroll down to **Danger Zone**.
3. Click **Transfer** and follow instructions.
   - You’ll be asked to type the organization name and confirm.
4. After the transfer:
   - The repo lives under the organization.
   - Update your local `origin` remote:
     ```bash
     git remote set-url origin https://github.com/<organization>/<repo>.git
     ```

---

### **Option 2: Duplicate Repository to Organization**
(You **copy** the repository to the organization as a separate repo)

#### When to use:
- You want to keep your personal fork **and** also maintain a version under the organization.

#### Steps:
1. On GitHub:
   - Go to the organization and click **New Repository**.
   - Name it the same or differently.
   - Create an empty repo (no README or license).

2. On your local machine:
   ```bash
   cd <your-local-repo>
   git remote add upstream-org https://github.com/<organization>/<repo>.git
   git push upstream-org main  # or master, or the branches you want
   ```

3. You can now keep it updated by pushing changes to both `origin` and `upstream-org` if needed:
   ```bash
   git push origin main
   git push upstream-org main
   ```

---

## ✅ Goal
Force main in naftalysh-org/github_actions_web_api
⬅️ to match the contents and history of update in naftalysh/github_actions_web_api


## ✅ Correct Workflow

### 1. Navigate to the target repo (organization repo directory)

You need to **clone** or **go into** the existing local clone of the organization repo:

```bash
cd C:\tmp
git clone https://github.com/naftalysh-org/github_actions_web_api.git
cd github_actions_web_api
```

Now you're inside the Git repository for `naftalysh-org/github_actions_web_api`.

---

### 2. Add your personal repo as a remote

```bash
git remote add personal https://github.com/naftalysh/github_actions_web_api.git
```

✅ This will now work because you're inside a valid `.git` repo.

---

### 3. Proceed with syncing `main` to `update` from your personal repo

```bash
git fetch personal update
git checkout main
git reset --hard personal/update
git push origin main --force
```

---

## 🛡 Optional: Backup main before force-pushing
If you want to keep a tag of the old main state:

```bash
git tag backup-main-$(date +%Y%m%d)
git push origin backup-main-$(date +%Y%m%d)
```


Absolutely! Below is the **final, robust, and updated procedure** for setting up a Git pre-commit mechanism with the `pre-commit` framework, including **safe installation of `detect-secrets` using `pipx`** to comply with modern Ubuntu and WSL environments (PEP 668 restrictions).

---

# ✅ Git Pre-commit Hook Setup with Secrets Detection (Ubuntu / WSL Friendly)

---

## 📌 What is `pre-commit`?

[`pre-commit`](https://pre-commit.com) is a framework to manage Git hooks like `pre-commit`, `pre-push`, etc.
It helps prevent issues **before they reach the repository**, such as secrets, broken formatting, or syntax errors.

---

## 🧠 Why Use `pre-commit` Over Manual Hooks?

| Feature                            | Manual `.git/hooks/pre-commit` | `pre-commit` Framework             |
|-----------------------------------|--------------------------------|------------------------------------|
| Portable & team-shareable         | ❌ No                          | ✅ Yes (versioned in the repo)     |
| Built-in secrets detection        | ❌ No                          | ✅ Yes (with `detect-secrets`)     |
| Multi-language support            | ❌ Shell-only                 | ✅ Python, JS, Shell, Docker, etc. |
| Autoformatting / Linting          | ❌ Must write scripts         | ✅ Plug & play                      |
| Modern OS compatibility (WSL)     | ❌ Manual only                | ✅ Yes, supports `pipx` or `venv`  |

---

## 🛠️ Full Setup Instructions

---

### 1️⃣ Install `pre-commit` Framework

```bash
sudo apt update
sudo apt install pre-commit
```

---

### 2️⃣ Navigate to Your Git Repository

```bash
cd path/to/your-git-repo
```

---

### 3️⃣ Create a `.pre-commit-config.yaml` File (Best Practices)

```yaml
repos:
  # 🔐 Secret detection with baseline
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: 'tests/.*'

  # ✅ General file checks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-json
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: debug-statements

  # 🐍 Python formatter
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        language_version: python3

  # 🧼 Python linter
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-bugbear]

  # 🐚 Shell linter
  - repo: https://github.com/koalaman/shellcheck-precommit
    rev: v0.9.0
    hooks:
      - id: shellcheck
        files: \.sh$

  # 📄 Markdown linter
  - repo: https://github.com/markdownlint/markdownlint
    rev: v0.12.0
    hooks:
      - id: markdownlint
        files: \.md$

  # 🐳 Dockerfile linter
  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint
        files: Dockerfile
```

Save this as `.pre-commit-config.yaml` in your repo root.

---

### 4️⃣ Install the Git Hook

```bash
pre-commit install
```

This creates `.git/hooks/pre-commit`, which runs:
```bash
#!/bin/sh
exec pre-commit run --hook-stage commit "$@"
```

---

### 5️⃣ (Optional) Test All Hooks Across the Repo

```bash
pre-commit run --all-files
```

---

### 6️⃣ Add a `.secrets.baseline` File for Secrets Scanning

#### a. ✅ Install `pipx` (safe package installer for CLI tools)
```bash
sudo apt install pipx
pipx ensurepath
```

Restart your shell if needed.

#### b. ✅ Install `detect-secrets` via `pipx` (safe, isolated):
```bash
pipx install detect-secrets
```

#### c. ✅ Create the baseline file:
```bash
detect-secrets scan > .secrets.baseline
```

#### d. (Optional) Audit and confirm:
```bash
detect-secrets audit .secrets.baseline
```

Use `a` to accept or `r` to reject suspected secrets.

#### e. ✅ Commit both config and baseline:
```bash
git add .pre-commit-config.yaml .secrets.baseline
git commit -m "Add pre-commit config and secrets baseline"
```

---

## 🔄 What Happens When You Commit

```bash
git commit -m "add new code"
```

The following checks are triggered automatically:
- 🔐 Secrets scanning (`detect-secrets`)
- ✅ JSON/YAML syntax validation
- 🐍 Code formatting with `black`
- 🧼 Linting with `flake8`, `shellcheck`
- 🐳 Dockerfile best-practices

If anything fails, the commit is **blocked**.

---

## 📋 Summary Checklist

| Task                                    | Command or File                                  | Done? |
|----------------------------------------|--------------------------------------------------|-------|
| Install `pre-commit`                   | `sudo apt install pre-commit`                    | ✅    |
| Create config file                     | `.pre-commit-config.yaml`                        | ✅    |
| Install Git hook                       | `pre-commit install`                             | ✅    |
| Run on all files (optional)            | `pre-commit run --all-files`                     | ✅    |
| Install `pipx`                         | `sudo apt install pipx && pipx ensurepath`       | ✅    |
| Install `detect-secrets` safely        | `pipx install detect-secrets`                    | ✅    |
| Create `.secrets.baseline`             | `detect-secrets scan > .secrets.baseline`        | ✅    |
| (Optional) Audit baseline              | `detect-secrets audit .secrets.baseline`         | ✅    |
| Commit config and baseline             | `git add` and `git commit`                       | ✅    |

---
# Resolving "Large File" Push Errors to GitHub with Git LFS on WSL

This document outlines the problem of encountering push errors to GitHub due to large files and provides a step-by-step solution using Git Large File Storage (LFS), including installation on WSL (Windows Subsystem for Linux) and rewriting history for existing large files.

## The Problem: GitHub File Size Limits

When attempting to push commits to a GitHub repository, you might encounter an error similar to this:

```
remote: error: File path/to/your/largefile.dat is 150.00 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
! [remote rejected] your-branch -> your-branch (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/your-username/your-repository.git'
```

This error occurs because GitHub imposes a strict limit on the size of individual files that can be directly stored in a Git repository (typically 100MB). Even if a large file was added in a past commit and subsequently "removed" or added to `.gitignore`, its presence in the Git history will still cause the push to be rejected if that history is being sent to the remote.

## The Solution: Git Large File Storage (LFS)

Git LFS is an extension that replaces large files in your Git repository with small text pointers. The actual large file content is stored on a separate LFS server (like the one provided by GitHub). This keeps your Git repository small and performant while still versioning your large assets.

### Step 1: Install Git LFS on WSL (Ubuntu/Debian Example)

If you're working within a WSL environment (e.g., Ubuntu), you need to install Git LFS there.

1.  **Open your WSL terminal.**

2.  **Add the PackageCloud repository for Git LFS:**
    This repository provides the latest versions of Git LFS.
    ```bash
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    ```

3.  **Install Git LFS:**
    Use `apt-get` to install the package.
    ```bash
    sudo apt-get install git-lfs
    ```

4.  **Verify the installation (optional but recommended):**
    ```bash
    git lfs --version
    ```
    You should see output like `git-lfs/x.y.z (GitHub; linux amd64; go a.b.c)`.

5.  **Initialize Git LFS for your user account (run once per user):**
    This command installs global Git LFS hooks.
    ```bash
    git lfs install
    ```
    Output: `Git LFS initialized.`

### Step 2: Navigate to Your Repository

Ensure you are in the root directory of your local Git repository within your WSL terminal.

```bash
cd /path/to/your/repository
# Example: cd /mnt/c/Users/YourUser/Projects/my-project
```

### Step 3: Initialize Git LFS for the Repository

Even if you ran `git lfs install` globally, you might need to initialize it for the specific repository if it wasn't done before or if you cloned a fresh copy. This ensures the local repository hooks are set up.

```bash
git lfs install
```
Output: `Git LFS initialized.` (It might also say it's already initialized, which is fine).

### Step 4: Track the Large File(s)

You need to tell Git LFS which files (or file patterns) it should manage.

*   **Identify the large file:** In our example error, it was `Selenium/selenium-drivers/linux/chrome-linux64/chrome`.
*   **Track the file:**
    ```bash
    git lfs track "Selenium/selenium-drivers/linux/chrome-linux64/chrome"
    ```
    You can also use patterns, e.g., `git lfs track "*.psd"` to track all Photoshop files.

    This command creates or updates a file named `.gitattributes` in your repository. This file tells Git how to handle files matching the specified patterns.

*   **Important Note on `.gitignore`:** If the large file was previously listed in your `.gitignore` file, you must remove or comment out that line. Git LFS can only track files that Git itself is aware of. If Git is ignoring the file, LFS won't manage it.

### Step 5: Stage the `.gitattributes` File

Add the `.gitattributes` file to your Git staging area.

```bash
git add .gitattributes
```
If you also modified `.gitignore` (to stop ignoring the large file), add it as well:
```bash
git add .gitignore .gitattributes
```

### Step 6: Migrate Existing Large Files in History

If the large file was already committed to your repository's history (which is why the push is failing), simply tracking it for future commits isn't enough. You need to rewrite your repository's history to convert the existing large file objects into LFS pointers.

**Caution:** Rewriting history changes commit SHAs. If you are collaborating with others, ensure they are aware and coordinate this process. Back up your repository before proceeding.

```bash
git lfs migrate import --everything --include="Selenium/selenium-drivers/linux/chrome-linux64/chrome"
```
*   `migrate import`: The command to rewrite history for LFS.
*   `--everything`: Instructs LFS to rewrite all local branches and tags. If you only want to rewrite the current branch and its ancestors, you might omit this or use more specific options, but `--everything` is common for a full cleanup.
*   `--include="path/to/your/largefile.ext"`: Specifies the exact file(s) to convert. You can use comma-separated paths or patterns if converting multiple files/types.

This process can take some time depending on the repository size and history depth.

### Step 7: Push the Rewritten History to the Remote

After the migration, your local history has been changed. To update the remote repository (e.g., GitHub), you will need to perform a "force push." It's generally safer to use `--force-with-lease` than a plain `--force` as it helps prevent accidentally overwriting work if the remote branch has new commits you haven't fetched.

```bash
git push --force-with-lease origin your-target-branch
```
*   Replace `your-target-branch` with the name of the branch you are trying to push (e.g., `main`, `develop`, `updates`).
*   Replace `origin` with your remote's name if it's different.

If `--force-with-lease` still gives issues (e.g., if the remote truly diverged in an unexpected way and you are certain your local version is correct), you might fall back to `git push --force origin your-target-branch`, but understand the risks.

### Step 8: Verification

After the push, check your GitHub repository.
*   The large file should now appear as an LFS pointer (a small text file) when you browse the repository.
*   The actual file content can be downloaded by clicking on it.
*   Your repository size (as reported by GitHub) should be smaller.

---

By following these steps, you can effectively manage large files in your Git repository using Git LFS and resolve push errors related to file size limits on platforms like GitHub.
