# Hackathon April 2021
# Team: Free Agent Rejects
# Project: The Most Amazing Financial Advisor Ever
#
# Margaret's contribution

stuff_list = []


# Logo to start off the program.
def large_logo():
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$                $$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$$     $$$   $$$$$$ $$$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$$    $$$$   $$$$$$$$$$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$$    $$$$   $$$$$$$$$$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$           $$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$     $$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$    $$$$$   $$$     $$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$                  $$$$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$     $$$$$$$$$$            $$$$$$$$$$$$$     $$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")


large_logo()

# Logo followed by welcome with header.
print("\nWelcome to...")


def header_fin_ad():
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    \nT H E  M O S T  A M A Z I N G  F I N A N C I A L  A D V I S O R  E V E R\n
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\n$$$$$$$$$$$$$$$$$$$$$$$$ Free Financial Advice! $$$$$$$$$$$$$$$$$$$$$$$$\n""")


header_fin_ad()


# Header followed by introduction.
def intro_fin_ad():
    print("""THE MOST AMAZING FINANCIAL ADVISOR EVER uses the magical power of AI to
offer you the most amazing financial advice you're ever likely to
experience.*"
\nSimply enter your financial data with our helpful questionnaire and let
THE MOST AMAZING FINANCIAL ADVISOR lead you through various investment
options.
\nTHE MOST AMAZING FINANCIAL ADVISOR will then print out a Personalized
Portfolio Just For You. Soon you'll be on your way to an amazing financial
future.""")


intro_fin_ad()


# Introduction followed by important disclaimer.
def disclaimer():
    print("""\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n
