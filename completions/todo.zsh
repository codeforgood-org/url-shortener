#compdef todo.py todo

# Zsh completion script for todo.py
# Installation:
#   Copy this file to a directory in your $fpath, typically:
#   cp completions/todo.zsh ~/.zsh/completion/_todo
#   Or add to your ~/.zshrc:
#   fpath=(~/path/to/completions $fpath)
#   autoload -U compinit && compinit

_todo() {
    local -a commands
    commands=(
        'add:Add a new task'
        'list:List all tasks'
        'remove:Remove a task by number'
        'clear:Remove all tasks'
        'config:View or set configuration'
        'help:Show help message'
    )

    local -a config_keys
    config_keys=(
        'tasks_file:Path to tasks JSON file'
        'use_colors:Enable/disable colored output'
        'show_task_ids:Show task IDs'
        'date_format:Date format string'
    )

    _arguments -C \
        '1: :->command' \
        '*: :->args'

    case $state in
        command)
            _describe 'command' commands
            ;;
        args)
            case $words[2] in
                config)
                    if (( CURRENT == 3 )); then
                        _describe 'config key' config_keys
                    elif (( CURRENT == 4 )); then
                        case $words[3] in
                            use_colors|show_task_ids)
                                _values 'value' 'true' 'false'
                                ;;
                        esac
                    fi
                    ;;
                remove)
                    _message 'task number'
                    ;;
                add)
                    _message 'task description'
                    ;;
            esac
            ;;
    esac
}

_todo "$@"
