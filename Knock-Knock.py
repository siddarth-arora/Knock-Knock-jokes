import random 
import time

jokes = {
        "Leon":"Leon on me when you’re not strong!",
       "Annie":"Annie thing you can do I can do better!",
        "Lena":"Lena a little closer, and I’ll tell you another joke!",                                                                                                                                                                                                 
      "Quiche":"Can I have a hug and a quiche?",
          "Wa":"What are you so excited about?!",
       "Adore":"Adore is between you and me so please open up!",
        "I am":"Don’t you even know who you are?!",
      "A leaf":"A leaf you alone if you leaf me alone.", 
        "Hike":"I didn’t know you liked Japanese poetry!",
"A little old lady":"Wow, I didn’t know you could yodel!",
   "Ice cream soda":"Ice scream soda people can hear me!",
            "Haven":"Haven you heard enough of these knock-knock jokes?",
            "Keith":"Keith me, my thweet prince!",
           "Europe":"No, you’re a poo!",
            "Double":"W!",
          "Anita":"Anita drink of water so please let me in!",
          "Alex":"Alex-plain when you open the door!",
          "Olive":"Olive next door. Hi neighbor!",
          "Hawaii":"I’m fine, Hawaii you?",
          "Nun":"Nunya business!",
          "June":"June know how long I’ve been knocking out here?",
          "Spell":"W-H-O!",
          "Oscar":"Oscar silly question and get a silly answer!",
          "Conrad":"Conrad-ulations! That was a good knock-knock joke!",
          "Anita":"Anita go to the bathroom!",
          "Dejav":"Knock, knock",
          "Owls say":"Yes, they do.",
          "Cargo":"Cargo beep, beep and vroom, vroom!",
          "To":"No, it’s to whom!",
          "Cash":"No thanks, but I’d love some peanuts.",
          "Mustache":"Mustache you a question, but I’ll shave it for later!",
          "Dwayne":"Dwayne the bathtub ⏤ I’m dwowning!",
          "Ya":"No thanks,I use Bing or Google",
          "Control Freak":"Okay, now you say control freak who?",
          "Billy Bob Joe Penny":"Really? How many Billy Bob Joe Pennies do you know?",
          "Theodore":"Theodore wasn’t opened so I knocked.",
          "Alec":"Alec it when you ask me questions.", 
          "Cereal":"Cereal pleasure to meet you!",
          "Cantaloupe":"Cantaloupe to Vegas, you’re too young!",
          "Beats":"Beats me.",
          "Kenya":"Kenya feel the love tonight?",
          "Interrupting sloth":"(20 seconds of silence)Sloooooooooth",
          "Ida":"Surely, it’s pronounced Idaho.",
          "Cabbage":"You expect a cabbage to have a last name?",
          "Sweden":"Sweden sour chicken!",
          "Art":"R2-D2!",
          "Smellmop":"Ew, no thanks!",
          "I need a puh":"Then why don’t you find a toilet!",
          "Hatch":"God bless you!",
          "Tank":"You’re welcome.",
          "Voodoo":"Voodoo you think you are asking me so many questions?",
          "Boo":"Uh, why are you crying?",
          "Honeybee":"Honeybee a dear and open up will you?",
          "Says":"Says me, that’s who!",
          "Alice":"Alice so quiet. Let’s make some noise!",
          "Iran":"Iran all the way here!",
          "Doctor":"No, no, just the doctor.",
          "Euripides":"Euripides jeans and you pay for them, okay?",
          "Amish":"Really, you’re a shoe? Uh, okay.",
          "Figs":"Figs the doorbell!",
          "Dishes":"Dishes the police, open up!",
          "Lettuce.":"Lettuce in or we’ll break down the door!",
          "Razor":"Razor hand and dance the boogie!",
          "I am":"So you have identity problems, huh?",
          "Luke":"Luke through the keyhole and see!",
          "Amos":"A mosquito!",
          "Howard":"Howard I know?",
          "Odysseus":"Odysseus the last straw!",
          "A Mayan":"A Mayan in the way?",
          "Abe":"Abe-C-D-E!",
          "Icing":"Icing so loudly so everyone can hear me!",
          "Tennis":"Tennis five plus five!",
          "Nicholas":"A Nicholas is not much money these days.",
          "Candice":"Candice door open or am I stuck out here?",
          "Cow":"No cow says mooooooo!",
          "Robin":"Robin you! Now hand over the cash",
          "Annie":"Annie way you can let me in?",
          "Canoe":"Canoe come and play? I’m bored!",
          "Gorilla":"Gorilla me a hamburger!"
}
          



aa=random.choice(list(jokes.keys()))
bb=jokes[aa]


while True:
    print('KNOCK, KNOCK')
    yup=input()
    if(yup=='Whos there?' or yup=="Who's there?" or yup=='Who is there?'):
       print(aa)
    else:
        print("please type [Who's there?]")
        yup=input()
        if(yup=='Whos there?' or yup=="Who's there?" or yup=='Who is there?'):
          print(aa)
        else:
          print("please type [Who's there?]")
          yup=input()
          if(yup=='Whos there?' or yup=="Who's there?" or yup=='Who is there?'):
            print(aa)
          
    sup=input()
    if(sup==aa+" who?"):
      print(bb)
    else:
        print("please type "+ aa + " who?" )
        sup=input()
        if(sup==aa+" who?"):
          print(bb)
        else:
          print("please type "+ aa + " who?" )
          sup=input()
          if(sup==aa+" who?"):
            print(bb)
            time.sleep(1)  