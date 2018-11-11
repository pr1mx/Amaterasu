#coding: utf-8
#!/usr/bin/python3

from huepy import *
import os
import random

bannerA = '''
	   /-                                          -/  
	  /m/                                        /m/  
	  -NNs`                                    `sNN:  
	  .NNmh.                /+:               .hmNN.  
	  `mN-/d:              `yyo              :d/.Nm`  
	   dm` `o+             `yy+             +o` `md   
	   hd `: .+`           `yy/           `+. :` dh   
	   sh  -y. -`          `yy:          `. .y-  yy   
	  .os ` -do`           `yy-           `od-   so.  
	  yy+ `y--sy:          `yy.          :ys-   `+yh  
	/`y+:  ..              :yy-                +s:+y./
	:/o                 `:ss::oo-              .`  o/:
	                   /ss:    -os:                   
	 `-..`             /y/      +y+                   
	  `:syysoo+//:-.`   +y:    +y+     ``.-::/++o+:`  
	     syyhddhhhyys-   oy:  +y+  `/syyyyyyyyys.     
	    `syyyyohNNmdyy/` `oy-+y+  .syhmNNNddyyys      
	    `yyyys:`./+oyyys. `syy+  /yhmmhyo.`oyyyy`     
	     `-:+oss+.     `-` -ys `::-.`   .+syso+:`     
	           `-::.`      .y+       `:++:-`          
	                       `y/      ``                
	                        s:                        
	              `-        o.        .               
	               +-       +`       -.               
	               `h.      /       .o                
	                /h`     -      `h.                
	                 hy            ss                 
	                 :Ns          +m.                 
	                  yNy-:yyys:`/mo                  
	                   -omh//++hds/`                  
	                      :sdy+.
'''

banner1 = '''
                              __
                            .d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
'''

banner2 = '''
                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba
                         Y8o                   Y8'         88
                          `Y8               ,8"           `P
                            Y8o        ,d8P'              ba
                       ooood8888888P"""'                  P'
                    ,od                                  8
                 ,dP     o88o                           o'
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$
'''

banner3 = '''
 ▄▄▄       ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████  ██▀███   ▄▄▄        ██████  █    ██ 
▒████▄    ▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒████▄    ▒██    ▒  ██  ▓██▒
▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▓██  ▒██░
░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒▓▓█  ░██░
 ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒▒▒█████▓ 
 ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ 
  ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░░░▒░ ░ ░ 
  ░   ▒   ░      ░     ░   ▒    ░         ░     ░░   ░   ░   ▒   ░  ░  ░   ░░░ ░ ░ 
      ░  ░       ░         ░  ░           ░  ░   ░           ░  ░      ░     ░     
                                                                                   
'''

def show_banners(versao):
	banners = [bannerA, banner1, banner2, banner3]
	print(random.choice(banners))