#!/usr/bin/env bash
# Bash completion script for todo.py
# Installation:
#   Copy this file to /etc/bash_completion.d/ or source it in your ~/.bashrc:
#   source /path/to/completions/todo.bash

_todo_completions()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Available commands
    opts="add list remove clear config help"

    # Complete commands
    if [ $COMP_CWORD -eq 1 ]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi

    # Complete config keys
    if [ "${prev}" == "config" ]; then
        config_keys="tasks_file use_colors show_task_ids date_format"
        COMPREPLY=( $(compgen -W "${config_keys}" -- ${cur}) )
        return 0
    fi

    # Complete config values for use_colors
    if [ "${COMP_WORDS[COMP_CWORD-2]}" == "config" ] && [ "${prev}" == "use_colors" ]; then
        COMPREPLY=( $(compgen -W "true false" -- ${cur}) )
        return 0
    fi

    # Complete config values for show_task_ids
    if [ "${COMP_WORDS[COMP_CWORD-2]}" == "config" ] && [ "${prev}" == "show_task_ids" ]; then
        COMPREPLY=( $(compgen -W "true false" -- ${cur}) )
        return 0
    fi

    return 0
}

# Register the completion function
complete -F _todo_completions todo.py
complete -F _todo_completions todo

# If todo.py is aliased, complete that too
if alias todo &>/dev/null; then
    complete -F _todo_completions todo
fi
