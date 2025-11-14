# Shell Completion Scripts

This directory contains shell completion scripts for the Todo List Manager. Completion scripts provide tab-completion for commands and arguments in your shell.

## Bash Completion

### Installation

#### System-wide (requires sudo)

```bash
sudo cp completions/todo.bash /etc/bash_completion.d/todo
```

#### User-level

Add to your `~/.bashrc`:

```bash
source /path/to/url-shortener/completions/todo.bash
```

Then reload your shell:

```bash
source ~/.bashrc
```

### Usage

After installation, you can use tab-completion:

```bash
todo <TAB>                    # Shows available commands
todo config <TAB>             # Shows config keys
todo config use_colors <TAB>  # Shows true/false options
```

## Zsh Completion

### Installation

#### Using fpath

1. Copy the completion file to a directory in your `$fpath`:

```bash
mkdir -p ~/.zsh/completion
cp completions/todo.zsh ~/.zsh/completion/_todo
```

2. Add to your `~/.zshrc` (if not already present):

```bash
fpath=(~/.zsh/completion $fpath)
autoload -U compinit && compinit
```

3. Reload your shell:

```bash
source ~/.zshrc
```

#### Direct sourcing

Add to your `~/.zshrc`:

```bash
source /path/to/url-shortener/completions/todo.zsh
```

### Usage

After installation, you can use tab-completion:

```bash
todo <TAB>                    # Shows available commands with descriptions
todo config <TAB>             # Shows config keys with descriptions
todo config use_colors <TAB>  # Shows true/false options
```

## Fish Completion

Fish completion support coming soon!

## Testing Completion

### Bash

After installing, test with:

```bash
todo <TAB><TAB>
```

You should see a list of available commands.

### Zsh

After installing, test with:

```bash
todo <TAB>
```

You should see a list of available commands with descriptions.

## Troubleshooting

### Bash

If completion doesn't work:

1. Check if bash-completion is installed:
   ```bash
   apt-get install bash-completion  # Debian/Ubuntu
   brew install bash-completion     # macOS
   ```

2. Verify the completion is loaded:
   ```bash
   complete -p todo
   ```

### Zsh

If completion doesn't work:

1. Check your fpath:
   ```bash
   echo $fpath
   ```

2. Verify completion is initialized:
   ```bash
   autoload -U compinit && compinit
   ```

3. Rebuild completion cache:
   ```bash
   rm -f ~/.zcompdump
   compinit
   ```

## Creating an Alias

If you create an alias for the todo script:

```bash
alias todo='python /path/to/todo.py'
```

The completion scripts will still work!

## Contributing

If you'd like to add completion support for other shells (Fish, PowerShell, etc.), please submit a pull request!
