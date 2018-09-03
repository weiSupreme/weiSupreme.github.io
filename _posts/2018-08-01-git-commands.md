---
layout: post
title: 常用的git命令
categories: InformalEssay
tags: Github
author: zhuwei
description: 整理的一些常用的git的命令
---

                            
&emsp;&emsp;一些常用的git 命令集合：               

            git add filename
            git add . (add all file)

            git commit -m "discribtions"

            git push origin master (-f: force to push)
            git push origin branchNeme:branchName

            git checkout -b newBranchName
            git checkout brachName
            git branch -a (list all branch)
            
            git tag v1.0
            git tag -a v1.0 -m "describe"
            git show v1.0
            git push origin v1.0
            git tag -d v1.0
            git push origin :refs/tags/v1.0				

            git status

            git log

            git diff

            git reset --hard HEAD^ (back to last version)

            git branch -D branchName (delete local branch)
            git push origin --delete branchName (delete remote branch)

            git checkout -- filename (delete changes if don't add)
            git reset HEAD filename (delete changes after adding)
