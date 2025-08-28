#!/usr/bin/env python

from buildbot.plugins import changes

sources = []
sources.append(
    changes.GitHubPullrequestPoller(
        owner="gentoo",
        branches=None,
        category="gentoo-pull",
        repo="gentoo",
    )
)

sources.append(
    changes.GitPoller(
        repourl="https://github.com/gentoo/gentoo.git",
        branches=True,
        category="gentoo-pull",
        workdir="gentoo-repository",
        pollInterval=300,
    )
)

sources.append(
    changes.GitPoller(
        repourl="https://anongit.gentoo.org/git/proj/linux-patches.git",
        only_tags=True,
        category="gentoo-tags-git",
        workdir="linux-patches-tags",
        pollInterval=300,
    )
)

sources.append(
    changes.GitPoller(
        repourl="https://anongit.gentoo.org/git/proj/linux-patches.git",
        branches=True,
        category="gentoo-git",
        workdir="linux-patches-branches",
        pollInterval=300,
    )
)

sources.append(
    changes.GitPoller(
        repourl="https://github.com/jessesimpson36/linux-patches.git",
        branches=True,
        category="gentoo-git",
        workdir="linux-patches-branches2",
        pollInterval=300,
    )
)
