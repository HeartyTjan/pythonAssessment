
def display_phone_book_menu():
    print( """

        Phone Book
    .............................
                
        1 --> Search 
        2 --> Service Nos.
        3 --> Add name
        4 --> Erase
        5 --> Edit  
        6 --> Assign tone
        7 --> Send b'card
        8 --> Options
        9 --> Speed dials
        10 --> Voice tags
        11 --> Main Menu
    .............................
        """)

def display_options_menu() :
    print("""
    
        Options
    ...................................
        1 --> Type of view
        2 --> Memory status
        3 --> Back to previous menu
    ...................................
         """)

def display_message_menu() :
    print("""
        Messages
    .............................
                    
    1 --> Write messages
    2 --> inbox
    3 --> Outbox
    4 --> Picture messages
    5 --> Templates 
    6 --> Smileys
    7 --> Message settings
    8 --> Info service
    9 --> Voice mailbox number
    10 --> Service command editor
    0 --> Back to Main menu

                
    .............................
    """)
 
def display_message_setting() :
    print("""

		Message Settings
	...................................
		1 --> Set 1
		2 --> Common
		3 --> Back to previous Menu
	...................................
		""");
        
def display_set1_menu() :
    print("""

			Set 1
	..................................
		1 --> Message Centre number
		2 --> Messages sent as
		3 --> Message validity
		4 --> Back to previous Menu 
	...................................
		""")
def diplay_common_menu() :		
    print("""

		   	Common
	..................................
		 1 --> Delivery reports
		 2 --> Reply via same centre		
         3 --> Character support	
         4 --> Back to the previous Menu		
	..................................
	""" )


def display_call_register_menu() :
    print ( """

			Call register 
	............................
				 	
		1 --> Missed calls
		2 --> Received calls
		3 --> Dailed calls
		4 --> Erase recent call lists
		5 --> Show call durations	
		6 --> Show call costs
		7 --> Call cost settings
		8 --> Prepaid credit 
		0 --> Back to Main menu

............................
	""")
    
def display_show_call_cost_menu() :
    print("""

		Show call cost
...............................
	1 --> Last call cost	
	2 --> All call cost	
	3 --> Clear Counters
	4 --> Back to Previous Menu
..................................
	""")
    
def display_call_cost_setting_menu():
    print("""
									
				Call cost settings
			....................................
				1 --> Call cost limit	
				2 --> Show costs in
				3 --> Back to previous menu	
			....................................
			  """)
              
def display_tones_menu() :
    print("""

					  Tones
			.............................
				 	
				1 --> Ringing tone
				2 --> Ringing Volume
				3 --> Incoming call alert
				4 --> Composer
				5 --> Message alert tone	
				6 --> Keypad tones
				7 --> Warning and game tones
				8 --> Vibrating alert
				9 --> Screen saver
				0 --> Back to Main menu

			..............................
				  """)
                  
def display_setting_menu() :
    print("""

                Settings
............................................
				 	
		1 --> Call settings
		2 --> Phone settings
		3 --> Security settings
		4 --> Restore factory settings
		0 --> Back to Main menu

.............................................
    """)
def display_call_setting_menu():
    print("""
					
			Call Settings
	..................................
			1 --> Automatic redial
			2 --> Speed dialing
			3 --> Call waiting options
			4 --> Own number sending
			5 --> Phone line in use 
			6 --> Automatic answer
			7 --> Back to previous menu

	..................................
		  """)
def display_phone_setting_menu() :
    print("""

			 Phone Settings
..........................................
		1 --> Language
		2 --> Cell info display
		3 --> Welcome note
		4 --> Network selection
		5 --> Lights 
		6 --> Confirm sim service actions
		7 --> Back to previous menu
...........................................
		""")
def display_security_setting_menu() :
    print("""

		Security S ettings
..................................
	1 --> Pin code request
	2 --> Call barring service
	3 --> Fixed dialing
	4 --> Closed user group
	5 --> Phone security 
	6 --> Change access codes
	7 --> Back to previous menu

..................................
	  """)
      
