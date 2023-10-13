#!/usr/bin/env bash
function lazygit() {
    git commit -m "$1"
    git push
}
