def find_highest_bid(bidding_dictionary):
    highest_bid=0
    highest_bidder=""

    for bidder in bidding_dictionary:
       if bidding_dictionary[bidder] > highest_bid:
          highest_bidder=bidder  
          highest_bid=bidding_dictionary[bidder]

    print(f"The winner is {bidder} with a bid of {highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name=input("Enter Your name: ")
    print(f"Welcome to the secret auction program {name}")
    price=int(input("Enter your bid: "))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes'or'no': ").lower()
    if should_continue=="no":
       continue_bidding=False
       find_highest_bid(bids)
    else:
        continue_bidding=True
        print("\n"*20)

  