def verse_menu_options() :

	match user_option : 

	    case 1 : 
                print("""
                        
                        On the first day of Christmas, my true love gave to me
                        A Partridge in a Pear Tree

                        """)  


	    case 2 : 
                print("""
                        
                On the second day of Christmas, my true love gave to me
                Two turtle doves,
                And a partridge in a pear tree

                """)
                        
	    case 3 :
                    print("""
                
                        On the third day of Christmas, my true love gave to me...
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)
	    case 4 :
                    print("""
                
                        On the fourth day of Christmas, my true love gave to me...
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.
                    
                        """)

	    case 5 : 
                    print("""
                
                        On the fifth day of Christmas, my true love gave to me...
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)
	    case 6:	
                    print("""
                
                        On the sixth day of Christmas, my true love gave to me...
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)	
                
	    case 7 : 
                    print("""
                
                        On the seventh day of Christmas, my true love gave to me...
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)

	    case 8 : 
                    print("""
                
                        On the eighth day of Christmas, my true love gave to me...
                        Eight maids a-milking,
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)

	    case 9 :    
                    print("""
                
                        On the ninth day of Christmas, my true love gave to me...
                        Nine ladies dancing,
                        Eight maids a-milking,
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree

                        """)

	    case 10 : 
                    print("""
                
                        On the tenth day of Christmas, my true love gave to me...
                        Ten lords a-leaping,
                        Nine ladies dancing,
                        Eight maids a-milking,
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree...

                        """)

	    case 11 : 
                    print("""
                
                        On the eleventh day of Christmas, my true love gave to me...
                        Eleven pipers piping,
                        Ten lords a-leaping,
                        Nine ladies dancing,
                        Eight maids a-milking,
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)
                
	    case 12 : 
                    print("""
            
                        On the twelfth day of Christmas, my true love gave to me...
                        Twelve drummers drumming,
                        Eleven pipers piping,
                        Ten lords a-leaping,
                        Nine ladies dancing,
                        Eight maids a-milking,
                        Seven swans a-swimming,
                        Six geese a-laying,
                        Five golden rings,
                        Four calling birds,
                        Three French hens,
                        Two turtle doves,
                        And a partridge in a pear tree.

                        """)
    
	    case _ : print("Thank you")
	
		


def display_song_verse_menu() :

	print ("""
			
				12 Days of Christmas
			=====================================
			 1 --> A patridge in a pear tree
			 2 --> Two Turtle Doves
			 3 --> Three French Hens
			 4 --> Four Calling Birds
			 5 --> Five Golden Rings
			 6 -->  Six Gesse a-Laying
			 7 --> Seven Swans a-Swimming
			 8 --> Eight Maids a-Milking
			 9 --> Nine Ladies Dancing
			 10 --> Ten Lords a-Leaping
			 11 --> 11. Eleven Pipers Piping
			 12 --> Twelve Drummers Drumming
			 0 --> Quit
			=====================================
	 """)	

display_song_verse_menu()


user_option = 1

while user_option != 0 :

	user_option = int(input("Enter prefered option :"))

	verse_menu_options()




	