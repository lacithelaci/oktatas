  285  mkdir gyakorlas
  286  cd gyakorlas
  287  mkdir www
  288  cd www
  289  mkdir htdocs include
  290  cd htdocs
  291  touch index.php
  295  cd
  297  cd gyakorlas
  298  cd www
  299  cd include
  300  touch main.inc
  301  cd
  302  cd gyakorlas
  303  mkdir log
  304  cd log
  305  touch error.log
  306  clear
  307  cd gyakorlas
  308  cd
  309  cd gyakorlas
  310  tree
  311  sudo chmod 751 log
  312  cd log
  313  sudo chmod 64 error.log
  314  cd
  315  cd gyakorlas
  316  sudo chmod 777 www
  317  cd www
  318  sudo chmod 575 htdocs
  319  cd htdocs
  320  sudo 644 index.php
  321  sudo chmod 644 index.php
  322  cd
  323  cd gyakorlas
  324  cd www
  325  sudo chmod 755 include
  326  cd include
  327  sudo chmod 755 main.inc
  328  cd
  329  cd gyakorlas
  331  sudo chown user:users log
  333  sudo chown user:users www
  334  cd log
  335  sudo chown user:students error.log
  336  sudo groupadd students
  337  sudo groupadd losers
  338  sudo chown user:students error.log
  339  cd
  340  cd gyakorlas
  341  cd www
  342  sudo chown loser:losers htdocs
  343  sudo chown user:users include
  344  cd htdocs
  345  sudo chown loser:students index.php
  346  cd
  347  cd gyakorlas
  348  cd www
  349  cd include
  350  sudo chown user:students main.inc
  351  cd
  352  cd gyakorlas
  355  cd log
  358  cd
  359  cd gyakorlas
  360  cd www
  363  history > gyakorlas.bat
