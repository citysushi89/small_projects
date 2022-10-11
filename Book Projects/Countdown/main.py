# Show a countdown timer animation using a seven-segment display

import sys, time
import sevseg

# User selects number using whole number inputs
while True:
    seconds_left = input("How many seconds would you like to countdown from? ")
    try:
       seconds_left = int(seconds_left)
       break
    except ValueError:
        print("Please input a whole number using digits") 


try:
    while True:
        #Clear screen by printing several new lines
        print('\n' * 60)

        # Getting hours and minutes from seconds left
        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600) // 60)
        seconds = str(seconds_left % 60)

        # Get the digit strings from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Displaying the digits
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if seconds_left == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print("Press Ctrl-C to quit.")

        time.sleep(1)
        seconds_left -= 1
except KeyboardInterrupt:
    print("You stopped the countdown!")
    sys.exit()
