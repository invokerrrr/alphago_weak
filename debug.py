#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Invoker Bot
@Email   : invoker-bot@outlook.com
@Site    : 
@Data    : 2022/6/27
@Version : 1.0
"""

from alphago_weak.dataset.u_go import UGoArchive

if __name__ == '__main__':
    archive = UGoArchive()
    archive.download()
