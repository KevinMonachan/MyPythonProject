import art
print(art.logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def ceaser(text,shift_amount,cipher_direction):
    output_text=""
    if cipher_direction == "decrypt":
        shift_amount *= -1

    for letters in text:
        if letters not in alphabet:
            output_text += letters
        else:
            shifted_position = alphabet.index(letters) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {cipher_direction}ed text is {output_text}")

should_continue = True
while should_continue:

  cipher_direction=input("Enter Encrypt or Decrypt: ").lower() 
  text=input("Enter the message: ").lower()
  shift_amount=int(input("Enter the shift amount: "))
  output=ceaser(text,shift_amount,cipher_direction)

  result=input("Do you want to continue? Yes or No: ").lower()
  if result=="no":
    should_continue=False
    print("Goodbye")