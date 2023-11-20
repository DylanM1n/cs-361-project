The way that you use this microservice in order to request data is by typing or writing to the microservice.txt file "true"
after you do this you the microservice will generate 2 numbers for you to read from and that is the requesting and recieveing done.


tictactoe game                          service.txt               microservice
      |                                     |                           |
      ||           getCord()  (sends true)  |                           |
      ||--------------------------------->  ||                          |
      ||                                    ||                          |
      ||<-----------------------------------||      generates numbers   |
      ||            status                  || ------------------------>||  
      ||                                    ||                          ||
      ||                                    ||<-------------------------||
      ||               send cords           ||         sendback cords   ||
      ||<-----------------------------------||                          ||
      ||                                    ||                          ||
      ||                                    ||                          ||
      ||              closeRequest          ||                          ||
      ||----------------------------------> ||        close             ||
      |                                     ||------------------------->||
      |                                     |                           |                       