def display_clock_menu() :
    print("""
					  
			Clock	
...........................................
		1 --> Alarm clock
		2 --> Clock settings
		3 --> Date setting
		4 --> Stopwatch
		5 --> Countdown timer
		6 --> Auto update of date and time
		0 --> For main menu
............................................
	""")


def display_main_menu():
    
    print("""

         Welcome to Nokia 3310

            MAIN Menu
    ---------------------------------------
                    
        1 --> Phone Book
        2 --> Message
        3 --> Chat
        4 --> Call Register
        5 --> Tones 
        6 --> Settings
        7 --> Call Divert
        8 -->  Games
        9 --> Calculator
        10 --> Reminders
        11 --> Clock
        12 --> Profiles
        13 --> Sim Services
        0 --> Quit
                
    -----------------------------------------
            """)

display_main_menu()
user_choice = int(input("Enter preferred option :  "))

match user_choice :
    case 1: 
        display_phone_book_menu()
        phone_book_menu = int(input("Enter preferred option :  "))
        match phone_book_menu :
            case 1: print("Search")
            case 2: print("Service Nos")
            case 3: print("Add name")
            case 4: print("Erase")
            case 5: print("Edit")
            case 6: print("Assign tone")
            case 7: print("Send b'card")
            case 8: 
                display_options_menu()
                option_menu = int(input("Enter preferred option :  "))
                match option_menu :
                    case 1: print("Type of view")
                    case 2: print("Memory Status")
                    case 3: display_phone_book_menu() 
                    case _:
                        print("Invalid")
                        display_options_menu()
       
            case 9: print("Speed dials")
            case 10 : print("Voice tags")
            case 11 : display_main_menu()
            case _: 
                print("Invalid option!!. Try again")
                display_phone_book_menu() 

    case 2:
        display_message_menu()
        message_menu = int(input("Enter preferred option :  "))
        match message_menu :
            case 1 : print("Write Message")
            case 2 : print("Inbox.")
            case 3 : print("Outbox")
            case 4 : print("Picture Message")
            case 5 : print("Template")
            case 6 : print("Smileys")
            case 7 : 
                    display_message_setting()
                    message_setting_menu = int(input("Enter preferred option :  "))
                    match message_setting_menu :
                        case 1 : 
                                display_set1_menu()
                                set1_menu = int(input("Enter preferred option :  ")) 
                                match set1_menu :
                                    case 1 : print("Message Centre number")     
                                    case 2 : print("Message Sent As")
                                    case 3 : print("Message Validity")
                                    case 4 : display_message_setting()
                                    case _ : 
                                            print("Invalid option!!. Try again")
                                            display_set1_menu()
                                
                        case 2 : 
                                diplay_common_menu()
                                common_menu = int(input("Enter preferred option :  ")) 
                                match common_menu :
                                    case 1 : print("Delivery reports")
                                    case 2 : print("Reply via same centre")
                                    case 3 : print("Character support")
                                    case 4 : displayMessageSetting()
                                    case _ : 
                                             print("Invalid option!!. Try again");
                                             diplay_common_menu() 

                        case 3 : display_message_menu()
                        case _ : 
                                print("Invalid option!!. Try again");
                                display_message_setting()
		
            
            case 8 : print("Info Service")
            case 9 : print("Voice Mailbox Number")
            case 10 : print("Service Command Editor")
            case 0 : displayMainMenu()
            case _ : 
                    print("Invalid option!!. Try again");
                    display_message_menu()
    
    case 3 : print ("Chat")
    case 4 : 
            display_call_register_menu()
            call_register_menu = int(input("Enter preferred option :  ")) 
            match  call_register_menu :
                case 1 : print("Missed Calls")
                case 2 : print("Received calls")
                case 3 : print("Dailed calls")
                case 4 : print("Erase recent call lists")
                case 5 : print("Show call durations")
                case 6 : 
                        display_show_call_cost_menu()
                        show_call_cost_menu = int(input("Enter preferred option :  ")) 
                        match showCallCostMenu :
                            
                            case 1 : print("Last Call Cost")
                            case 2 : print("All Call Cost")
                            case 3 : print("Clear Counter");
                            case 4 : display_call_register_menu()
                            case _ :   
                                    print("Invalid option!!. Try again")
                                    display_show_call_cost_menu()
                
                case 7 : 
                        display_call_cost_setting_menu()
                        call_cost_setting_menu = int(input("Enter preferred option :  ")) 
                        match call_cost_setting_menu :
                        
                            case 1 : print("Call Cost Limit")
                            case 2 : print("Show Cost in")
                            case 3 : display_call_register_menu()
                            case _ :   
                                    print("Invalid option!!. Try again")
                                    display_call_cost_setting_menu()

                case 8 : print("Prepaid credit")
                case 0 : display_main_menu()
                case _ :
                        print("Invalid option!!. Try again");
                        display_call_register_menu()
         
                
    case 5 : 
            display_tones_menu()
            tones_menu = int(input("Enter preferred option :  ")) 
            match tones_menu :
                case 1 : print("Ringing tone")
                case 2 : print("Ringing Volume")
                case 3 : print("Incoming call alert")
                case 4 : print("Composer")
                case 5 : print("Message alert tone")
                case 6 : print("Keypad tones")
                case 7 : print("Warning and game tones")
                case 8 : print("Vibrating alert")
                case 9 : print("Screen saver")
                case 0 : display_main_menu()
                case _ : 
                        print("Invalid option!!. Try again")
                        display_tones_menu()
                            
    case 6 :
            display_setting_menu()
            setting_menu = int(input("Enter preferred option :  "))
            match setting_menu :
                case 1 : 
                        display_call_setting_menu();
                        call_setting_menu = int(input("Enter preferred option :  "))
                        match call_setting_menu :
                            case 1 : print("Automatic redial")
                            case 2 : print("Speed dialing")
                            case 3 : print("Call waiting options")
                            case 4 : print("Own number sending")
                            case 5 : print("Phone line in use ")
                            case 6 : print("Automatic answer")
                            case 7 : display_setting_menu()
                            case _ : 
                                     print("Invalid option!!. Try again")
                                     display_call_setting_menu()

                            
                case 2 : 
                        display_phone_setting_menu()
                        phone_setting_menu = int(input("Enter preferred option :  "))
                        match phone_setting_menu :
                            case 1 : print("Language ")
                            case 2 : print("Cell info display")
                            case 3 : print("Welcome note")
                            case 4 : print("Network selection")
                            case 5 : print("Lights")
                            case 6 : print("Confirm sim service actions")
                            case 7 : display_setting_menu()
                            case _ :
                                     print("Invalid option!!. Try again")
                                     display_phone_setting_menu()

                        
                        
                        
                case 3 : 
                         display_security_setting_menu()
                         security_setting_menu = int(input("Enter preferred option :  "))
                         match security_setting_menu :
                            case 1 : print("Pin code request")						  
                            case 2 : print("Call barring service")
                            case 3 : print("Fixed dialing")
                            case 4 : print("Closed user group")  
                            case 5 : print("Phone security")
                            case 6 : print("Change access codes")
                            case 7 : display_setting_menu()
                            case _ :  
                                     print("Invalid option!!. Try again")
                                     display_security_setting_menu()
        
                case 4 : print("Restore factory settings")
                case 0 : display_main_menu()
                case _ :   
                         print("Invalid option!!. Try again")
                         display_setting_menu()

    case 7 : print("Call divert")
    case 8 : print("Games")
    case 9 : print("Calculator")
    case 10 : print("Reminder")
    case 11 :   
             display_clock_menu()
             clock_menu = int(input("Enter preferred option : "))
             match clock_menu :
                case 1 : print("Alarm clock")
                case 2 : print("Clock settings")
                case 3 : print("Date setting")
                case 4 : print("Stopwatch")
                case 5 : print("Countdown timer")	
                case 6 : print("Auto update of date and time")
                case 0 : display_main_menu()
                case _ :   
                         print("Invalid option!!. Try again")
                         display_clock_menu()
        
    case 12 : print("Profile")
    case 13 : print("Sim services")
    case _ :  
             print("Invalid option!!. Try again") 
             display_main_menu()

            

    
