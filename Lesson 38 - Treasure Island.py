print('''

                 / \ '          ,|
                    `\`\      //|                             ,|
                      \ `\  //,/'                           -~ |
   )             _-~~~\  |/ / |'|                       _-~  / ,
  ((            /' )   | \ / /'/                    _-~   _/_-~|
 (((            ;  /`  ' )/ /''                 _ -~     _-~ ,/'
 ) ))           `~~\   `\/'/|'           __--~~__--\ _-~  _/,
((( ))            / ~~    \ /~      __--~~  --~~  __/~  _-~ /
 ((\~\           |    )   | '      /        __--~~  \-~~ _-~
    `\(\    __--(   _/    |'\     /     --~~   __--~' _-~ ~|
     (  ((~~   __-~        \~\   /     ___---~~  ~~\~~__--~
      ~~\~~~~~~   `\-~      \~\ /           __--~~~'~~/
                   ;\ __.-~  ~-/      ~~~~~__\__---~~ _..--._
                   ;;;;;;;;'  /      ---~~~/_.-----.-~  _.._ ~
                  ;;;;;;;'   /      ----~~/         `\,~    `\ 
                  ;;;;'     (      ---~~/         `:::|       `.
                  |'  _      `----~~~~'      /      `:|        ()))),
            ______/\/~    |                 /        /         (((((())
          /~;;.____/;;'  /          ___.---(   `;;;/             )))'`))
         / //  _;______;'------~~~~~    |;;/\    /                ((   (
        //  \ \                        /  |  \;;,\                 `
       (<_    \ \                    /',/-----'  _>
        \_|     \\_                 //~;~~~~~~~~~
                 \_|               (,~~   -Tua Xiong
                                    \~\
                                     
''')
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Treasure Island Game               *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Treasure Island Game!")
print("Your mission is to find treasure!\n")
print("(Enter Y/N or L/R to navigate your way through the game!)\n")

print(r"""\
     ___  ,--.  __________________________/   ,   /_______
    'O---O'~
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _
         _____                       ~'O---O'
 _______< Rome|_____        __________________________
           ||      /   ,   /
""")

user_direction = input("You have arrived at a crossroads. The direction sign is broken"
                       " So...do you wish to go left or right?")

if user_direction == 'RIGHT' or user_direction == 'right' or user_direction == 'r':
    print("\n Oh no! You were torn apart by the very cross Hen of DEATH!!!!! --> GAME OVER!")
    print((('''       ,~.
   ,-'__ `-,
  {,-'  `. }              ,')
 ,( a )   `-.__         ,',')~,
<=.) (         `-.__,==' ' ' '}
  (   )                      /
   `-'\   ,                  )
       |  \        `~.      /
       \   `._        \    /
        \     `._____,'   /
         `-.            ,'
            `-.      ,-'
               `~~~~'
               //_||
            __//--'/`   hjw
          ,--'/`  '
             '
    ''')))

elif user_direction == 'LEFT' or user_direction == 'left' or user_direction == 'l':
    print("After a walk along a tree shaded winding path, you arrive at a "
          "placid lake.\n The lake water laps gently at the shore edge. \n"
          "It is beginning to get dark, do you jump in and swim across"
          ", or decide to wait until dawn?\n")
    print(r"""\
                ___
          /`  _\
          |  / 0|--.
     -   / \_|0`/ /.`'._/)
 - ~ -^_| /-_~ ^- ~_` - -~ _
 -  ~  -| |   - ~ -  ~  -
jgs     \ \, ~   -   ~
         \_|
    """)



user_choice = input("Press s or type yes to swim across, type n or no to stay put."
                    " So...do you wish to go for a swim or risk the darkening forest?...")
if user_choice == 'YES' or user_choice == 'yes' or user_choice == 'y':
    print("\n Oh no! You were torn apart by the very cross goldfish of DEATH!!!!! --> GAME OVER!")
    print((('''       /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
    ''')))

elif 'NO' == user_choice or user_choice == 'no' or user_choice == 'n':
    print("\n Whew, good decision. The goldfish of DEATH would have got you, instead,the next morning"
          " was bright and sunny with fluffy clouds as you "
              "safely make your way along the lakes edge."
              "\nEventually you come across a little cottage deep in the woods. "
          "The fluffy clouds appear to have changed colour to a grim dark gray... \n"
          "The little cottage has three doors,\n one coloured red, one coloured blue and one coloured yellow.\n")
    print(r"""\ 
                                       //\\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
    
    """)

user_choice = input("Your going to have to pick one, whats it going to be...(R)ed (B)lue or (Y)eller...?")
if user_choice == 'BLUE' or user_choice == 'blue' or user_choice == 'b' or user_choice == 'B'or user_choice == 'RED' or user_choice == 'red' or user_choice == 'r' or user_choice =='R':
    print("\n Oh no! You were torn apart by the very cross Dragon of DEATH!!!!! --> GAME OVER!")
    print(r"""\
              ^\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\
  )\-._    ||         ;"._      "=.     )\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\
            (_/(_/(_/                  '., \ \\ \`.'    LGB
                                           `." `.'
    """)

elif user_choice == 'Yeller' or user_choice == 'Yellow' or user_choice == 'y' or user_choice == 'Y':
    print("WELL DONE!, You have found the treasure...an old copy of Sonic the Hedgehog dvd, yay.")
    print(r"""\
                               ______                         
                     _.-*'"      "`*-._                   
                _.-*'                  `*-._              
             .-'                            `-.           
  /`-.    .-'                  _.              `-.        
 :    `..'                  .-'_ .                `.      
 |    .'                 .-'_.' \ .                 \     
 |   /                 .' .*     ;               .-'"     
 :   L                    `.     | ;          .-'         
  \.' `*.          .-*"*-.  `.   ; |        .'            
  /      \        '       `.  `-'  ;      .'              
 : .'"`.  .       .-*'`*-.  \     .      (_               
 |              .'        \  .             `*-.           
 |.     .      /           ;                   `-.        
 :    db      '       d$b  |                      `-.     
 .   :PT;.   '       :P"T; :                         `.   
 :   :bd;   '        :b_d; :                           \  
 |   :$$; `'         :$$$; |                            \ 
 |    TP              T$P  '                             ;
 :                        /.-*'"`.                       |
.sdP^T$bs.               /'       \                       
$$$._.$$$$b.--._      _.'   .--.   ;                      
`*$$$$$$P*'     `*--*'     '  / \  :                      
   \                        .'   ; ;   [bug]              
    `.                  _.-'    ' /                       
      `*-.                      .'                        
          `*-._            _.-*'                          
               `*=--..--=*'
    """)






