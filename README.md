# Description
Simple Telegram bot to get posts from a custom subreddit.

# How to use
Just change the token and subreddit from `run.sh` to your telegram bot token and the desired subreddit, whithout the `/r/`.

# Leave running on Linux
  
- ssh into the remote machine  
- start tmux by typing tmux into the shell  
- start the process you want inside the started tmux session  
- leave/detach the tmux session by typing Ctrl+b and then d  
  
You can now safely log off from the remote machine, your process will keep running inside tmux. When you come back again and want to check the status of your process you can use tmux attach to attach to your tmux session.  
  
If you want to have multiple sessions running side-by-side, you should name each session using Ctrl+b and $. You can get a list of the currently running sessions using tmux list-sessions or simply tmux ls, now attach to a running session with command tmux attach-session -t.  
  
Feel free to ask me any questions or make any suggestions or pull requests.
