# below is a loop that limits the number of attempts to 3
# In below example, attempts remaining only shown when a wrong pin has been typed

import sys
import getpass

supplied_pin = None
correct_pin = "1234"
attempts_allowed = 3
attempts = 0

while supplied_pin != correct_pin:
        while attempts < attempts_allowed:
                supplied_pin = input("Enter your PIN:")
                # supplied_pin = getpass.getpass (prompt = "Enter your PIN:", stream=None)
                # getpass method & module should mean the password typed in the terminal is not shown, however this isn't working for my laptop
                # might be a mac issue
                # instead it warns in red text in the terminal that password input may be echoed
                if supplied_pin != correct_pin:
                        print("Incorrect pin")
                        attempts = attempts + 1
                        print("Attempts remaining:", str(attempts_allowed - attempts))
                else:
                # else condition will be met when the pin is correct - when supplied_pin == correct_pin, and the loop breaks
                        break
        else:
                # this else is with the while attempts < attempts_allowed condition
                # when there has been 3 attempts, the user will be told they have exceeded the number of attempts and the loop is broken
                # sys.exit('Number of attempts exceeded')
                print('Number of attempts exceeded')
                break

else:
        # this else is with the initial while condition, so when supplied_pin == correct_pin the below is printed
        print("Correct pin")
