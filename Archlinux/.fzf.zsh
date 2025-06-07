# Setup fzf
# ---------
if [[ ! "$PATH" == */home/isaac/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/home/isaac/.fzf/bin"
fi

source <(fzf --zsh)
