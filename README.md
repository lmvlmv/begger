Beggar my Neighbour fiddling


# Notes


## Game number handling
* Game number spec

52 bit number, 13 bits represent court card positions. Iterator
court card permutes from 4J 4Q 4K. Iterator. permutations fixed list? saves generator code

TODO: Court card positions could be represented by bits. J=01, Q=10, K=11, 24 bits with leading zero = court spec for individual game. 

validate game number: check for 13 bits, check for court spec

max game number = 4502500115742720 (52nd bit set)

Game number = long int
Specific game = long int:hexhexhex


`fff0000000000:55aaff`

Game number -> ASCII spec (26/26 JQK and -)

`JJJJQQQQKKKK--------------/--------------------------`

ASCII spec -> game number

* Generate next game number
* generate range of game numbers
* generate range of count games and return game numbers

## Game player

* Play game given specific game
  * Return stats 
* Play all court permutes for game number
  * Return stats
* Detect looped games

## Data handler

* Game stats
  * Number of turns
  * Number of tricks
  * Nubmer of start positions visited

* Track game number ranges played
  * Generate new ranes to play
  * Generate interesting ragnes to play
* Track n longest games
  * Store by specific game number
  * Track most moves
  * Track most tricks
  * Track most start positions visited

## Queue handler

* Celery and rabbitmw
* Game playing workers for game numbers
* Game playing workers for specific games
* Results object returning. Messages for data handler?

## Error handling

* lost games?
* Bad resutls?

## Machine learning

Train reinforcement lerning to try to find long games. 
train based on start position. goal is maximize turns.


