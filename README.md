# GitHub Copilotを実践で使う
This is the repository for the LinkedIn Learning course GitHub Copilotを実践で使う. The full course is available from [LinkedIn Learning][lil-course-url].

![GitHub Copilotを実践で使う][lil-thumbnail-url] 

GitHub CopilotはAIによるプログラミング支援を受けることができるサービスです。「Copilot」は副操縦士という意味で、プログラマーのコーディングをさまざまな形でサポートしてくれます。このコースではGitHub Copilotの実践的な使い方について解説します。GitHub Copilotの導入方法から２つのライセンスの違い、対話形式でサポートを受ける方法や、ダミーデータを生成する方法など、GitHub Copilotの活用方法を紹介します。このコースを受講することでGitHub Copilotの支援について理解し、コーディングを効率よく行えるようになるでしょう。


## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

インストラクター

西村誠

プログラマー、Microsoft MVP


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/practical-github-copilot-23091337
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4D0DAQEuwrY928jGiA/learning-public-crop_675_1200/0/1711062897781?e=2147483647&v=beta&t=qHwJRHdLdfEmplr7ShA0qk_jH4qfRiWD-oB7T3p4Bnk