* Please note THE MOST AMAZING FINANCIAL ADVISOR EVER is for
'entertainment' purposes only, and accepts no liability for the financial
ruin that may result.
\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n""")


disclaimer()


# Step 1: Get a starting number, starting_dollars, from user-inputted questionnaire
print("""STEP I: YOUR FINANCIAL INFORMATION
Gather up all the information regarding your assets, and THE MOST AMAZING
FINANCIAL ADVISOR will lead you through a questionnaire and calculate how
much you are currently worth. When you enter numbers, omit any commas.\n""")

print("""How much do you have in your checking and savings account? If you have more
than one, be sure to include them all.""")
checking_savings_raw = input("$ ")
if not checking_savings_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    checking_savings_raw = input("$ ")
checking_savings = int(checking_savings_raw)

print("""\nHow much do you have in investment accounts? Please liquidate all your
 stocks, bonds, IRAs, etc, so they will be ready to invest in more amazing options.""")
investments_raw = input("$ ")
if not investments_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    investments_raw = input("$ ")
investments = int(investments_raw)

print("""\nInclude what you have stashed under the mattress, and be sure to check 
under chair cushions. Add the amount here (round to nearest dollar.""")
mattress_raw = input("$ ")
if not mattress_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    mattress_raw = input("$ ")
mattress = int(mattress_raw)

print("""\nFine jewelry and precious gems, antiques, fine art, gold bullion? Time for a
visit to the pawn shop. Please enter the amount of cash you get from all these.""")
pawned_raw = input("$ ")
if not pawned_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    pawned_raw = input("$ ")
pawned = int(pawned_raw)

print("\nAre you a trust fund baby? Liquidate now and enter amount.")
trust_fund_raw = input("$ ")
if not trust_fund_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    trust_fund_raw = input("$ ")
trust_fund = int(trust_fund_raw)

print("""\nWhat about a retirement account/401K? Little good they'll do you now. 
Take the early withdrawal penalty and add it here.""")
retirement_raw = input("$ ")
if not retirement_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    retirement_raw = input("$ ")
retirement = int(retirement_raw)

print("""\nSetting aside money in an educational fund for existing or future children?
Get rid of those,too. There's other investing to be done. Enter the amount here.""")
kid_ed_raw = input("$ ")
if not kid_ed_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    kid_ed_raw = input("$ ")
kid_ed = int(kid_ed_raw)

print("""\nDo you have a spouse with life insurance? For the right price, you'll be able to
get that, too. How much is that spouse of yours really worth?""")
spouse_life_raw = input("$ ")
if not spouse_life_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    spouse_life_raw = input("$ ")
spouse_life = int(spouse_life_raw)

print("\nIf you own a house, sell it and add the price you get for it here.")
house_raw = input("$ ")
if not house_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    house_raw = input("$ ")
house = int(house_raw)

print("\nDitto for your car(s). Add their selling price here.")
car_raw = input("$ ")
if not car_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    car_raw = input("$ ")
car = int(car_raw)

print("""\nDitto for any other motor vehicles - RVs, motorcycles, scooters, electric bicycles,
four-wheelers, snowmobiles, jet skis,etc. And don't forget any yachts or
other watercraft.""")
other_motor_raw = input("$ ")
if not other_motor_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    other_motor_raw = input("$ ")
other_motor = int(other_motor_raw)

print("\nReal estate? Time to sell them and add the money here.")
real_estate_raw = input("$ ")
if not real_estate_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    real_estate_raw = input("$ ")
real_estate = int(real_estate_raw)

print("""\nOwn any businesses? Get rid of them and get what money you can from them, and include")
any profit here.""")
businesses_raw = input("$ ")
if not businesses_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    businesses_raw = input("$ ")
businesses = int(businesses_raw)

print("""\nWe've tried to be as comprehensive as possible so that we may best serve you, but
if you own anything else that's worth any money, sell it and add it here. Don't
forget the clothing off your back.""")
other_liquidity_raw = input("$ ")
if not other_liquidity_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    other_liquidity_raw = input("$ ")
other_liquidity = int(other_liquidity_raw)
starting_dollars = (checking_savings + investments + mattress + pawned + trust_fund + retirement +
                    kid_ed + spouse_life + house + car + other_motor + real_estate + businesses + other_liquidity)

print("\nPart One completed!")


# Divider between sections, to be used again between Step 2 and final summary
def major_divider():
    print("""\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ :$: $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n""")


major_divider()


# Step 2 Spend money. Print starting amount.
print(f"Your total liquid assets are: ${starting_dollars}.")
print("\nNow it's time to make some amazing investments.")

# Create dollars_left variable, and set it to starting_dollars.
dollars_left = starting_dollars


# A function that prints out how much money is left after each purchase.
def notify_dollars_left():
    print(f"\nYou have ${dollars_left} to invest.\n")


# Begin for dollars_left >= $1.2 trillion
# 1.2 trillion options
#
# The cost of the peas and country options.
peas_country_cost = 1200000000000000

if dollars_left >= 1200000000000000:
    print("""\nWith your current assets, you may begin with the following options.\n
Each is a bargain at 1.2 trillion dollars.
    1. Invest in the World Peas Fund to solve world hunger for a few years.
       It's also tax-deductible, so there's that.
    2. Buy a politically unstable but very large country, name currently undisclosed for
       national security reasons.\n""")

    peas_country = input("Enter 1 or 2: ")

    # Appending functions to stuff_list_functions based on choice (separate from stuff_list since Ash did it differently
    # than I did). Goes in the summary at the end.
    if peas_country == '1':
        stuff_list.append('peas')
    elif peas_country == '2':
        stuff_list.append('country')
    else:  # Trying to account for user error.
        print("You entered an invalid response. I'll choose for you.")
        stuff_list.append('country')

    dollars_left = dollars_left - peas_country_cost

# $50 billion dollar investment
football_space_cost = 50000000000000

if dollars_left < 1200000000000000 and dollars_left >= 50000000000000:
    notify_dollars_left()
    print("""Use $50 billion toward an amazing investment. Choose between the following:
    1. Buy a new professional football franchise, the TTIWW,This Time It Will Work Football League.
    2. How about becoming an investor in Space Force and receive an honorary ranking of Admiral
       (the Admiral part is not verified).""")

    football_space = input("Enter 1 or 2: ")
    if football_space == '1':
        stuff_list.append('football')
    elif football_space == '2':
        stuff_list.append('space_force')
    else:  # Account for user error.
        print("You entered an invalid response. You entered an invalid response. I'll choose for you.")
        stuff_list.append('football')

    dollars_left = dollars_left - football_space_cost

# $2 billion dollar options
island_titanic_cost = 2000000000000

if dollars_left >= 2000000000000:
    notify_dollars_left()
    print("""For two billion dollars, you can have one of these:
    1. A private resort island off the coast of Florida. The buildings have only minor
       cosmetic damage from the last hurricane.
    2. A replica of the Titanic, scaled to size and replicated down to the last detail.
       Ready for a high seas voyage!""")

    island_titanic = input("Enter 1 or 2: ")
    if island_titanic == '1':
        stuff_list.append('island')
    elif island_titanic == '2':
        stuff_list.append('titanic')
    else:  # Account for user error.
        print("You entered an invalid response. I'll choose for you.")
        stuff_list.append('island')

    dollars_left = dollars_left - island_titanic_cost

# $500 million option
jupiter_igloo_cost = 500000000000

if dollars_left >= 500000000000:
    notify_dollars_left()
    print("""For $500 million dollars, you have the following investment choices:
    1. A human mission to Jupiter, including landing and putting your personal brand flag in the
       virgin soil. Just imagine what a great photo or video it would make.
    2. Become a venture capitalist, and put your $500 million to a new start-up company,
       the Luxury Igloo Company, which builds custom igloo mansions on the vast, yet unclaimed
       continent of Antarctica.""")
    jupiter_igloo = input("Enter 1 or 2: ")
    if jupiter_igloo == '1':
        stuff_list.append('jupiter')
    elif jupiter_igloo == '2':
        stuff_list.append('igloo')
    else:  # Account for user error.
        print("You entered an invalid response. I'll choose for you.")
        stuff_list.append('igloo')

    dollars_left = dollars_left - jupiter_igloo_cost

# $100,000,000,000 option $100 million

art_jet_cost = 100000000

if dollars_left >= 100000000:
    notify_dollars_left()
    print("""For $100 million dollars, you have the following investment choices:
    1. Purchase fine art! The painting, Portrait de le Chien Sans Barb, by Vincent Van Dog
       has reappeared on the art market! It would look great in your living room!
    2. How about a private jet that seats up to 180 passengers? You can transport you and
       your closest buds to a pool party in Florida, then be back in NYC for dinner!""")
    art_jet = input("Enter 1 or 2: ")
    if art_jet == '1':
        stuff_list.append('art')
    elif art_jet == '2':
        stuff_list.append('jet')
    else:  # Account for user error.
        print("You entered an invalid response. I'll choose for you.")
        stuff_list.append('art')

    dollars_left = dollars_left - art_jet_cost

    # Ash's contribution to Part 2
choice = 'nothing'

if dollars_left >= 50000000:
    while choice == 'nothing':
        choice = str(input('''\nChoose between the following options.

    1. Commission a genetics laboratory to create pigeons the size of pelicans. $33110000
    2. Hold a flag referendum to change the United States flag. $31250010
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 50,000,000 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 33110000
        stuff_list.append('pigeons')
    elif '2' in choice:
        dollars_left -= 31250010
        stuff_list.append('flag')
    elif '3' in choice:
        print('Not a fan? Alright, moving on.')
        print(' ')

choice = 'nothing'

if dollars_left >= 16000000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Lick Fork, a quaint town in West Virginia. $12500500
    2. A car that, upon honking the horn, uses the rest of the gas to shoot off like a rocket. $14300050
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 16,890,000 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 12500500
        stuff_list.append('Lick Fork')
    elif '2' in choice:
        dollars_left -= 14300050
        stuff_list.append('rocket car')
    elif '3' in choice:
        dollars_left -= 12500500
        stuff_list.append('Lick Fork')
        print("Sorry, you're buying Lick Fork.")
        print(' ')

    choice = 'nothing'

if dollars_left >= 2000000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. An insane mansion in the middle of nowhere in Wyoming. $1757000
    2. A flip phone that has Oprah on speed dial. $1525000
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 2,589,950 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 1757000
        stuff_list.append('mansion')
    elif '2' in choice:
        dollars_left -= 1525000
        stuff_list.append('Oprah')
    elif '3' in choice:
        print('Feeling cheap today! No problem.')
        print(' ')

choice = 'nothing'

if 'mansion' in stuff_list:
    while choice == 'nothing':
        choice = str(input('''Would you like to purchase home insurance for $10000?

    1. Yes
    2. No
'''))
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 10000
        stuff_list.append('insurance')
    if '2' in choice:
        print('Okay, your choice.')
        print(' ')

choice = 'nothing'

if dollars_left >= 800000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Some sick spy gear. $510025
    2. Commission Christian Louboutin to create antiheels, where the toe is higher than the heel. $525000
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 832,950 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 510025
        stuff_list.append('spy gear')
    elif '2' in choice:
        dollars_left -= 525000
        stuff_list.append('antiheels')
    elif '3' in choice:
        print("Look who doesn't know fashion.")
        print(' ')

choice = 'nothing'

if dollars_left >= 290000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. A loud horn to scare fish away from your boat. $150250
    2. A strangely life-like model of Gibby from iCarly. $175500
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 307,950 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 150250
        stuff_list.append('horn')
    elif '2' in choice:
        dollars_left -= 175500
        stuff_list.append('Gibby')
    elif '3' in choice:
        print('Yeah, I understand.')
        print(' ')

choice = 'nothing'

if dollars_left >= 2000000:
    while choice == 'nothing':
        choice = str(input('''Perhaps a donation?

Choose between the following options.

    1. Donate $1,000,000 to wildlife conservation.
    2. Donate $1,000,000 to starving children.
    3. I hate charity.

Which donation would you like to make?
'''))
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 1000000
        stuff_list.append('wildlife')
    elif '2' in choice:
        dollars_left -= 1000000
        stuff_list.append('children')
    elif '3' in choice:
        stuff_list.append('cheap')
        print('Wow. Just you wait, cheapskate.')
        print(' ')

choice = 'nothing'

if dollars_left >= 100000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. A ring holder that screeches "PRECIOUSSSS" when given a ring. $75250
    2. A 300 foot long selfie stick. $68500
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 132,450 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 75250
        stuff_list.append('precious')
    elif '2' in choice:
        dollars_left -= 68500
        stuff_list.append('selfie stick')
    elif '3' in choice:
        print('No? Alright, then.')
        print(' ')

choice = 'nothing'

if dollars_left >= 50000:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. A book subscription where one word is sent per week for ease of reading. $35300
    2. A telescope that has a high quality printed picture of the stars instead of a lens. $37550
    3. Neither

Which opportunity would you like to invest in?
'''))  # min 57,200 left
        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Try again.")
    if '1' in choice:
        dollars_left -= 35300
        stuff_list.append('books')
    elif '2' in choice:
        dollars_left -= 37550
        stuff_list.append('telescope')
    elif '3' in choice:
        print("Someone isn't a fan of learning.")
        print(' ')

# Cat's contribution to Part 2
stuff_list_cat = []

# lists of things to purchase with data: Title, Amount, Buying Text, Text to Print after
vacuum = ["Crystal Vacuum", 17000,
          "The Crystal Ergoripado Vacuum Cleaner! Designed by Lukasz Jemoil this vacuum is "
          "\ndecorated with 3,730 Swarovski crystals! For the low price of ""$17,000!",
          "Your overpriced vacuum cleaner broke."]
cravings_box = ["Cat", 16000, "Buy 3,200 Taco Bell Cravings Boxes for $1600.",
                "You ate all of the 3,200 taco bell cravings boxes... you did this to yourself."]
pigeon_milk = ["Pigeon Milk Investment",
               12000, "$12000 for a majority stock ownership in Greenfield Pigeon Milk Farms!",
               "The pigeon milk you invested in doesn't end up being as popular as test groups determined, "
               "you lost your money."]
doge_coin = ["Doge Coin", 11000, "Invest $11000 dollars into Doge Coin!", "Doge coin is a joke, you lost $16000"]
time_share = ["Time Share", 8000, "Spend $8000 to buy a time share on a small volcanic island in the Mediterranean.",
              "Your time share investment went to waste, the volcano erupted and your dreams are washed away in a "
              "sea of lava"]
lawn_mower = ["Lawn Mower", 7000, "Purchase a high end ride-on lawn mower for $7000.",
              "You never used your lawn mower once and your dreams of starting a lawn mowing business slipped "
              "through your fingers."]
german_shepard = ["German Shepard", 2700, "Buy an overpriced purebred german shepard for $2700.",
                  "Your german shepard ran away."]
beaver_business = ["Beaver Trapping Business", 4000, "Purchase $4000 of equipment to start a beaver trapping business.",
                   "All of your beaver traps were stolen by beavers to make a dam."]
airbnb = ["Fancy Airbnb", 1500, "$1500 for a one night stay at a luxury airbnb in the city!",
          "Your airbnb didn't quite workout as expected... you woke up in a bathtub full of ice missing a kidney."]
australia = ["Australia Plane Ticket", 2000, "$2000 for a one-way plane ticket to Australia!",
             "The moment you landed in Australia you got bitten by a venomous snake."]
racoons = ["Racoons", 800, "Purchase several racoons for $800 to start a petting zoo.",
           "Your petting zoo business has come to a sudden halt... The racoons bit a child and you are "
           "now being sued."]
magical_stick = ["Magical Stick", 900, "Buy a magical stick for $900 from a mysterious stranger who claims it will "
                 "help you defeat your enemies.", "With the help of your newly purchased magic stick you learned that "
                 "magic isn't real, you got your butt kicked"]
fitbit_stocks = ["FitBit Stocks", 600, "Purchase 600 dollars worth of Fit Bit stocks.", "Who even uses Fit Bit "
                 "anymore? You now owe money for your stocks."]
carrier_pigeons = ["Carrier Pigeons", 700, "Buy an entire flock of carrier pigeons for $700", "Your neighbor purchased "
                   "an entire flock of hunting falcons.... your pigeons are all dead."]


# function takes in the list containing the item info
def prompt_user_for_purchase(item1, item2):

    print("Choose between the following options:")
    print("1.", item1[2])
    print("2.", item2[2])
    print("3. eh... I'll pass...")

    user_input = int(input("Make your decision: "))
    while user_input < 1 or user_input > 3:
        user_input = int(input("Invalid Selection! Try again: "))

    if user_input == 1:
        print("Excellent decision!")
        return item1
    elif user_input == 2:
        print("Excellent decision!")
        return item2
    else:
        print("your loss")
        return 0


if dollars_left >= 15000:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(vacuum, cravings_box)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 10000:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(pigeon_milk, doge_coin)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 5000:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(time_share, lawn_mower)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 2500:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(german_shepard, beaver_business)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 1000:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(airbnb, australia)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 750:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(racoons, magical_stick)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

if dollars_left >= 500:
    print(f"\nYou currently have ${dollars_left} to invest.")
    purchase = prompt_user_for_purchase(fitbit_stocks, carrier_pigeons)
    if purchase != 0:
        stuff_list_cat.append(purchase)
        dollars_left = dollars_left - purchase[1]

choice = 'nothing'

if dollars_left >= 420:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. A lettuce grower. Imagine being able to walk a few steps in the comfort of your home 
    and pick out your (fresh) salad for lunch! $300
    2. A mystery box of Pokemon cards. (May contain first gen first edition) $420
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 300 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 300
            stuff_list.append('grower')

    elif '2' in choice:
        if dollars_left - 420 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 420
            stuff_list.append('mystery box')

    elif '3' in choice:
        print('Did not like those options? Alright.')

choice = 'nothing'

if dollars_left >= 210:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. 32 inch Tube TV. $210
    2. Spark plugs. $100
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 210 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 210
            stuff_list.append('tv')

    elif '2' in choice:
        if dollars_left - 100 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 100
            stuff_list.append('spark')

    elif '3' in choice:
        print('You never know when you need spark plugs. Whatever.')

choice = 'nothing'

if dollars_left >= 100:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. 4th of July Christmas tree. $80
    2. Pretty picture frame. $50
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 100 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 80
            stuff_list.append('tree')

    elif '2' in choice:
        if dollars_left - 100 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 50
            stuff_list.append('frame')

    elif '3' in choice:
        print('It was a really pretty frame.')

choice = 'nothing'

if dollars_left >= 50:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Surprised filled stocking. $40
    2. Portable CD player. $30
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 50 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 40
            stuff_list.append('stocking')

    elif '2' in choice:
        if dollars_left - 50 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 30
            stuff_list.append('CD')

    elif '3' in choice:
        print("Now you'll never know the surprise.")

choice = 'nothing'

if dollars_left >= 25:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Cooking book. $20
    2. Tiny pillow. $15
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 25 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 20
            stuff_list.append('book')

    elif '2' in choice:
        if dollars_left - 25 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 15
            stuff_list.append('pillow')

    elif '3' in choice:
        print("It's your life.")

choice = 'nothing'

if dollars_left <= 10 and dollars_left >= 0:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Shoe Laces. $6
    2. Popsicle sticks. $5
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 10 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 6
            stuff_list.append('laces')

    elif '2' in choice:
        if dollars_left - 10 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 5
            stuff_list.append('sticks')

    elif '3' in choice:
        print('Could have had a cute project.')

if dollars_left >= 3:
    print('You currently have ${}'.format(dollars_left), 'to invest.')
    while choice == 'nothing':
        choice = str(input('''Choose between the following options.

    1. Random rock from the streets. $3
    2. Pack of gum. $3
    3. Neither

Which opportunity would you like to invest in?'''))

        if '1' not in choice and '2' not in choice and '3' not in choice:
            choice = 'nothing'
            print("Invalid choice. Please try again!")

    if '1' in choice:
        if dollars_left - 5 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 3
            stuff_list.append('rock')

    elif '2' in choice:
        if dollars_left - 5 < 0:
            print('Sorry, You are out of money!')
        else:
            dollars_left -= 3
            stuff_list.append('gum')

    elif '3' in choice:
        print('Makes sense.')

print("You've finished Part Two!\n")

# Portfolio Summary
major_divider()
print("Part Three: PORTFOLIO SUMMARY")
print("\nCongratulations! You're well on your way to an amazing financial future!")
print("\nYour personalized portfolio summary:")

if dollars_left < 0:
    print(f"\nYour remaining balance is in the red, ${dollars_left}.")
else:
    print(f"\nYou have ${dollars_left} remaining to invest.")

# 1.2 trillion options
if 'peas' in stuff_list:
    print("""\nYou invested in the World Peas Fund to solve world hunger for a few years. People got sick
of eating peas after six months and so stopped eating them. The agricultural system collapsed
due to overproduction of peas and underproduction of every other crop. Money left over: $0.""")

if 'country' in stuff_list:
    print("""\nYou bought a country. There was a military coup, and now the country is a failed state.
Money remaining: $0.""")

# $50 billion
if 'football' in stuff_list:
    print("""\nYou invested in the TTIWW, This Time It Will Work Football League. Unfortunately, it didn't.
Better luck next time. Money left of this investment: $0.""")

if 'space_force' in stuff_list:
    print("""\nYou invested $50 billion in Space Force. It's been used up on administrative costs. Oh, and the
Admiralty thing didn't work out. Something about anti-corruption.""")

# $2 billion
if 'island' in stuff_list:
    print("""\nYou chose a private resort island... in region that regularly gets hurricanes... So...
The buildings took major cosmetic damage. Total left of the investment: $0.""")

if 'titanic' in stuff_list:
    print("""\nYou purchased a replica of the Titanic. True to its original design, it sank while on
its maiden voyage. Luckily, this time there were enough lifeboats for everyone. However,
the ship was totally lost along with the investment. Perhaps it'll make a good movie
someday.""")

# $500 million
if 'jupiter' in stuff_list:
    print("""\nYou invested in a human mission to Jupiter. It was scrapped after it was pointed out that
the planet has no firm surface. But not before all the money was spent.""")

if 'igloo' in stuff_list:
    print("""\nYou invested in the Antarctica-based Luxury Igloo Company. For some reason, no one
wanted an igloo mansion. On Antarctica. Go figure. Not before the corporate igloo headquarters
was built there. Between that and the daily cost to maintain it, your $500 million
is no more.""")

# $100 million
if 'art' in stuff_list:
    print("""\nYou purchased Portrait de le Chien Sans Barb. Turns out that it's not the famous painting
we thought it was. It's not worth any money. At all. Unless you can sell it. But that's
highly unlikely.""")

if 'jet' in stuff_list:
    print("""\nYou purchased a private jet. The good news is everyone survived. The bad news
is the plane crashed while attempting to take off. You may be facing fines.""")

# Ash's contribution to Part 3
if 'pigeons' in stuff_list:
    print('')
    print('The massive pigeons you decided to create have proven to be slightly '
          'more of an annoyance than the old pigeons. The amount of pigeon poop '
          'in public has nearly doubled. But wow those are some large pigeons.')
if 'flag' in stuff_list:
    print('')
    print('You chose to change the United States flag. You are now constantly assaulted '
          'in public by hicks who feel you have disrespected "Merica" by changing the '
          'flag. You can hardly go out without being spit on, but others thought it '
          'was funny, so it was worth it, right?')
if 'Lick Fork' in stuff_list:
    print('')
    print('The town of Lick Fork has grown on you. Sure, the well water tastes a bit '
          'rusty, and the townfolk seem to be gearing up for a riot with actual '
          'pitchforks and torches, but the town is just so quaint.')
if 'rocket car' in stuff_list:
    dollars_left -= 10000000
    print('')
    print('You bought a car that blasts off like a rocket with your remaining gas '
          'at the honk of a horn. The first time you used the rocket feature, you '
          'killed many and injured more. The damages were astounding. You ended up '
          'paying $10 million to those affected by this tragedy. What did you expect? ')
if 'mansion' in stuff_list and 'insurance' not in stuff_list:
    print('')
    print("Since $10000 was too much for you after buying this $1757000 home, "
          "you went without insurance. Well, the people in a neighboring town "
          "didn't appreciate your fancy house making them look back, so it was "
          "torn down in the night with no witnesses to point blame. Should have "
          "forked over the money for the insurance, huh? ")
if 'insurance' in stuff_list:
    print('')
    dollars_left += 1757000
    print('The people in a neighboring town to your mansion in Wyoming thought you '
          'were trying to make them look bad, so your house was mysteriously torn '
          'down in the night. But you wisely bought insurance so you got your '
          '$1757000 back, hooray!')
if 'Oprah' in stuff_list:
    print('')
    print('At first Oprah was happy to talk to you about your childhood and how '
          'to move forward with your life goals. But soon, after your daily calls '
          'to complain about your day, she found herself feeling rather creeped '
          'out. She sent an assistant to destroy the flip phone and she changed '
          'her phone number.')
if 'spy gear' in stuff_list:
    print(' ')
    dollars_left -= 100000
    print('The U.S. government found your purchase of excessively expensive spy gear '
          'suspicious, so your gear was seized and you were fined $100000.')
if 'antiheels' in stuff_list:
    print('')
    dollars_left += 11500025
    print("Some time after you commissioned Christian Louboutin to craft antiheels, "
          "the trend spread like wildfire. You can't open a magazine these days "
          "without seeing models breaking their ankles in antiheels. You received "
          "$11500025 from your investment, so far.")
if 'horn' in stuff_list:
    print('')
    print("You bought a horn that scares fish away from your boat. Well, you certainly "
          "don't have to worry about sharks, I guess.")
if 'Gibby' in stuff_list:
    print('')
    print('Your strangely life-like model of Gibby from iCarly is a favorite possession '
          'of yours. The actor who played Gibby liked your instagram post when you '
          'posted a picture of your model.')
if 'precious' in stuff_list:
    print('')
    dollars_left -= 101570
    print('Once, when placing a ring in your screeching ring stand, the hand on the ring '
          'stand grips your finger so tightly that you cannot move. The ring stand '
          'screeches "THIIIIIIIEEEEF!" When you get to the hospital, doctors are forced '
          'to remove your third finger. Your hospital bill was $101570.')
if 'selfie stick' in stuff_list:
    print('')
    print("Your 300 foot selfie stick was snatched ten minutes after you started "
          "using it at DisneyLand. You got some cool drone-like pictures, though.")
if 'books' in stuff_list:
    print('')
    print('The knowledge you have gained from your book subscription has changed your '
          'life. You read through a lovely self-help book, and now you feel like you '
          'can tackle whatever challenges come your way.')
if 'telescope' in stuff_list:
    print('')
    print('After some time of using your telescope with a printed picture of the stars '
          'instead of a lens, you are a master at recognizing constellations. It '
          'really impresses people when you point them out in the real night sky.')
if 'wildlife' in stuff_list:
    print('')
    print('Your donation to wildlife conservation helped save an endangered species '
          'of rhinos. The foundation dedicated to saving these rhinos name their '
          'facility after you. Your heart is warm with the knowledge that you have '
          'done good in the world.')
if 'children' in stuff_list:
    print('')
    print('You receive photos in the mail of some of the starving children your '
          'donation helped to feed. The foundation dedicated to dispersing food to '
          'children in need name their facility after you. Your heart is warm with the '
          'knowledge that you have done good in the world.')

# Cat's contribution to Part 3
for x in range(len(stuff_list_cat)):
    print("\n", stuff_list_cat[x][3])

if 'cheap' in stuff_list:
    print('')
    print('You went on a hunting trip in the wild because you thought it would impress '
          'others if you shot a lion with a high-powered gun from a distance the lion '
          'could not even see you from. As you made your way toward the wildlands, you '
          'hear a whistle from the trees. Thousands of the starving children you chose '
          'not to donate to emerge. They have white-hot anger in their eyes. The crowd '
          'parts and a dozen lions stride forward. Before you can react, the head child '
          'whistles again and the lions rip you to pieces. If only you had compassion '
          'in your heart, then you might have donated a portion of your stack of cash. ')
if 'grower' in stuff_list:
    print('')
    print("You were so excited to try out your new lettuce grower but you left"
          "it in the sun too long and now all of your lettuce is dead.")
if 'mystery box' in stuff_list:
    print('')
    print("Your Pokemon card investment was useless... no first gen cards and "
          "the they were stolen by some lame kid anyways.")
if 'tv' in stuff_list:
    print('')
    print("Upon plugging in your TV you discovered that it does not work..."
          "after numerous customer service calls and being on hold for hours"
          "you gave up. What a waste.")
if 'spark' in stuff_list:
    print('')
    print("Your spark plugs ended up sitting in the garage for years and years."
          "Let's face it, they will never be used.")
if 'tree' in stuff_list:
    print('')
    print("""You purchased a Christmas tree for 4th of July and couldn't decorate it because
 you couldn't find any 4th of July Christmas ornaments.""")
if 'frame' in stuff_list:
    print('')
    print("""You purchased a picture frame but realized you didn't have any pictures to put in it.""")
if 'stocking' in stuff_list:
    print('')
    print("""You purchased a surprise filled stocking. It had coals in it.""")
if 'book' in stuff_list:
    print('')
    print("""You purchased a cooking book. The recipes were awful.""")
if 'pillow' in stuff_list:
    print("")
    print("""You purchased a tiny pillow. And never figured out why.""")
if 'laces' in stuff_list:
    print("")
    print("""You purchased shoe laces. They all broke and you need new ones again.""")
if 'sticks' in stuff_list:
    print("")
    print("You purchased popsicle sticks. They were all broken.")
if 'rock' in stuff_list:
    print("")
    print("You picked up a rock for $3. Sounds like a bum deal to me.")
if 'gum' in stuff_list:
    print("")
    print("Pack of gum was black licorice - flavored. Tasted awful.")
