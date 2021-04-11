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
investments_raw = input("S ")
if not investments_raw.isdigit():
    print("Invalid entry. Please try again (only numbers)")
    investments_raw = input("$ ")
investments = int(investments_raw)

print("""\nInclude what you have stashed under the mattress, and be sure to check 
under chair cushions. Add the amount here (round to nearest dollar.""")
mattress_raw = input("S ")
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
print("\nNow it's time to make some amazing investments./n")

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
    print(""""\nWith your current assets, you may begin with the following options.
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
# Portfolio Summary
print("""Congratulations! You've finished!\n""")
major_divider()
print("PORTFOLIO SUMMARY")
print(f"\nYou have ${dollars_left} remaining to invest.")
print("\nYour personalizied protfolio summary:")
# 1.2 trillion options
if 'peas' in stuff_list:
    print("""\nYou invested in the World Peas Fund to solve world hunger for a few years. People got sick
of eating peas after six months and so stopped eating them. The agricultural system collapsed
due to overproduction of peas and underproduction of every other crop. Money left over: $0.""")

if 'country' in stuff_list:
    print("""\nYou bought a country. There was a military coup, and now the country is a failed state.
Money remaining: $0.""")

# $50 billiion
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
