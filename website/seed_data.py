from .models import db , Data
from website import create_app
app = create_app()
stages_data = [
    { 'level': '1.1.0.0', 'text': 'You stir from a 2-year coma. The hospital room is dimly lit, machines beep erratically, and a chilling groan echoes from outside. A strange silence hangs heavy in the air.', 'question': 'What do you do?', 
     'choices': 'Face the unknown and step outside the room$Look around the room.', 'location': 'hospital_room' , 'next_level': '1.1.1.0$1.1.2.0' , 'item' : "" , 'use' : ""},  
    { 'level': '1.1.1.0', 'text': 'You venture into the hallway. From the shadows, two lurching figures turn towards you - zombies! Their guttural snarls fill the air.', 'question': 'What do you do?',  
     'choices': 'Run in the opposite direction, hoping for an escape.$Retreat back into the room and barricade the door.', 'location': 'hospital_corridor' , 'next_level': '1.1.1.1$1.1.2.0' , 'item' : "" , 'use' : ''},
    { 'level':'1.1.1.1' , 'text': "Terror propels you down the dark corridor. But ahead, more shuffling figures emerge from the gloom! There's nowhere to go… The zombies close in, their hunger overpowering your desperate struggle." , 'question' : ' YOU DIE!','choices': 'RESTART' , 'location':'hospital_corridor2' , 'next_level': '1.1.0.0' , 'item' : "" , 'use' : ''},
    { 'level': '1.1.2.0' , 'text': ' Panic rising, you scour the room. Through a cracked window, you glimpse a city in ruins. The realization hits you - a zombie outbreak! Amongst the chaos, you find a rusty but sturdy knife tucked away in a cabinet.' , 'question': 'What do you do?' ,'choices': 'Armed with the knife, charge outside and fight.$Keep searching, looking for a better escape route.' , 
     'location' : 'hospital_room' , 'next_level': '1.1.2.1$1.2.0.0' , 'item' : "Knife" , 'use' : ""},
    { 'level' : '1.1.2.1' , 'text' : 'Adrenaline surges as you confront the zombies head-on, knife in hand. Their strength is terrifying! The zombies overpower you. Their relentless attack leaves you no chance.' , 'question' : 'YOU DIED!' , 'choices' : 'RESTART' , 'location' : 'hospital_corridor' , 'next_level' : '1.1.0.0' , 'item' : "", 'use':"Knife" },
    
    { 'level': '1.2.0.0', 
    'text': 'Your eyes scan the room desperately. An abandoned AC vent catches your attention.You squeeze through the vent and drop into a dimly lit storage room. Boxes and crates are stacked high, coated in a thick layer of dust. The air hangs heavy with a musty scent and an unsettling silence.', 
    'question': 'What do you do?', 
    'choices': 'Search the crates for supplies$Look for another exit from the room.', 
    'location': 'storage_room' , 
    'next_level': '1.2.1.0$1.2.2.0',
    'item' : "" , 'use' : ""} ,
    { 'level': '1.2.1.0', 
    'text': 'You pry open a crate, revealing a small first-aid kit . A glimmer of hope sparks; these could be valuable for what lies ahead.',  
    'question': 'What do you do?', 
    'choices': 'Search for more supplies$Take the supplies and head towards the exit you noticed earlier.', 
    'location': 'storage_room' , 
    'next_level': '1.2.1.1$1.2.2.0',
    'item' : "First-aid" , 'use' : ""} ,
    { 'level': '1.2.1.1', 
    'text': 'As you rummage through more crates, a piercing scream echoes from somewhere deeper within the hospital. Should you investigate or abandon the search?', 
    'question': 'What do you do?', 
    'choices': 'Investigate the scream, hoping to help or find an escape route$Flee back to safety, fearing the worst.', 
    'location': 'storage_room' , 
    'next_level': '1.2.2.0$1.2.0.0', 
    'item' : "" , 'use' : ""} ,
    { 'level': '1.2.2.0', 
    'text': 'You approach the door with the sliver of light. Holding your breath, you turn the handle. It creaks open, leading to a narrow service corridor.', 
    'question': 'What do you do?', 
    'choices': 'Venture into the corridor, hoping it leads to an exit$Hesitate, unsure about what lies ahead.', 
    'location': 'dark_corridor' , 
    'next_level': '1.3.0.0$1.2.0.0', 
    'item' : "" , 'use' : "" }  , 
    { 'level': '1.3.0.0', 
    'text': 'The corridor opens into the deserted main lobby of the hospital. Chairs are overturned, and a broken reception desk lies in disarray. Sunlight streams weakly through shattered windows. In the center of the room, two zombies hunched over the reception desk, their moans echoing through the hall.', 
    'question': 'What do you do?', 
    'choices': 'Approach the Desk $Head for the Exit ', 
    'location': 'hospital_lobby' , 
    'next_level': '1.3.1.0$1.4.0.0', 
    'item' : "" , 'use' : "" } ,
    { 'level': '1.3.1.0', 
  'text': 'As you creep closer to the desk, a muffled whimper reaches your ears. You peer over the edge and spot a middle-aged woman cowering beneath the desk, her eyes wide with terror. This must be the source of the scream you heard earlier.',  
  'question': 'What do you do?', 
  'choices': 'Help the Woman $Leave Her Behind ', 
  'location': 'hospital_lobby' , 
  'next_level': '1.3.2.0$1.4.0.0', 
  'item' : "" , 'use' : "Knife" } ,
    { 'level': '1.3.2.0', 
  'text': 'In a desperate attempt to help the woman, you reach down towards her. Unfortunately, the commotion attracts the attention of the zombies. They turn towards you with a horrifying growl.',  
  'question': 'Your fate is sealed. YOU DIE!', 
  'choices': 'RESTART', # No choices here, this is a dead end
  'location': 'hospital_lobby' , 
  'next_level': '1.1.0.0', # Back to the beginning
  'item' : "" , 'use' : "" } ,
    {
  'level': '1.4.0.0',
  'text': 'Ignoring the cries for help, you charge towards the exit, adrenaline pumping. The heavy glass doors are locked. You slam against them with all your might, but they hold firm. Panic starts to cloud your judgment.',
  'question': 'What do you do?',
  'choices': 'Search for another exit.$Break a window to escape.',
  'location': 'hospital_lobby',
  'next_level': '1.4.1.0$1.4.2.0',
  'item': "",
  'use': ""},
    {
  'level': '1.4.1.0',
  'text': 'Keeping your eyes peeled for danger, you frantically scan the lobby for another escape route. A fire escape door catches your eye in the corner of the room.',
  'question': 'What do you do?',
  'choices': 'Head towards the fire escape.$Look for something to break the window with.',
  'location': 'hospital_lobby',
  'next_level': "1.5.0.0$1.4.2.0",
  'item': "",
  'use': ""
    },
    {
  'level': '1.4.2.0',
  'text': 'With a surge of determination, you grab a nearby chair and hurl it at the glass window. The impact shatters the glass, raining down shards everywhere. The alarm blares to life, echoing through the empty halls.',
  'question': "Now that you've created a distraction, what do you do?",
  'choices': 'Climb through the broken window.$Carefully navigate around the broken glass and head for the exit.',
  'location': 'hospital_lobby_broken_window',
  'next_level': '1.5.1.0$1.5.2.0',
  'item': "",
  'use': ""
},
    {
      'level': '1.5.1.0',
  'text': 'Ignoring the sharp edges, you clamber through the broken window, squeezing your body through the jagged opening. Cuts sting your skin, but you ignore the pain. You\'re free.',
  'question': "Where do you go from here?",
  'choices': 'Leave through the main gate towards the highway.$Leave through the back gate towards the smaller roads.',
  'location': 'outside_hospital',
  'next_level': '1.6.0.0$1.6.1.0',
  'item': "",
  'use': ""
      },
    {
      'level': '1.5.2.0',
  'text': 'Picking your way carefully through the broken glass, you manage to reach the exit door. You fling it open and bolt outside, the blaring alarm at your back.',
  'question': 'Where do you go from here?',
  'choices': 'Leave through the main gate towards the highway.$Leave through the back gate towards the smaller roads.',
  'location': 'outside_hospital',
  'next_level': '1.6.0.0$1.6.1.0',
  'item': "",
  'use': ""
      },
    
    {
  'level': '1.5.0.0',
  'text': 'Reaching the fire escape, you pull on the handle. Thankfully, it swings open easily. You waste no time to run outside into the parking lobby.',
  'question': 'You reach the parking lobby. What do you do next?',
  'choices': 'Leave through the main gate towards the highway.$Leave through the back gate towards the smaller roads.',
  'location': 'outside_hospital',
  'next_level': '1.6.0.0$1.6.1.0',
  'item': "",
  'use': ""
},
    {
      'level' : '1.6.0.0',
      'text' : 'LEVEL CLEARED! YOU HAVE ESCAPED THE ZOMBIE INFESTED HOSPITAL!',
      'question' : '',
      'choices' : 'NEXT LEVEL',
      'location' : 'main_road',
      'next_level' : '2.1.0.0',
      'item' : "",
      'use' : ""
    },
    {
      'level': '1.6.1.0',
      'text' : 'LEVEL CLEARED! YOU HAVE ESCAPED THE ZOMBIE INFESTED HOSPITAL!',
      'question' : '',
      'choices' : 'NEXT LEVEL',
      'location' : 'small_road',
      'next_level' : '2.1.0.0',
      'item' : "",
      'use' : ""
    },
    {
  "level": "2.1.0.0",
  "text": "The sun beats down mercilessly as you trudge along the dusty road. Every muscle in your body aches, and your throat feels parched. You scan the desolate landscape for any sign of life, but there's nothing. Just the relentless sun and the endless road stretching before you.",
  "question": "You continue walking for a while, until you spot a lone car abandoned on the side of the road. Smoke curls from its hood. What do you do?",
  "choices": "Investigate the car.$Keep walking.",
  "location": "deserted_road",
  "next_level": "2.1.1.0$2.4.0.0",
  "item": "",
  "use": ""
},
    {
  "level": "2.1.1.0",
  "text": "Cautiously approaching the car, you peer through the cracked windshield. A figure hunches over the steering wheel, unmoving. You call out, but there's no response. With a deep breath, you reach for the handle and pull open the creaking door.",
  "question": "Inside the car, you find a man, pale and sweating profusely. There's a gruesome bite wound on his arm. He looks at you with pleading eyes. What do you do?",
  "choices": "Help him out of his misery.$Run as far as possible from this infected man.",
  "location": "car_interior",
  "next_level": "2.1.3.0$2.4.0.0",
  "item": "",
  "use": ""
},
    {
  "level": "2.1.3.0",
  "text": "Compassion compels you to help the injured man. You offer him a bandage from your first-aid kit, but he pushes it away weakly. 'It's too late for me,' he rasps. 'Do me a kindness... end it before I turn.' Tears well up in your eyes, but you understand his plea.",
  "question": "Will you end his suffering?",
  "choices": "Grant his wish and end his suffering.$Refuse to kill someone with your own hands.",
  "location": "dying_man_in_car",
  "next_level":"2.1.3.1$2.4.0.0",
  "item" : "",
  "use" : ""
  },
    {
      "level":"2.1.3.1",
      "text":"As you are about to end the man's life, he utters his final words . 'Please take care of my daughter.. I gave up my life to protect her all this time.' You agree and end the man's suffering.",
      "question" : "You notice a small girl sitting in the back seat. What do you do?",
      "choices":"Take her out of the car and kill the man.$Kill the man in front of her.",
      "location":"small_girl",
      "next_level":"2.2.0.0$2.3.0.0",
      "item":"",
      "use":""
    },
  
    {
      "level":"2.2.0.0",
      "text":"As you are taking the girl out of the car, you notice that she has a very old bite mark which has almost healed.",
      "question":"What do you do with the girl?",
      "choices":"Leave her and run away as she might turn into a zombie anytime soon.$Ignore the mark and kill her father.",
      "location":"small_girl",
      "next_level":"2.4.0.0$2.2.1.0",
      "item":"Flashlight",
      "use":"item"
    },
    {
      "level":"2.2.1.0",
      "text":"You kill the man but his daughter's eyes are filled with tears. You console her and you both start heading down the road. ",
      "question":"You find an abandoned car which looks like it might still work. What do you do?",
      "choices":"Hotwire the car and try to make it work.$Leave the car and start moving quickly to avoid any zombies",
      "location":"abandoned_car",
      "next_level":"2.2.2.0$2.2.3.0",
      "item":"",
      "use":""
    },
    {
      "level":"2.2.2.0",
      "text":"You hotwire the car and bursts back into life! You and the girl into the car and drive off into the abandoned city.",
      "question":"You ask the girl for her name and she whispers 'Ellie'. (You have found yourself a new companion!)",
      "choices":"NEXT",
      "location":"sunset",
      "next_level":"3.1.0.0",
      "item":"",
      "use":""
    },
    {
      "level":"2.2.3.0",
      "text":"You and the girl abandon the car and start walking off down the road towards the sunset not knowing what destiny has in store for you both.",
      "question":"You ask the girl for her name and she whispers 'Ellie'. (You have found yourself a new companion!)",
      "choices":"NEXT",
      "location":"sunset",
      "next_level":"3.0.0.0",
      "item":"",
      "use":""
    },
    {
      "level":"2.3.0.0",
      "text":"As you try to kill the man, her daughter leaps at you from the backseat with a pocketknife in her hand.",
      "choices":"She pushes the knife deep inside the side of your throat and YOU DIE!",
      "choices":"RESTART",
      "location":"abandoned_car",
      "next_level":"2.1.0.0",
      "item":"",
      "use":""
    }
    ,{
      "level":"2.4.0.0",
      "text":"You leave the person behind and start heading down the road. ",
      "question":"You find an abandoned car which looks like it might still work. What do you do?",
      "choices":"Hotwire the car and try to make it work.$Leave the car and start moving quickly to avoid any zombie interactions.",
      "location":"abandoned_car",
      "next_level":"2.4.1.0$2.4.2.0",
      "item":"",
      "use":""
    },
    {
      "level":"2.4.1.0",
      "text":"You hotwire the car and bursts back into life! You drive off down the road towards the sunset not knowing what destiny has in store for you.",
      "question":"",
      "choices":"NEXT",
      "location":"sunset",
      "next_level":"3.0.0.0",
      "item":"",
      "use":""
    },
    {
      "level":"2.4.2.0",
      "text":"You abandon the car and start walking down the road towards the sunset not knowing what destiny has in store for you." ,
      "question":"",
      "choices":"NEXT",
      "location":"sunset",
      "next_level":"3.0.0.0",
      "item":"",
      "use":""
    }
    ]

def populate_db():
    with app.test_request_context():
        for stage in stages_data:
            level = stage['level']
            existing_stage = Data.query.filter_by(level=level).first()

            if existing_stage:
            # Update the existing stage with new data
                for key, value in stage.items():
                    setattr(existing_stage, key, value)  
            else:
                new_stage = Data(**stage) 
                db.session.add(new_stage)

        db.session.commit()