#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

#PS1='[\u@\h \W]\$ '
#PS1="[\[\e[31m\]\u\[\e[m\]@\[\e[36m\]\h\[\e[m\]: \[\e[34m\]\W] \[\e[37m\]> "
PS1="\[\e[01;36m\][\[\e[01;36m\]\A \u\[\e[01;37m\] \W\[\e[01;36m\]]\$\[\e[00m\] "

screenfetch

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
