import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkFont
from PIL import Image, ImageTk



class PickYourJourney:
    def __init__(self, root):
        """
        Initialize the game with the main window, fonts, UI elements, and music.
        """
        self.root = root
        self.root.title("The Story Forge")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1ec1d6")



        # Custom fonts
        self.title_font = tkFont.Font(family="Impact", size=70, weight="bold")
        self.story_font = tkFont.Font(family="Times New Roman", size=28)
        self.button_font = tkFont.Font(family="Helvetica", size=20, weight="bold")

        # Title
        self.title_label = tk.Label(root, text="The Story Forge", font=self.title_font, fg="#d31ed6", bg="#1ec1d6")
        self.title_label.pack(pady=30)



        # Story text
        self.story_text = tk.Label(root, text="", wraplength=1000, justify="center", font=self.story_font, fg="#FFFFFF", bg="#1ec1d6")
        self.story_text.pack(pady=40)

        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#1ec1d6")
        self.button_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Navigation frame
        self.nav_frame = tk.Frame(root, bg="#1ec1d6")
        self.nav_frame.pack(pady=20)

        # Back button
        self.back_button = tk.Button(self.nav_frame, text="Back", font=self.button_font, bg="#FFFFFF", fg="#1e1e1e", relief="raised", bd=3, command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=10)

        # Q&A section label
        self.qa_label = tk.Label(root, text="Any questions?", font=self.story_font, bg="#1ec1d6")
        self.qa_label.pack(pady=10)

        # Q&A frame
        self.qa_frame = tk.Frame(root, bg="#1ec1d6")
        self.qa_frame.pack(pady=20)

        # Q&A entry and button
        self.qa_entry = tk.Entry(self.qa_frame, font=self.story_font, width=50, bg="#030202")
        self.qa_entry.pack(side=tk.LEFT, padx=10)
        self.qa_button = tk.Button(self.qa_frame, text="Ask", font=self.button_font, bg="#FFFFFF", fg="#1e1e1e", relief="raised", bd=3, command=self.handle_qa)
        self.qa_button.pack(side=tk.LEFT)

        # Player name
        self.player_name = None

        # History of choices for navigation
        self.history = []

        # List to store player choices
        self.choices = []

        # Start game
        self.start_screen()
        
    def start_screen(self):
        while True:
            self.player_name = simpledialog.askstring("Input", "What is your name?", parent=self.root)
            if self.player_name and self.player_name.strip():
                self.player_name = self.player_name.strip()
                break
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid name.")
        self.show_story(f"Hi {self.player_name}, Step into a world where you guide the narrative. From peaceful mountain retreats to eerie haunted halls, vibrant markets to ancient secrets hidden in libraries — each path offers a new experience, shaped by your decisions.Whether you're craving calm, chasing adventure, or braving something darker...your next story awaits.")
        
        self.create_buttons([
            ("Begin the Journey", self.title_screen),
            ("Stop and miss out", self.quit_game)
        ])
    def title_screen(self):
        self.show_story(f"{self.player_name}, Please choose between the 3 Genre of Stories that are Provided. Don't Worry, You can Always Come back and choose another Genre if you want!")
        self.create_buttons([
            ("Adventure Stories", self.adventure_stories),
            ("Horror Stories", self.horror_stories),
            ("Laid-Back Stories", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])

    def adventure_stories(self):
        self.show_story("Welcome to the Adventure Story Section!")
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.create_buttons([
            ("Grand Prison Escape", self.prison_escape_desc),
            ("Lost in the Jungle", self.jungle_desc),
            ("Arctic Survival", self.arctic_desc),
            ("Choose A Different Genre", self.title_screen),
            ("Stop", self.quit_game)
        ])
        self.history = []
        self.choices = []
        
    def horror_stories(self):
        self.show_story("Welcome to the Horror Stories Section!")
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.create_buttons([
            ("Haunted Escape", self.haunted_mansion_desc),
            ("The Hollow Portrait", self.hollow_portrait_desc),
            ("Whispering Lighthouse", self.lighthouse_desc),
            ("Choose A Different Genre", self.title_screen),
            ("Stop", self.quit_game)
        ])
        self.history = []
        self.choices = []
        
    def laid_back_stories(self):
        self.show_story("Welcome to the Laid Back Stories Section!")
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.create_buttons([
            ("Your Cake Business", self.business_desc),
            ("Mountain Retreat", self.mountain_retreat_desc),
            ("The Library Visit", self.library_visit_desc),
            ("Choose A Different Genre", self.title_screen),
            ("Stop", self.quit_game)
        ])
        self.history = []
        self.choices = []

    # Adventure Story Descriptions
    def prison_escape_desc(self):
        self.add_to_history(self.adventure_stories)
        self.show_story("In this story you are trapped in a prison for a crime that you did not commit,\n however, no one is listening to you, so you must find a way to escape!\nWould you like to play this story?")
        self.create_buttons([
            ("Continue With the Story", self.start_Prison_Escape),
            ("Choose A Different Story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])

    def jungle_desc(self):
        self.add_to_history(self.adventure_stories)
        self.show_story("Your plane has crashed in the heart of an uncharted jungle. With limited supplies and danger\n all around, every choice could mean survival—or a quick end. \nWill you escape, uncover secrets, or become part of the jungle forever?")
        self.create_buttons([
            ("Continue With the Story", self.jungle_start),
            ("Choose A Different Story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])

    def arctic_desc(self):
        self.add_to_history(self.adventure_stories)
        self.show_story("Your research plane crashes in the frozen Arctic. With strange signals, hidden caves, \nand deadly wildlife, you must act fast to stay warm, stay alive, and uncover\n what really happened. Will you be rescued—or disappear into the ice?")

        self.create_buttons([
            ("Continue With the Story", self.arctic_start),
            ("Choose A Different Story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])

    # Horror Story Descriptions
    def haunted_mansion_desc(self):
        self.add_to_history(self.horror_stories)
        self.show_story("You’ve entered the infamous Blackwood Manor for one night—just to prove you’re brave. \nBut the house remembers its past, and not all of it is dead. Will you\n uncover its secrets or become part of its legend?")
        self.create_buttons([
            ("Continue With the Story", self.haunted_mansion_start),
            ("Choose A Different Story", self.horror_stories),
            ("Stop", self.quit_game)
        ])

    def hollow_portrait_desc(self):
        self.add_to_history(self.horror_stories)
        self.show_story("You’ve inherited a mysterious old house—and its portrait isn’t just decoration. With every choice,\n the painting changes… and so do you. Can you break the cycle, \nor will your image be the next to stare back?")
        self.create_buttons([
            ("Continue With the Story", self.hollow_portrait_start),
            ("Choose A Different Story", self.horror_stories),
            ("Stop", self.quit_game)
        ])

    def lighthouse_desc(self):
        self.add_to_history(self.horror_stories)
        self.show_story("On a fog-drenched night, you explore the abandoned lighthouse where a keeper once vanished without a trace. \nEchoes of his final night guide your steps—if you listen closely.\n Can you uncover his story before dawn breaks?")
        self.create_buttons([
            ("Continue With the Story", self.lighthouse_start),
            ("Choose A Different Story", self.horror_stories),
            ("Stop", self.quit_game)
        ])

    # Laid-Back Story Descriptions
    def business_desc(self):
        self.add_to_history(self.laid_back_stories)
        self.show_story("You’ve just opened your first bakery—fresh cakes, new hope, and your first three customers. But every choice\n you make can lead to success, scandal, or shuttered doors.\n Who will you serve first... and how sweet will your story end?")
        self.create_buttons([
            ("Continue With the Story", self.business_start),
            ("Choose A Different Story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])

    def mountain_retreat_desc(self):
        self.add_to_history(self.laid_back_stories)
        self.show_story("Escape to a peaceful cabin in the mountains for a weekend of fresh air, quiet moments, and memorable choices. \n Whether you explore waterfalls, sketch at scenic lookouts, \nor sip coffee in a cozy village café, every path leads to a different kind of serenity.")
        self.create_buttons([
            ("Continue With the Story", self.mountain_retreat),
            ("Choose A Different Story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])

    def library_visit_desc(self):
        self.add_to_history(self.laid_back_stories)
        self.show_story("Spend a peaceful afternoon in a charming local library filled with books, secrets, and quiet surprises. \nWhether you solve a mystery, join a book club, or explore ancient\n manuscripts, every choice opens a new chapter of discovery.")
        self.create_buttons([
            ("Continue With the Story", self.library_visit),
            ("Choose A Different Story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
    def start_Prison_Escape(self):
        
        self.add_to_history(self.prison_escape_desc) 
        """
        Start the game by asking for the player's name and presenting the initial story.
        """
        # Clear history and choices when starting a new game

        

        self.show_story(f"Hello, {self.player_name}. You have been put in this high-security prison for a crime you did not commit.\n"
                        "Oh, and if you get caught escaping, you’ll be sent to an isolated island. Good luck.")

        self.create_buttons([
            ("Wake up and look around", self.first_choice),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Picked the Grand Prison Escape Game")

    def first_choice(self):
        self.add_to_history(self.start_Prison_Escape)  # Add current state to history after updating the state
        """
        Present the first set of choices to the player.
        """
        self.show_story(f"{self.player_name}, you wake up after being knocked out. Three guards are standing on the other side of the bars.\n"
                        "What will you do?")
        self.create_buttons([
            ("Try to steal the keys", self.steal_guard_shift_changes),
            ("Try to fight the guards", self._fight_guard_shift_change),
            ("Wait and sit there", self.guard_shift_change),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Wake up and look around")

    def guard_shift_change(self):
        self.add_to_history(self.first_choice)  # Add current state to history after updating the state
        """
        Present the next set of choices after the guard shift change.
        """
        self.show_story(f"{self.player_name}, after three hours, two guards leave for their shift change, leaving a sleepy guard standing watch.\n"
                        "Now is your chance to escape!")
        self.create_buttons([
            ("Try to steal the keys from the sleepy guard", self.steal_keys_success),
            ("Just sit and wait", self.excess_laziness),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])

        self.choices.append("Wait and sit there")

    def _fight_guard_shift_change(self):
        self.add_to_history(self.first_choice)  # Add current state to history after updating the state
        """
        Present the next set of choices after the guard shift change.
        """
        self.show_story(f"{self.player_name}, You tried to throw a punch at the guard but realize you are too weak to do anything \n after three hours, two guards leave for their shift change, leaving a sleepy guard standing watch.\n"
                        "Now is your chance to escape!")
        self.create_buttons([
            ("Try to steal the keys from the sleepy guard", self.steal_keys_success),
            ("Just sit and wait", self.excess_laziness),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Try to fight the guards")

    def steal_guard_shift_changes(self):
        self.add_to_history(self.first_choice)  # Add current state to history after updating the state
        """
        Present the next set of choices after the guard shift change.
        """
        self.show_story(f"{self.player_name}, You tried to steal the keys from one of the guard, but one of them notices and throws you back. \n after three hours, two guards leave for their shift change, leaving a sleepy guard standing watch.\n"
                        "Now is your chance to escape!")
        self.create_buttons([
            ("Try to steal the keys again", self.steal_keys_success),
            ("Just sit and wait", self.excess_laziness),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Try to steal the keys")

    def steal_keys_success(self):
        self.add_to_history(self.guard_shift_change)  # Add current state to history after updating the state
        """
        Handle the player's success in stealing the keys.
        """
        self.show_story(f"{self.player_name}, you carefully take the keys from the sleepy guard and unlock your cell. You are free!\n"
                        "What will you do next?")
        self.create_buttons([
            ("Hide behind a supply cart", self.sneak_around),
            ("Run for the exit", self.run_for_exit),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Try to steal the keys from the sleepy guard")

    def sneak_around(self):
        self.add_to_history(self.steal_keys_success)  # Add current state to history after updating the state
        """
        Handle the player's choice to sneak around.
        """
        self.show_story(f"{self.player_name}, you hide behind a supply cart as two guards walk past. You see a vent and a staircase leading to the exit.")
        self.create_buttons([
            ("Climb into the vent", self.vent_escape),
            ("Take the stairs", self.staircase_escape),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Hide behind a supply cart")

    def run_for_exit(self):
        self.add_to_history(self.steal_keys_success)  # Add current state to history after updating the state
        """
        Handle the player's choice to run for the exit.
        """
        self.show_story(f"{self.player_name}, you try to run for the exit, but the noise alerts the guards. You are caught and sent to the isolated island.")
        self.create_buttons([
            ("Play Again", self.start_Prison_Escape),
            ("Quit", self.quit_game),
            ("Show choice report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Run for the exit")

    def vent_escape(self):
        self.add_to_history(self.sneak_around)  # Add current state to history after updating the state
        """
        Handle the player's choice to escape through the vent.
        """
        self.show_story(f"{self.player_name}, you crawl through the vent and reach the laundry room where prisoner uniforms are stored.")
        self.create_buttons([
            ("Steal a guard uniform", self.disguise_escape),
            ("Try to sneak past the workers", self.get_caught),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Climb into the vent")

    def disguise_escape(self):
        self.add_to_history(self.vent_escape)  # Add current state to history after updating the state
        """
        Handle the player's success in disguising as a guard.
        """
        self.show_story(f"{self.player_name}, you put on a guard uniform and walk confidently through the prison, blending in.\n"
                        "You reach the main entrance and step outside into the cold night air. You've escaped!\n"
                        "Congratulations, you have successfully escaped the prison!")
        
        self.choices.append("Steal a guard uniform")
        self.create_buttons([
            ("Play Again", self.start_Prison_Escape),
            ("Quit", self.quit_game),
            ("Show Choice Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])


    def staircase_escape(self):
        self.add_to_history(self.sneak_around)  # Add current state to history after updating the state
        """
        Handle the player's choice to take the stairs.
        """
        self.show_story(f"{self.player_name}, you take the stairs, but a guard spots you and sounds the alarm. You are captured and sent to the isolated island.")
        
        
        self.choices.append("Take the stairs")
        self.create_buttons([
            ("Play Again", self.start_Prison_Escape),
            ("Quit", self.quit_game),
            ("Show Choice Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])


    def get_caught(self):
        self.add_to_history(self.vent_escape)  # Add current state to history after updating the state
        """
        Handle the player getting caught.
        """
        self.show_story(f"{self.player_name}, you hesitate too long, and the guards eventually catch you. You are sent to the isolated island.")  
        
        self.choices.append("Try to sneak past the workers")
        self.create_buttons([
            ("Play Again", self.start_Prison_Escape),
            ("Quit", self.quit_game),
            ("Show Choice Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])


    def excess_laziness(self):
        self.add_to_history(self.guard_shift_change)  # Add current state to history after updating the state
        """
        Handle the player's choice to remain lazy.
        """
        self.show_story(f"{self.player_name}, You have waited for several days, and no opportunities to escape have shown up, you will spend the rest of your life here.")
        self.create_buttons([
            ("Play Again", self.start_Prison_Escape),
            ("Quit", self.quit_game),
            ("Show Choices Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])
        
        self.choices.append("Just sit and wait")
    

# Start of the Code for Lost in the Jungle
    def jungle_start(self):
        
        self.add_to_history(self.adventure_stories)
        """Starting point for jungle survival story."""
        self.show_story(f"{self.player_name}, your plane crashed in the middle of a dense, uncharted jungle. \n"                     "You're the only survivor, with limited supplies and no communication. The jungle is full of dangers \n"                     "and mysteries. Can you survive long enough to be rescued?")
        self.create_buttons([
            ("Assess your surroundings", self.jungle_first_choice),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the Jungle Story")

    def jungle_first_choice(self):
        self.add_to_history(self.jungle_start)
        self.show_story(f"{self.player_name}, you look around and see:\n"                      "1. The smoldering wreckage of the plane with some supplies\n"                      "2. A dense jungle path leading away from the crash site\n"                       "3. A nearby river with fresh water")
        self.create_buttons([
            ("Search the plane wreckage", self.jungle_search_plane),
            ("Explore the jungle path", self.jungle_explore_path),
            ("Go to the river", self.jungle_go_to_river),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Assess your surroundings")

    def jungle_search_plane(self):
        self.add_to_history(self.jungle_first_choice)
        self.show_story(f"{self.player_name}, you find a first aid kit, some canned food, and a flare gun. \n"  "Suddenly, you hear rustling in the bushes nearby. It could be an animal or something else.")
        self.create_buttons([
            ("Investigate the noise", self.jungle_investigate_noise),
            ("Fire the flare gun", self.jungle_fire_flare),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Search the plane wreckage")

    def jungle_explore_path(self):
        self.add_to_history(self.jungle_first_choice)
        self.show_story(f"{self.player_name}, You go towards the path, but it is covered in thorns \n" "However, luckily you find  a flare gun and a first aid kit and store it.\n" "Suddenly, you hear rustling in the bushes nearby. It could be an animal or something else.")
        self.create_buttons([
            ("Investigate the noise", self.jungle_investigate_noise),
            ("Go to the thorn filled path", self.thorned_death),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Search the plane wreckage")
        
    def thorned_death(self):
        self.add_to_history(self.jungle_explore_path)
        self.show_story(f"{self.player_name}, Unfortunately, every part of your body hurts now, and you are unable to do anything.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Went into the Thorned Path despite warnings")
        
    def jungle_go_to_river(self):
        self.add_to_history(self.jungle_first_choice)
        self.show_story(f"{self.player_name}, The river's water is clean so you drink some \n" "You also find a flare gun and a first aid kit and store it.\n"  "Suddenly, you hear rustling in the bushes nearby. It could be an animal or something else." )
        self.create_buttons([
            ("Investigate the noise", self.jungle_investigate_noise),
            ("Go for a swim", self.Drowned_death),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Go to the river")
        
    def Drowned_death(self):
        self.add_to_history(self.jungle_go_to_river)
        self.show_story(f"{self.player_name}, You go for a swim but your foot gets trapped and you are unable to escape, leading for you to drown.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Decided to Swim")

    def jungle_investigate_noise(self):
        self.add_to_history(self.jungle_search_plane)
        self.show_story(f"{self.player_name}, you cautiously approach the noise and discover a wounded jaguar. \n"    "It growls at you but seems too injured to attack.")
        self.create_buttons([
            ("Try to help the jaguar", self.jungle_help_jaguar),
            ("Back away slowly", self.jungle_back_away),
            ("Use the flare gun to scare it", self.jungle_scare_jaguar),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Investigate the noise")

    def jungle_help_jaguar(self):
        self.add_to_history(self.jungle_investigate_noise)
        self.show_story(f"{self.player_name}, you use the first aid kit to treat the jaguar's wounds. Surprisingly, it lets you. \n"                      "After tending to it, the jaguar limps away but keeps looking back at you, almost like it wants you to follow.")
        self.create_buttons([
            ("Follow the jaguar", self.jungle_follow_jaguar),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Try to help the jaguar")

    def jungle_follow_jaguar(self):
        self.add_to_history(self.jungle_help_jaguar)
        self.show_story(f"{self.player_name}, you follow the jaguar deep into the jungle. It leads you to a hidden cave \n" "with ancient carvings on the walls and a small freshwater spring inside.")
        self.create_buttons([
            ("Explore the cave", self.jungle_explore_cave),
            ("Make this your shelter", self.jungle_make_shelter),
            ("Continue following the jaguar", self.jungle_continue_following),
            ("Stop", self.quit_game),
            ("Pick another story",self.adventure_stories)
        ])
        self.choices.append("Follow the jaguar")

    def jungle_explore_cave(self):
        self.add_to_history(self.jungle_follow_jaguar)
        self.show_story(f"{self.player_name}, as you explore the cave, you discover ancient artifacts and a map carved into the wall \n"                     "that shows a route through the jungle to a coastal village. This could be your way to civilization!")
        self.create_buttons([
            ("Follow the map to the village", self.jungle_village_ending),
            ("Stay and study the artifacts", self.jungle_study_artifacts),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Explore the cave")

    def jungle_village_ending(self):
        self.add_to_history(self.jungle_explore_cave)
        self.show_story(f"{self.player_name}, after three days of following the map, you reach a small coastal village. \n"                      "The villagers welcome you and arrange for your return home. You survived the jungle and discovered \n"                     "an ancient civilization in the process!")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Follow the map to the village")

    def jungle_grab_supplies(self):
        self.add_to_history(self.jungle_search_plane)
        self.show_story(f"{self.player_name}, you quickly gather the supplies and retreat to a safe distance. \n"                      "With these resources, you can now focus on building shelter and signaling for help.")
        self.create_buttons([
            ("Build a shelter", self.jungle_build_shelter),
            ("Try to signal for help", self.jungle_signal_for_help),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Grab supplies and retreat")

    def jungle_fire_flare(self):
        self.add_to_history(self.jungle_search_plane)
        self.show_story(f"{self.player_name}, you fire the flare gun into the sky. A passing ship sees your signal and sends a rescue team! \n"                      "You're saved and brought back to civilization.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Fire the flare gun")

    def jungle_back_away(self):
        self.add_to_history(self.jungle_investigate_noise)
        self.show_story(f"{self.player_name}, you back away in fear, but you also back away from a chance to be saved.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Back away slowly")

    def jungle_scare_jaguar(self):
        self.add_to_history(self.jungle_investigate_noise)
        self.show_story(f"{self.player_name}, you scare away the Jaguar, But the flare gun causes a rescue team to come and rescue you!")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Use the flare gun to scare it")



    def jungle_make_shelter(self):
        self.add_to_history(self.jungle_follow_jaguar)
        self.show_story(f"{self.player_name}, you decide to make the cave your shelter. It's safe from predators and has fresh water. \n"     "After several days, a search party finds your shelter and rescues you!")
        self.create_buttons([
            ("Play Again", self.show_story_options),
            ("Quit", self.quit_game),
            ("Show Choice Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Make this your shelter")

    def jungle_continue_following(self):
        self.add_to_history(self.jungle_follow_jaguar)
        self.show_story(f"{self.player_name}, you continue following the jaguar deeper into the jungle. \n"     "It leads you to a hidden temple where a tribe of indigenous people take you in and help you recover.")
        self.create_buttons([
            ("Play Again", self.show_story_options),
            ("Quit", self.quit_game),
            ("Show Choice Report", self.show_choices_report),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Continue following the jaguar")

    def jungle_study_artifacts(self):
        self.add_to_history(self.jungle_explore_cave)
        self.show_story(f"{self.player_name}, you spend days studying the artifacts. You discover they hold clues to a \n"     "long-lost civilization. You use the flare gun to get rescued, and your findings make you famous!")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.jungle_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.adventure_stories)
        ])
        self.choices.append("Stay and study the artifacts")
    
##### Code for Starting Your Business

    def business_start(self):
        self.add_to_history(self.laid_back_stories)
        self.show_story(f"{self.player_name}, Hi, You are a young owner of a brand new bakery titled {self.player_name}'s Cakes. Today is your first day.")
        self.create_buttons([
            ("Put up the open sign!", self.business_first_choice),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the Starting your own business story.")

    def business_first_choice(self):
        self.add_to_history(self.business_start)
        self.show_story(
            f"{self.player_name}, you look around the bakery. It's quiet, with the scent of fresh flour and sugar in the air. 3 customers walk in, which one will you greet first? A man in a suit and tie, who looks like he is in a rush. An elderly lady who is having trouble standing up for a long time. A teenager who is on their phone."
        )
        self.create_buttons([
            ("The man in a suit", self.man_in_suit),
            ("The Elderly Lady", self.the_elderly_lady),
            ("The teenager", self.the_teenager),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Opened shop for the day")

    def man_in_suit(self):
        self.add_to_history(self.business_first_choice)
        self.show_story(
            "You say hi to the man in the suit and ask him what he wants. He says he needs a minute, but stays next to the counter so no other customer can be greeted. After a while, the man finally orders a small piece of cake, and your other customers leave. Your business really struggles in the following days, and you are forced to shut down."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Chose the Man in the Suit")

    def the_teenager(self):
        self.add_to_history(self.business_first_choice)
        self.show_story(
            "You say hi to the teenager and ask her what she wants. She says that she is just here to take pictures for her Instagram. Will you let them take pictures? The other customers are about to leave!"
        )
        self.create_buttons([
            ("let her take pictures", self.let_her_stay),
            ("no, make her leave", self.make_her_leave),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Chose the teenager")

    def let_her_stay(self):
        self.add_to_history(self.the_teenager)
        self.show_story(
            "You let her stay and post. Your business becomes popular and your sales increase!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Let the teenager take pictures for instagram")

    def make_her_leave(self):
        self.add_to_history(self.the_teenager)
        self.show_story(
            "You make the teenager leave, but the other customers have already left. Your business really struggles in the following days, and you are forced to shut down."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Made the teenager leave")

    def the_elderly_lady(self):
        self.add_to_history(self.business_first_choice)
        self.show_story(
            "You say hi to the elderly lady and ask her what she wants. She says she doesn't know what she should get and asks you what flavor cake she should get."
        )
        self.create_buttons([
            ("Vanilla", self.which_ingredients),
            ("Red Velvet", self.which_ingredients),
            ("Chocolate", self.which_ingredients),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Chose the Lady ")

    def which_ingredients(self):
        self.add_to_history(self.the_elderly_lady)
        self.show_story(
            "That old lady thanks you for your recommendation. She asks you what ingredients are in your cakes and how they are made. You think to yourself, she sure is wasting a lot of my time!"
        )
        self.create_buttons([
            ("Answer Honestly", self.answered_honestly),
            ("Lie", self.lied_to_lady),
            ("Say you are not sure", self.did_not_know),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Told the Lady Which ingredients you use")

    def answered_honestly(self):
        self.add_to_history(self.which_ingredients)
        self.show_story(
            "The Old Lady thanks you, and orders what you recommended. She then reveals that she is a famous food critic, and says that she will write a great review for you. Although the other 2 customers have left, your business is now booming and you are making profit!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Answered to the old lady truthfully")

    def lied_to_lady(self):
        self.add_to_history(self.which_ingredients)
        self.show_story(
            "The Old Lady can tell you lied, but orders what you recommended. She then reveals that she is a famous food critic, and says that she will write a bad review for you. The other 2 customers have also left, and your business continues to struggle for the next days."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Lied to the old lady")

    def did_not_know(self):
        self.add_to_history(self.which_ingredients)
        self.show_story(
            "The Old Lady puts up a frown, but orders what you recommended. She then reveals that she is a famous food critic, and says she will write a mediocre review for you. The other 2 customers have also left, and your business continues to be mediocre for the next days."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.business_start),
            ("Stop", self.quit_game),
            ("Pick another story", self.laid_back_stories)
        ])
        self.choices.append("Told the Lady you did not know ingredients")
        
    
    
    def haunted_mansion_start(self):
        self.add_to_history(self.horror_stories)
        self.show_story(f"{self.player_name}, you've dared to spend the night in the haunted Blackwood Manor.\n"
                        "The door slams shut behind you. Where will you explore first?")
        self.create_buttons([
            ("Main Hall", self.mansion_main_hall),
            ("Upstairs", self.mansion_upstairs),
            ("Basement", self.mansion_basement),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the Haunted Mansion Story")

    def mansion_main_hall(self):
        self.add_to_history(self.haunted_mansion_start)
        self.show_story(f"{self.player_name}, in the dusty main hall you see:\n"
                        "1. A flickering candle\n"
                        "2. A grandfather clock ticking backwards\n"
                        "3. A mysterious letter on a table")
        self.create_buttons([
            ("Examine the candle", self.mansion_candle),
            ("Check the clock", self.mansion_clock),
            ("Read the letter", self.mansion_letter),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered the main hall")

    def mansion_candle(self):
        self.add_to_history(self.mansion_main_hall)
        self.show_story(f"{self.player_name}, the candle's flame turns blue as you approach. A whisper comes from it:\n"
                        "'Help us remember...' What will you do?")
        self.create_buttons([
            ("Touch the flame", self.mansion_touch_flame),
            ("Blow it out", self.mansion_blow_out),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Examined the candle")

    def mansion_touch_flame(self):
        self.add_to_history(self.mansion_candle)
        self.show_story(f"{self.player_name}, you see visions of the Blackwood family's last night.\n"
                        "When you wake up, dawn is breaking and you feel at peace.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Touched the flame")

    def mansion_blow_out(self):
        self.add_to_history(self.mansion_candle)
        self.show_story(f"{self.player_name}, darkness envelops you! When light returns, you're outside the mansion.\n"
                        "The door is gone. You'll never forget what happened.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Blew out the candle")

    def mansion_clock(self):
        self.add_to_history(self.mansion_main_hall)
        self.show_story(f"{self.player_name}, the clock chimes 13 times! A secret compartment opens,\n"
                        "revealing a small key. Will you take it?")
        self.create_buttons([
            ("Take the key", self.mansion_take_key),
            ("Leave it", self.mansion_leave_key),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Checked the clock")

    def mansion_take_key(self):
        self.add_to_history(self.mansion_clock)
        self.show_story(f"{self.player_name}, the key fits a hidden door behind a painting.\n"
                        "Inside is the family's diary. Reading it, you learn their tragic story.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took the key")

    def mansion_leave_key(self):
        self.add_to_history(self.mansion_clock)
        self.show_story(f"{self.player_name}, you leave the key. The mansion creaks angrily.\n"
                        "You run outside just as dawn breaks, vowing never to return.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the key")

    def mansion_letter(self):
        self.add_to_history(self.mansion_main_hall)
        self.show_story(f"{self.player_name}, the letter warns: 'Beware the west wing at midnight.'\n"
                        "It's signed by Eleanor Blackwood, dated 100 years ago.")
        self.create_buttons([
            ("Go to west wing", self.mansion_west_wing),
            ("Stay in hall", self.mansion_main_hall),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Read the letter")

    def mansion_west_wing(self):
        self.add_to_history(self.mansion_letter)
        self.show_story(f"{self.player_name}, in the west wing you meet Eleanor's ghost!\n"
                        "She thanks you for reading her letter and shows you a secret exit.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Went to west wing")

    def mansion_upstairs(self):
        self.add_to_history(self.haunted_mansion_start)
        self.show_story(f"{self.player_name}, upstairs you find a child's room. A toy ball rolls to your feet.")
        self.create_buttons([
            ("Pick up the ball", self.mansion_ball),
            ("Leave it", self.mansion_leave_ball),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Went upstairs")

    def mansion_ball(self):
        self.add_to_history(self.mansion_upstairs)
        self.show_story(f"{self.player_name}, a ghost child appears, smiling. She leads you to a treasure\n"
                        "chest full of family heirlooms before showing you the way out at dawn.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Picked up the ball")

    def mansion_leave_ball(self):
        self.add_to_history(self.mansion_upstairs)
        self.show_story(f"{self.player_name}, the ball rolls away sadly. You leave feeling you missed\n"
                        "an opportunity, but at least you survived the night.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the ball")

    def mansion_basement(self):
        self.add_to_history(self.haunted_mansion_start)
        self.show_story(f"{self.player_name}, the basement has a strange altar with a glowing gem.")
        self.create_buttons([
            ("Take the gem", self.mansion_take_gem),
            ("Leave it", self.mansion_leave_gem),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Went to basement")

    def mansion_take_gem(self):
        self.add_to_history(self.mansion_basement)
        self.show_story(f"{self.player_name}, the gem gives you visions of the past!\n"
                        "You understand the family's secrets and leave at dawn as their chosen successor.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took the gem")

    def mansion_leave_gem(self):
        self.add_to_history(self.mansion_basement)
        self.show_story(f"{self.player_name}, you wisely leave the gem. The mansion seems to respect\n"
                        "your choice and lets you leave unharmed at dawn.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.haunted_mansion_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the gem")

    def arctic_start(self):
        self.add_to_history(self.adventure_stories)
        self.show_story(f"""{self.player_name}, your research plane crashes in the Arctic wilderness. Before you:
        
        Smoldering wreckage (possible supplies)
        Distant lights (research station?)
        Strange geometric ice formations""")
        self.create_buttons([
            ("Search wreckage", self.arctic_wreckage),
            ("Go toward lights", self.arctic_lights),
            ("Investigate ice", self.arctic_ice),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Started Arctic survival story")

    def arctic_wreckage(self):
        self.add_to_history(self.arctic_start)
        self.show_story("""The wreckage contains:
        
        Intact survival kit
        Damaged radio transmitter
        Pilot's frozen body""")
        self.create_buttons([
            ("Take survival kit", self.arctic_survival_kit),
            ("Attempt radio repair", self.arctic_radio_repair),
            ("Search pilot", self.arctic_pilot),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Searched plane wreckage")

    def arctic_survival_kit(self):
        self.add_to_history(self.arctic_wreckage)
        self.show_story("""The kit has:
        - 3 days of rations
        - Flare gun (2 flares)
        - First aid supplies
        Suddenly, a polar bear appears!""")
        self.create_buttons([
            ("Fire warning flare", self.arctic_flare),
            ("Hide quietly", self.arctic_hide),
            ("Run toward lights", self.arctic_lights),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took survival kit")

    def arctic_flare(self):
        self.add_to_history(self.arctic_survival_kit)
        self.show_story("""The flare scares the bear away!
        The light reveals a path to the research station.""")
        self.create_buttons([
            ("Follow path", self.arctic_station_path),
            ("Stay at wreckage", self.arctic_wait_rescue),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Used flare gun")

    def arctic_station_path(self):
        self.add_to_history(self.arctic_flare)
        self.show_story("""You reach an abandoned research station:
        Working heater
        Emergency radio
        Strange scientific notes""")
        self.create_buttons([
            ("Use radio", self.arctic_call_rescue),
            ("Read notes", self.arctic_notes),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Reached research station")

    def arctic_notes(self):
        self.add_to_history(self.arctic_station_path)
        self.show_story("""You look into the notes, it says in bolded words:
        YOU FELL RIGHT INTO MY TRAP!
        Suddenly the doors behind you, and you have no way to get out!
        BAD ENDING: Trapped in the research station""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.arctic_start),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Went into research station")

    def arctic_call_rescue(self):
        self.add_to_history(self.arctic_station_path)
        self.show_story("""Rescue arrives in 8 hours!
        You survive with minor frostbite.
        GOOD ENDING: Safe Return""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.arctic_start),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Called for rescue")

    def arctic_lights(self):
        self.add_to_history(self.arctic_start)
        self.show_story("""You reach a research outpost:
        Locked front door
        Broken window
        Solar panel still working""")
        self.create_buttons([
            ("Break in through window", self.arctic_break_in),
            ("Check solar equipment", self.arctic_solar),
            ("Return to wreckage", self.arctic_wreckage),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Approached research station")

    def arctic_break_in(self):
        self.add_to_history(self.arctic_lights)
        self.show_story("""Inside you find:
        Warm bedding
        Canned food supply
        Fully functional radio""")
        self.create_buttons([
            ("Use radio", self.arctic_call_rescue),
            ("Rest and recover", self.arctic_rest),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered research station")

    def arctic_ice(self):
        self.add_to_history(self.arctic_start)
        self.show_story("""The ice formations reveal:
        Perfect geometric patterns
        Hidden cave entrance
        Strange radio interference""")
        self.create_buttons([
            ("Enter cave", self.arctic_cave),
            ("Study patterns", self.arctic_patterns),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Investigated ice formations")

    def arctic_cave(self):
        self.add_to_history(self.arctic_ice)
        self.show_story("""The cave contains:
        Ancient ice murals
        Energy crystals
        Warning signs in Russian""")
        self.create_buttons([
            ("Take crystal", self.arctic_crystal),
            ("Study murals", self.arctic_murals),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered ice cave")

    def arctic_crystal(self):
        self.add_to_history(self.arctic_cave)
        self.show_story("""The crystal:
        Powers your dead radio
        Points toward rescue
        Causes ice instability""")
        self.create_buttons([
            ("Use crystal for rescue", self.arctic_crystal_rescue),
            ("Leave it", self.arctic_leave_crystal),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took energy crystal")

    def arctic_crystal_rescue(self):
        self.add_to_history(self.arctic_crystal)
        self.show_story("""The crystal guides rescuers to you!
        Scientists are fascinated by your discovery.
        SPECIAL ENDING: Scientific Discovery""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.arctic_start),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Used crystal for rescue")

    def arctic_radio_repair(self):
        self.add_to_history(self.arctic_wreckage)
        self.show_story("""You partially repair the radio - 
        it can only receive, not send.
        A weather report warns of coming storms.""")
        self.create_buttons([
            ("Take shelter", self.arctic_shelter),
            ("Risk traveling", self.arctic_lights),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Attempted radio repair")

    def arctic_pilot(self):
        self.add_to_history(self.arctic_wreckage)
        self.show_story("""The pilot has:
        A sealed mission briefing
        Keycard to research station
        Emergency painkillers""")
        self.create_buttons([
            ("Take keycard", self.arctic_keycard),
            ("Read briefing", self.arctic_briefing),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Searched pilot")

    def arctic_keycard(self):
        self.add_to_history(self.arctic_pilot)
        self.show_story("""The keycard gives access to:
        Research station labs
        Classified files
        Restricted areas""")
        self.create_buttons([
            ("Go to station", self.arctic_lights),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took keycard")

    def arctic_briefing(self):
        self.add_to_history(self.arctic_pilot)
        self.show_story("""The briefing reveals:
        - This was no accident
        - Someone sabotaged your plane
        - The research station holds answers""")
        self.create_buttons([
            ("Go to station", self.arctic_lights),
            ("Search wreckage more", self.arctic_wreckage),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Read pilot's briefing")

    def arctic_hide(self):
        self.add_to_history(self.arctic_survival_kit)
        self.show_story("""You hide behind the wreckage, holding your breath.
        The polar bear sniffs around but eventually wanders off.
        You're safe, for now.""")
        self.create_buttons([
            ("Wait and rest", self.arctic_wait_rescue),
            ("Try radio repair", self.arctic_radio_repair),
            ("Run toward lights", self.arctic_lights),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Hid from polar bear")

    def arctic_wait_rescue(self):
        self.add_to_history(self.arctic_hide)
        self.show_story("""Hours pass. As night falls, you fire a flare.
        A rescue team sees it and arrives by snowmobile.
        GOOD ENDING: Patient Rescue""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.arctic_start),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Waited for rescue")

    def arctic_shelter(self):
        self.add_to_history(self.arctic_radio_repair)
        self.show_story("""You build a makeshift shelter from wreckage parts.
        It's cramped but protects you from the storm.
        You hear a voice faintly over the radio...""")
        self.create_buttons([
            ("Respond using crystal", self.arctic_crystal_rescue),
            ("Wait until morning", self.arctic_wait_rescue),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took shelter from storm")

    def arctic_rest(self):
        self.add_to_history(self.arctic_break_in)
        self.show_story("""You rest under warm blankets.
        You regain strength, and in the morning, you spot a rescue chopper.
        You fire a flare to signal it.""")
        self.create_buttons([
            ("Signal chopper", self.arctic_call_rescue),
            ("Stay hidden", self.arctic_wait_rescue),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Rested at station")

    def arctic_solar(self):
        self.add_to_history(self.arctic_lights)
        self.show_story("""You inspect the solar panels and redirect power.
        The door's lock clicks—it's now open.
        Inside, warmth and supplies await.""")
        self.create_buttons([
            ("Enter station", self.arctic_break_in),
            ("Return to wreckage", self.arctic_wreckage),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Repaired solar panels")

    def arctic_patterns(self):
        self.add_to_history(self.arctic_ice)
        self.show_story("""The patterns suggest a message—coordinates?
        You note them and check your map.
        They point to a known emergency cache nearby.""")
        self.create_buttons([
            ("Head to cache", self.arctic_cache),
            ("Ignore and explore cave", self.arctic_cave),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Studied ice patterns")

    def arctic_cache(self):
        self.add_to_history(self.arctic_patterns)
        self.show_story("""At the marked location, you find:
        Rations and heating packs
        Beacon transmitter (working)
        You activate it and wait.""")
        self.create_buttons([
            ("Wait for rescue", self.arctic_wait_rescue),
            ("Head to cave", self.arctic_cave),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Found emergency cache")

    def arctic_murals(self):
        self.add_to_history(self.arctic_cave)
        self.show_story("""The murals depict ancient humans and glowing crystals.
        They seem to have revered the energy as sacred.
        You feel a deeper understanding of the cave's mystery.""")
        self.create_buttons([
            ("Take crystal", self.arctic_crystal),
            ("Leave cave", self.arctic_ice),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Studied murals")

    def arctic_leave_crystal(self):
        self.add_to_history(self.arctic_crystal)
        self.show_story("""You leave the crystal where it is.
        The cave trembles slightly, then falls silent.
        You exit safely and return to the surface.""")
        self.create_buttons([
            ("Head to research station", self.arctic_lights),
            ("Signal for help", self.arctic_wait_rescue),
            ("Pick another story", self.adventure_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the crystal")
   
    def hollow_portrait_start(self):
        self.add_to_history(self.horror_stories)
        self.show_story(f"""{self.player_name}, you have recently inherited a house from a distant relative, and now you have to check it out. 
                    As you enter the house, you see a few things:
                    1. A crooked painting in the main hall
                    2. A locked cabinet with a key on the ground""")
        self.create_buttons([
            ("Straighten the Portrait", self.straighten_portrait),
            ("Unlock the Cabinet", self.check_cabinet),  # Fixed: Changed from read_journal to check_cabinet
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Picked the Hollow Portrait Story")

    def straighten_portrait(self):
        self.add_to_history(self.hollow_portrait_start)
        self.show_story("""You straighten the crooked portrait. As you do, a strange chill runs through the room.
    The portrait’s expression seems... different now. A smile? You spot a note tucked behind the frame:  
    "Day 12: It noticed I touched it." """)
        self.create_buttons([
            ("Read the Note", self.read_portrait_note),
            ("Ignore it and check the Cabinet", self.check_cabinet),
            ("Walk away", self.leave_portrait),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Straightened the portrait")

    def read_portrait_note(self):
        self.add_to_history(self.straighten_portrait)
        self.show_story("""You unfold the note. The handwriting is frantic:  
    "Every time I touch the frame, it changes... and so do I."  
    Behind you, a floorboard creaks—no one else should be here.""")
        self.create_buttons([
            ("Turn around", self.turn_around_noise),
            ("Return to the Cabinet", self.check_cabinet),
            ("Leave the House", self.quit_game),
            ("Pick another story", self.horror_stories)
        ])
        self.choices.append("Read the portrait note")

    def leave_portrait(self):
        self.add_to_history(self.straighten_portrait)
        self.show_story("""You step back from the painting. Its eyes seem to follow you now, subtly tracking as you move.  
    The draft in the room feels colder.""")
        self.create_buttons([
            ("Check the Cabinet", self.check_cabinet),
            ("Leave the House", self.quit_game),
            ("Pick another story", self.horror_stories)
        ])
        self.choices.append("Backed away from the portrait")

    def check_cabinet(self):
        self.add_to_history(self.hollow_portrait_start)
        self.show_story("""You pick up the old key and unlock the cabinet. Inside you find:  
    - A dusty leather-bound journal  
    - A pearl button  
    - A broken pocket watch stuck at 3:07""")
        self.create_buttons([
            ("Open the Journal", self.read_journal),
            ("Take the Button", self.take_button),
            ("Wind the Watch", self.wind_watch),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Opened the cabinet")

    def take_button(self):
        self.add_to_history(self.check_cabinet)
        self.show_story("""You pick up the pearl button. It clings to your skin, warm and oddly alive.  
    When you glance at the portrait, it's missing the button from its jacket.""")
        self.create_buttons([
            ("Show the button to the portrait", self.show_button_to_portrait),
            ("Drop the button", self.drop_button),
            ("Keep it", self.keep_button),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took the pearl button")

    def read_journal(self):
        self.add_to_history(self.check_cabinet)
        self.show_story("""The journal entries begin sensibly, then spiral:  
    "Day 5: I hear it breathing at night."  
    "Day 18: The portrait’s smile is wider than yesterday."  
    Final entry: "It wants out." """)
        self.create_buttons([
            ("Compare it to the Portrait", self.compare_to_portrait),
            ("Close the Journal", self.close_journal),
            ("Take the Journal with you", self.keep_journal),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Read the journal")

    def wind_watch(self):
        self.add_to_history(self.check_cabinet)
        self.show_story("""The watch ticks once... and then starts moving backward.  
    Upstairs, faint footsteps move in sync with the ticking.  
    The portrait’s eyes are closed now.""")
        self.create_buttons([
            ("Go upstairs", self.go_upstairs),
            ("Stop the Watch", self.stop_watch),
            ("Leave the Room", self.leave_room),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Wound the broken watch")

    def compare_to_portrait(self):
        self.add_to_history(self.read_journal)
        self.show_story("""You glance at the portrait—its expression now perfectly matches the journal's final entry.  
    A new line appears in the journal: "YOU LOOK TIRED."  
    Your reflection in the glass blinks… but you didn’t.""")
        self.create_buttons([
            ("Cover the portrait", self.cover_portrait),
            ("Touch the journal again", self.keep_journal),
            ("Run", self.quit_game),
            ("Pick another story", self.horror_stories)
        ])
        self.choices.append("Compared the portrait and journal")

    def turn_around_noise(self):
        self.add_to_history(self.read_portrait_note)
        self.show_story("""You turn, but no one is there.  
    Just an empty hallway—and the portrait is no longer on the wall behind you.""")
        self.create_buttons([
            ("Follow the hallway", self.follow_hallway),
            ("Try to leave", self.quit_game),
            ("Call out", self.call_out),
            ("Pick another story", self.horror_stories)
        ])
        self.choices.append("Turned around to check the noise")

    def follow_hallway(self):
        self.add_to_history(self.turn_around_noise)
        self.show_story("""The hallway seems longer than before. Every door is open just a crack—except one at the far end.  
    A whisper: "You're almost done." But it came from inside your head.""")
        self.create_buttons([
            ("Enter the closed room", self.closed_room),
            ("Run back", self.hollow_portrait_start),
            ("Stay completely still", self.freeze_in_place),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Followed the hallway")

    def show_button_to_portrait(self):
        self.add_to_history(self.take_button)
        self.show_story("""You raise the pearl button toward the portrait.  
    Its eyes brighten, and the missing button reappears on its jacket—your hand goes cold.""")
        self.create_buttons([
            ("Drop the button", self.drop_button),
            ("Keep holding it", self.keep_button),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Showed the button to the portrait")

    def drop_button(self):
        self.add_to_history(self.take_button)
        self.show_story("""You drop the button. It rolls into the shadows.  
    A soft sigh escapes the painting, as if disappointed.""")
        self.create_buttons([
            ("Back away", self.leave_portrait),
            ("Check the cabinet again", self.check_cabinet),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Dropped the button")

    def keep_button(self):
        self.add_to_history(self.take_button)
        self.show_story("""You pocket the button. The skin on your hand tingles.  
    The portrait now smiles faintly whenever you look at it.""")
        self.create_buttons([
            ("Read the Journal", self.read_journal),
            ("Wind the Watch", self.wind_watch),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Kept the button")

    def close_journal(self):
        self.add_to_history(self.read_journal)
        self.show_story("""You shut the journal.  
    The room dims slightly, and you feel the presence of the portrait behind you again.""")
        self.create_buttons([
            ("Check the Cabinet", self.check_cabinet),
            ("Leave the Room", self.leave_room),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Closed the journal")

    def keep_journal(self):
        self.add_to_history(self.read_journal)
        self.show_story("""You keep the journal with you.  
    It hums slightly in your hands—something inside is awake.""")
        self.create_buttons([
            ("Check the portrait again", self.compare_to_portrait),
            ("Go upstairs", self.go_upstairs),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Kept the journal")

    def go_upstairs(self):
        self.add_to_history(self.wind_watch)
        self.show_story("""You follow the sound of reversed footsteps upstairs.  
    At the end of the hallway is a door slightly ajar. A faint light pulses from within.""")
        self.create_buttons([
            ("Enter the room", self.closed_room),
            ("Turn back", self.hollow_portrait_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Went upstairs")

    def stop_watch(self):
        self.add_to_history(self.wind_watch)
        self.show_story("""You try to stop the watch. It resists your touch, vibrating slightly, but then freezes.  
    Silence falls over the house. The portrait's eyes are now open again.""")
        self.create_buttons([
            ("Check the portrait", self.compare_to_portrait),
            ("Leave the Room", self.leave_room),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Stopped the watch")

    def leave_room(self):
        self.add_to_history(self.wind_watch)
        self.show_story("""You leave the room. Behind you, something clicks—like a lock sliding into place.""")
        self.create_buttons([
            ("Explore the hallway", self.follow_hallway),
            ("Try another object", self.check_cabinet),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the room")

    def cover_portrait(self):
        self.add_to_history(self.compare_to_portrait)
        self.show_story("""You throw a cloth over the portrait.  
    You hear a quiet hiss, and the light in the room flickers. Something doesn't like being hidden.""")
        self.create_buttons([
            ("Check the Journal", self.read_journal),
            ("Remove the cloth", self.compare_to_portrait),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Covered the portrait")

    def call_out(self):
        self.add_to_history(self.turn_around_noise)
        self.show_story("""You call out into the empty house.  
    Your own voice echoes back... but it doesn't sound quite like you.""")
        self.create_buttons([
            ("Follow the voice", self.follow_hallway),
            ("Stay silent", self.freeze_in_place),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Called out")

    def closed_room(self):
        self.add_to_history(self.follow_hallway)
        self.show_story("""You enter the room. It's an artist’s studio. On the easel: a half-finished portrait of you.  
    A note on the table: "All that’s left is the eyes."  
    The brush in the jar is wet.""")
        self.create_buttons([
            ("Complete the portrait", self.complete_portrait),
            ("Destroy the canvas", self.destroy_canvas),
            ("Back away", self.freeze_in_place),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered the closed room")

    def complete_portrait(self):
        self.add_to_history(self.closed_room)
        self.show_story("""You pick up the brush. As you paint the eyes, your vision blurs.  
    You feel yourself being watched—from inside.  
    When you blink, you're standing in the painting, watching your body leave the studio.""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.hollow_portrait_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("ENDING: Traded Places")

    def destroy_canvas(self):
        self.add_to_history(self.closed_room)
        self.show_story("""You tear through the canvas.  
    A horrible screech echoes in the house.  
    The portrait reappears in the hall, cracked and bleeding black paint.  
    But you're still... you. For now.""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.hollow_portrait_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("ENDING: Broken Loop")

    def freeze_in_place(self):
        self.add_to_history(self.follow_hallway)
        self.show_story("""You freeze. Everything goes still.  
    The draft stops. Your breath fogs the air—then stops too.  
    You’re stuck, unmoving, as if time itself forgot you.""")
        self.create_buttons([
            ("See choices", self.show_choices_report),
            ("Play again", self.hollow_portrait_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("ENDING: Forgotten by Time")
        
    def mountain_retreat(self):
        self.add_to_history(self.laid_back_stories)
        
        self.show_story(
            f"{self.player_name}, you’ve decided to spend a weekend at a cozy mountain retreat.\n"
            "The air is crisp, the pines are fragrant, and the view of the valley is breathtaking.\n"
            "As you settle into your cabin, you notice three activities calling your name. Which do you choose?"
        )
        self.create_buttons([
            ("Hike the nearby trail", self.hiking_trail),
            ("Visit the local village", self.village_visit),
            ("Relax by the cabin’s fireplace", self.fireplace_relax),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the mountain retreat adventure.")

    def hiking_trail(self):
        self.add_to_history(self.mountain_retreat)
        self.show_story(
            f"{self.player_name}, you lace up your boots and head out on the hiking trail.\n"
            "The path winds through towering pines, and you hear a distant waterfall.\n"
            "Soon, you reach a fork in the trail. One path leads to the waterfall, another to a scenic lookout.\n"
            "Which path do you take?"
        )
        self.create_buttons([
            ("Head to the waterfall", self.waterfall_path),
            ("Go to the lookout", self.lookout_path),
            ("Turn back to the cabin", self.return_to_cabin),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to hike the trail.")

    def village_visit(self):
        self.add_to_history(self.mountain_retreat)
        self.show_story(
            f"{self.player_name}, you drive down to the quaint mountain village.\n"
            "The streets are lined with charming shops and a bustling weekend market.\n"
            "You could browse the market stalls, visit a cozy café, or chat with a local artisan.\n"
            "What do you do?"
        )
        self.create_buttons([
            ("Browse the market", self.market_browse),
            ("Visit the café", self.cafe_visit),
            ("Talk to the artisan", self.artisan_chat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to visit the village.")

    def fireplace_relax(self):
        self.add_to_history(self.mountain_retreat)
        self.show_story(
            f"{self.player_name}, you decide to stay in and relax by the crackling fireplace.\n"
            "The cabin is cozy, with a stack of books and a journal on the table.\n"
            "Do you read a book, write in the journal, or take a nap?"
        )
        self.create_buttons([
            ("Read a book", self.read_book),
            ("Write in the journal", self.write_journal),
            ("Take a nap", self.take_nap),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to relax by the fireplace.")

    def waterfall_path(self):
        self.add_to_history(self.hiking_trail)
        self.show_story(
            f"{self.player_name}, you follow the sound of rushing water to a stunning waterfall.\n"
            "Mist rises from the base, and you notice a small cave behind the falls.\n"
            "A hiker nearby warns it might be slippery but says the cave holds a hidden gem.\n"
            "What do you do?"
        )
        self.create_buttons([
            ("Explore the cave", self.cave_exploration),
            ("Stay by the waterfall", self.stay_by_waterfall),
            ("Return to the trail", self.return_to_trail),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the waterfall path.")

    def lookout_path(self):
        self.add_to_history(self.hiking_trail)
        self.show_story(
            f"{self.player_name}, you climb to the scenic lookout and are rewarded with a panoramic view.\n"
            "A friendly park ranger offers to share their telescope to spot distant wildlife.\n"
            "Alternatively, you notice a sketchbook left by another hiker, tempting you to draw the view.\n"
            "What do you do?"
        )
        self.create_buttons([
            ("Use the telescope", self.use_telescope),
            ("Sketch the view", self.sketch_view),
            ("Head back down", self.return_to_trail),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the lookout path.")

    def return_to_cabin(self):
        self.add_to_history(self.hiking_trail)
        self.show_story(
            "You decide to head back to the cabin, enjoying the peaceful walk.\n"
            "The trail is quiet, and you feel relaxed but wonder what you missed at the waterfall or lookout.\n"
            "You return to the cabin and make a warm cup of tea."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Returned to the cabin from the trail.")

    def market_browse(self):
        self.add_to_history(self.village_visit)
        self.show_story(
            f"{self.player_name}, you wander through the vibrant market, filled with handmade goods.\n"
            "A vendor offers you a taste of local honey, while another shows you a unique wooden carving.\n"
            "Do you try the honey or buy the carving?"
        )
        self.create_buttons([
            ("Try the honey", self.try_honey),
            ("Buy the carving", self.buy_carving),
            ("Keep browsing", self.continue_browsing),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to browse the market.")

    def cafe_visit(self):
        self.add_to_history(self.village_visit)
        self.show_story(
            f"{self.player_name}, you step into the cozy café, greeted by the smell of fresh coffee.\n"
            "A barista suggests a special mountain blend or a homemade pastry.\n"
            "You also notice a poetry reading starting in the corner. What do you do?"
        )
        self.create_buttons([
            ("Order the coffee", self.order_coffee),
            ("Try the pastry", self.try_pastry),
            ("Join the poetry reading", self.poetry_reading),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to visit the café.")

    def artisan_chat(self):
        self.add_to_history(self.village_visit)
        self.show_story(
            f"{self.player_name}, you strike up a conversation with a local artisan weaving baskets.\n"
            "They offer to teach you a quick weaving technique or tell you about a hidden hot spring nearby.\n"
            "What do you choose?"
        )
        self.create_buttons([
            ("Learn to weave", self.learn_weaving),
            ("Hear about the hot spring", self.hot_spring_info),
            ("Return to the cabin", self.return_from_village),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to chat with the artisan.")

    def read_book(self):
        self.add_to_history(self.fireplace_relax)
        self.show_story(
            "You pick up a mystery novel from the cabin’s shelf and get lost in its pages.\n"
            "The story is gripping, and you spend hours by the fire, fully immersed.\n"
            "You feel relaxed but wonder if you missed out on exploring the mountains."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Read a book by the fireplace.")

    def write_journal(self):
        self.add_to_history(self.fireplace_relax)
        self.show_story(
            f"{self.player_name}, you write about your mountain retreat in the journal.\n"
            "The act of writing helps you reflect on your life and dreams.\n"
            "You feel inspired and decide to share your thoughts with a friend later."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Wrote in the journal.")

    def take_nap(self):
        self.add_to_history(self.fireplace_relax)
        self.show_story(
            "You curl up by the fireplace and take a peaceful nap.\n"
            "The crackling fire lulls you to sleep, and you wake up refreshed.\n"
            "It’s a calm day, but you wonder what adventures you might have missed."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took a nap by the fireplace.")

    def cave_exploration(self):
        self.add_to_history(self.waterfall_path)
        self.show_story(
            f"{self.player_name}, you carefully navigate the slippery rocks to enter the cave.\n"
            "Inside, you find an old journal with sketches of the mountain’s history.\n"
            "Do you keep the journal to read later or leave it for others to find?"
        )
        self.create_buttons([
            ("Keep the journal", self.keep_journal),
            ("Leave the journal", self.leave_journal),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Explored the cave behind the waterfall.")

    def stay_by_waterfall(self):
        self.add_to_history(self.waterfall_path)
        self.show_story(
            "You sit by the waterfall, letting the mist cool your face.\n"
            "It’s serene, and you feel at peace, but you wonder about the cave’s secrets.\n"
            "You head back to the cabin, content with the moment."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Stayed by the waterfall.")

    def return_to_trail(self):
        self.add_to_history(self.waterfall_path)
        self.show_story(
            "You decide to return to the main trail, enjoying the quiet forest.\n"
            "The hike is refreshing, but you feel you might have missed something special.\n"
            "You make it back to the cabin and relax for the evening."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Returned to the trail.")

    def use_telescope(self):
        self.add_to_history(self.lookout_path)
        self.show_story(
            "You use the ranger’s telescope and spot a family of deer in the valley.\n"
            "The ranger shares stories about the local wildlife, and you feel connected to nature.\n"
            "They invite you to a stargazing event tonight. Do you go?"
        )
        self.create_buttons([
            ("Attend stargazing", self.stargazing_event),
            ("Decline and return", self.decline_stargazing),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Used the telescope at the lookout.")

    def sketch_view(self):
        self.add_to_history(self.lookout_path)
        self.show_story(
            f"{self.player_name}, you sketch the stunning mountain view in the sketchbook.\n"
            "A passing hiker admires your work and suggests you show it at the village art fair.\n"
            "Your sketch wins a small prize, and you feel proud of your creativity!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Sketched the view at the lookout.")

    def try_honey(self):
        self.add_to_history(self.market_browse)
        self.show_story(
            "The local honey is sweet and floral, and the vendor shares its history.\n"
            "You buy a jar and feel inspired to try beekeeping someday.\n"
            "The market visit leaves you happy and buzzing with ideas!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Tried the local honey.")

    def buy_carving(self):
        self.add_to_history(self.market_browse)
        self.show_story(
            "You buy the wooden carving, a beautifully crafted mountain scene.\n"
            "The vendor tells you it’s made by a local elder with a rich story.\n"
            "You feel a connection to the village’s culture and treasure your new keepsake."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Bought the wooden carving.")

    def continue_browsing(self):
        self.add_to_history(self.market_browse)
        self.show_story(
            "You keep browsing the market, enjoying the sights and sounds.\n"
            "It’s a pleasant experience, but nothing particularly memorable happens.\n"
            "You return to the cabin, satisfied with your village visit."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Continued browsing the market.")

    def order_coffee(self):
        self.add_to_history(self.cafe_visit)
        self.show_story(
            "The mountain blend coffee is rich and aromatic, warming you up.\n"
            "You chat with the barista, who shares stories about the village’s history.\n"
            "You leave the café feeling energized and connected to the community."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Ordered the coffee.")

    def try_pastry(self):
        self.add_to_history(self.cafe_visit)
        self.show_story(
            "The homemade pastry is flaky and delicious, a perfect treat.\n"
            "You savor it slowly, enjoying the cozy café atmosphere.\n"
            "It’s a simple pleasure, but you wonder about the poetry reading."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Tried the pastry.")

    def poetry_reading(self):
        self.add_to_history(self.cafe_visit)
        self.show_story(
            f"{self.player_name}, you join the poetry reading and are moved by the heartfelt verses.\n"
            "You share a short poem of your own, and the group applauds warmly.\n"
            "You leave the café feeling inspired and part of something special."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Joined the poetry reading.")

    def learn_weaving(self):
        self.add_to_history(self.artisan_chat)
        self.show_story(
            "The artisan teaches you the basics of basket weaving, and you create a small basket.\n"
            "They praise your quick learning and gift you the materials to keep practicing.\n"
            "You return to the cabin with a new skill and a sense of accomplishment!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Learned to weave a basket.")

    def hot_spring_info(self):
        self.add_to_history(self.artisan_chat)
        self.show_story(
            "The artisan shares directions to a hidden hot spring in the mountains.\n"
            "You hike there and soak in the warm, soothing waters under the stars.\n"
            "It’s a magical experience that makes your retreat unforgettable!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Learned about the hot spring.")

    def return_from_village(self):
        self.add_to_history(self.artisan_chat)
        self.show_story(
            "You thank the artisan and head back to the cabin.\n"
            "The village was charming, but you feel you might have missed a unique opportunity.\n"
            "You settle in for a quiet evening by the fire."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Returned to the cabin from the village.")

    def keep_journal(self):
        self.add_to_history(self.cave_exploration)
        self.show_story(
            f"{self.player_name}, you take the journal back to the cabin and read it by the fire.\n"
            "It’s filled with fascinating stories about the mountain’s past explorers.\n"
            "You feel like you’ve uncovered a piece of history and cherish the find."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Kept the journal from the cave.")

    def leave_journal(self):
        self.add_to_history(self.cave_exploration)
        self.show_story(
            "You leave the journal in the cave for others to discover.\n"
            "You feel good about preserving the mystery, but wonder what stories it held.\n"
            "You return to the cabin, content with your hike."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the journal in the cave.")

    def stargazing_event(self):
        self.add_to_history(self.use_telescope)
        self.show_story(
            "You join the stargazing event and marvel at constellations through the ranger’s telescope.\n"
            "The group shares stories around a campfire, and you feel a deep connection to the universe.\n"
            "This night becomes a highlight of your retreat!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Attended the stargazing event.")

    def decline_stargazing(self):
        self.add_to_history(self.use_telescope)
        self.show_story(
            "You politely decline the stargazing invitation and head back to the cabin.\n"
            "You enjoy a quiet evening, but later hear the event was spectacular.\n"
            "You feel rested but wonder about the night sky you missed."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.mountain_retreat),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Declined the stargazing event.")
        
    def library_visit(self):
        self.add_to_history(self.laid_back_stories)
        
        self.show_story(
            f"{self.player_name}, it's a quiet afternoon, and you decide to visit the local library.\n"
            "The scent of old books fills the air, and soft sunlight streams through the windows.\n"
            "As you wander the aisles, you notice three intriguing options. Which will you choose?"
        )
        self.create_buttons([
            ("Browse the mystery section", self.mystery_section),
            ("Join a book club meeting", self.book_club),
            ("Explore the rare books room", self.rare_books),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the library visit adventure.")

    def mystery_section(self):
        self.add_to_history(self.library_visit)
        self.show_story(
            f"{self.player_name}, you head to the mystery section, where shelves are packed with thrilling novels.\n"
            "You find an old, dusty book with a note tucked inside that says, 'Solve the riddle to find the hidden treasure.'\n"
            "Do you try to solve the riddle or keep browsing?"
        )
        self.create_buttons([
            ("Solve the riddle", self.solve_riddle),
            ("Keep browsing", self.keep_browsing),
            ("Ask the librarian about the book", self.ask_librarian),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to browse the mystery section.")

    def book_club(self):
        self.add_to_history(self.library_visit)
        self.show_story(
            f"{self.player_name}, you join a lively book club meeting in the library’s cozy reading room.\n"
            "The group is discussing a classic novel, and they invite you to share your thoughts.\n"
            "You haven’t read the book, but you could wing it or listen quietly. What do you do?"
        )
        self.create_buttons([
            ("Share your thoughts", self.share_thoughts),
            ("Listen quietly", self.listen_quietly),
            ("Ask about the book", self.ask_book_club),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to join the book club.")

    def rare_books(self):
        self.add_to_history(self.library_visit)
        self.show_story(
            f"{self.player_name}, you enter the rare books room, where ancient tomes are displayed under soft lighting.\n"
            "A librarian offers to show you a special manuscript or let you explore on your own.\n"
            "You also notice a locked display case with a curious artifact. What do you do?"
        )
        self.create_buttons([
            ("See the manuscript", self.see_manuscript),
            ("Explore on your own", self.explore_rare_books),
            ("Inquire about the artifact", self.inquire_artifact),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose to explore the rare books room.")

    def solve_riddle(self):
        self.add_to_history(self.mystery_section)
        self.show_story(
            "You puzzle over the riddle: 'I’m hidden where knowledge sleeps, behind a cover of crimson.'\n"
            "You find a crimson-covered book on a high shelf. Inside is a map to a hidden library nook!\n"
            "Do you follow the map or share it with the librarian?"
        )
        self.create_buttons([
            ("Follow the map", self.follow_map),
            ("Share with librarian", self.share_with_librarian),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Tried to solve the riddle.")

    def keep_browsing(self):
        self.add_to_history(self.mystery_section)
        self.show_story(
            "You decide to keep browsing the mystery section, picking up a few intriguing novels.\n"
            "You spend a pleasant hour reading summaries but feel like you missed an adventure with the riddle.\n"
            "You leave with some good books but a lingering curiosity."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Kept browsing the mystery section.")

    def ask_librarian(self):
        self.add_to_history(self.mystery_section)
        self.show_story(
            "You ask the librarian about the mysterious book and the note inside.\n"
            "She smiles and reveals it’s part of a library scavenger hunt for fun.\n"
            "She invites you to join the hunt officially. Do you accept?"
        )
        self.create_buttons([
            ("Join the scavenger hunt", self.scavenger_hunt),
            ("Decline politely", self.decline_hunt),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Asked the librarian about the book.")

    def share_thoughts(self):
        self.add_to_history(self.book_club)
        self.show_story(
            f"{self.player_name}, you share some creative thoughts, improvising based on the discussion.\n"
            "The group loves your enthusiasm and invites you to join their next meeting.\n"
            "You make new friends and feel inspired to read the book for real!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Shared thoughts in the book club.")

    def listen_quietly(self):
        self.add_to_history(self.book_club)
        self.show_story(
            "You listen quietly to the book club’s discussion, enjoying their insights.\n"
            "The group appreciates your presence but doesn’t engage you much.\n"
            "You leave feeling relaxed but wish you’d contributed to the conversation."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Listened quietly in the book club.")

    def ask_book_club(self):
        self.add_to_history(self.book_club)
        self.show_story(
            "You ask the book club about the novel, and they eagerly explain its themes and plot.\n"
            "Their passion inspires you, and they lend you a copy to read at home.\n"
            "You leave excited to dive into the story and join them next time!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Asked the book club about the novel.")

    def see_manuscript(self):
        self.add_to_history(self.rare_books)
        self.show_story(
            "The librarian shows you a beautifully illustrated manuscript from the 18th century.\n"
            "You’re captivated by its history and ask if you can volunteer to help preserve such treasures.\n"
            "Do you volunteer or thank her and move on?"
        )
        self.create_buttons([
            ("Volunteer to help", self.volunteer_library),
            ("Thank her and move on", self.thank_librarian),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Viewed the rare manuscript.")

    def explore_rare_books(self):
        self.add_to_history(self.rare_books)
        self.show_story(
            "You explore the rare books room alone, marveling at the ancient texts.\n"
            "You find an old journal but can’t read its faded script.\n"
            "You enjoy the quiet experience but wonder if the librarian’s guidance would have added more."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Explored the rare books room alone.")

    def inquire_artifact(self):
        self.add_to_history(self.rare_books)
        self.show_story(
            "You ask about the artifact in the locked case, and the librarian explains it’s an ancient bookmark.\n"
            "She offers to let you examine it closely under supervision.\n"
            "Do you examine it or decide to explore elsewhere?"
        )
        self.create_buttons([
            ("Examine the artifact", self.examine_artifact),
            ("Explore elsewhere", self.explore_elsewhere),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Inquired about the artifact.")

    def follow_map(self):
        self.add_to_history(self.solve_riddle)
        self.show_story(
            "You follow the map to a hidden library nook filled with rare mystery novels.\n"
            "A note congratulates you on solving the riddle and offers you a free book!\n"
            "You leave with a treasure and a thrilling story to tell!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Followed the map to the hidden nook.")

    def share_with_librarian(self):
        self.add_to_history(self.solve_riddle)
        self.show_story(
            "You share the map with the librarian, who’s delighted by your find.\n"
            "She reveals it’s part of a library game and rewards you with a year’s free membership.\n"
            "You feel proud for your honesty and excited for more library visits!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Shared the map with the librarian.")

    def scavenger_hunt(self):
        self.add_to_history(self.ask_librarian)
        self.show_story(
            "You join the scavenger hunt, solving clues hidden in books across the library.\n"
            "You team up with other participants, and together you win the grand prize: a rare book set!\n"
            "You leave with new friends and a sense of accomplishment!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Joined the library scavenger hunt.")

    def decline_hunt(self):
        self.add_to_history(self.ask_librarian)
        self.show_story(
            "You politely decline the scavenger hunt and spend the rest of your time reading quietly.\n"
            "The library is peaceful, but you hear others laughing as they hunt for clues.\n"
            "You enjoy your day but wonder about the fun you missed."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Declined the scavenger hunt.")

    def volunteer_library(self):
        self.add_to_history(self.see_manuscript)
        self.show_story(
            "You volunteer to help preserve rare books, learning about restoration techniques.\n"
            "The library staff are grateful and invite you to a special exhibit opening.\n"
            "You feel honored to contribute to preserving history!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Volunteered to help with rare books.")

    def thank_librarian(self):
        self.add_to_history(self.see_manuscript)
        self.show_story(
            "You thank the librarian and continue exploring the library.\n"
            "You find some interesting books but don’t uncover anything extraordinary.\n"
            "You enjoy a calm day but wonder if volunteering would have been rewarding."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Thanked the librarian and moved on.")

    def examine_artifact(self):
        self.add_to_history(self.inquire_artifact)
        self.show_story(
            "You examine the ancient bookmark, which has intricate carvings.\n"
            "The librarian shares its history, linking it to a famous author from centuries ago.\n"
            "You’re invited to a lecture about the author, making your day unforgettable!"
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Examined the ancient bookmark.")

    def explore_elsewhere(self):
        self.add_to_history(self.inquire_artifact)
        self.show_story(
            "You decide to explore other parts of the library instead of examining the artifact.\n"
            "You find a cozy reading corner and enjoy a good book.\n"
            "It’s a relaxing day, but you wonder about the artifact’s story."
        )
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.library_visit),
            ("Pick another story", self.laid_back_stories),
            ("Stop", self.quit_game)
        ])
        
        self.choices.append("Explored elsewhere in the library.")
    def lighthouse_start(self):
        self.add_to_history(self.horror_stories)
        self.show_story(f"{self.player_name}, you've ventured to the old Whispering Lighthouse on a foggy night.\n"
                        "Legends say it’s haunted by a keeper’s spirit. The door creaks open. Where will you explore first?")
        self.create_buttons([
            ("Main Room", self.lighthouse_main_room),
            ("Spiral Staircase", self.lighthouse_staircase),
            ("Keeper’s Quarters", self.lighthouse_quarters),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Chose the Whispering Lighthouse Story")

    def lighthouse_main_room(self):
        self.add_to_history(self.lighthouse_start)
        self.show_story(f"{self.player_name}, the main room is dusty, with sea charts on the walls. You notice:\n"
                        "1. A glowing lantern\n"
                        "2. A weathered logbook\n"
                        "3. A tarnished brass telescope")
        self.create_buttons([
            ("Examine the lantern", self.lighthouse_lantern),
            ("Read the logbook", self.lighthouse_logbook),
            ("Look through the telescope", self.lighthouse_telescope),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered the main room")

    def lighthouse_lantern(self):
        self.add_to_history(self.lighthouse_main_room)
        self.show_story(f"{self.player_name}, the lantern pulses softly. A faint voice whispers:\n"
                        "'Find my light...' What will you do?")
        self.create_buttons([
            ("Touch the lantern", self.lighthouse_touch_lantern),
            ("Turn it off", self.lighthouse_turn_off),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Examined the lantern")

    def lighthouse_touch_lantern(self):
        self.add_to_history(self.lighthouse_lantern)
        self.show_story(f"{self.player_name}, touching the lantern shows you the keeper’s final night, guiding a ship to safety.\n"
                        "The fog lifts, and you leave at dawn, feeling the keeper’s gratitude.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Touched the lantern")

    def lighthouse_turn_off(self):
        self.add_to_history(self.lighthouse_lantern)
        self.show_story(f"{self.player_name}, you turn off the lantern. The room goes dark, but a soft glow leads you outside.\n"
                        "The lighthouse is silent now, and you leave as the fog clears.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Turned off the lantern")

    def lighthouse_logbook(self):
        self.add_to_history(self.lighthouse_main_room)
        self.show_story(f"{self.player_name}, the logbook’s final entry reads: 'The light must never fade.'\n"
                        "A hidden drawer pops open, revealing a silver locket. Will you take it?")
        self.create_buttons([
            ("Take the locket", self.lighthouse_take_locket),
            ("Leave it", self.lighthouse_leave_locket),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Read the logbook")

    def lighthouse_take_locket(self):
        self.add_to_history(self.lighthouse_logbook)
        self.show_story(f"{self.player_name}, the locket holds a photo of the keeper’s family. You feel a warm breeze.\n"
                        "The keeper’s spirit appears, thanks you, and guides you safely out at dawn.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Took the locket")

    def lighthouse_leave_locket(self):
        self.add_to_history(self.lighthouse_logbook)
        self.show_story(f"{self.player_name}, you leave the locket. The lighthouse hums softly, as if disappointed.\n"
                        "You exit at dawn, safe but wondering about the keeper’s story.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the locket")

    def lighthouse_telescope(self):
        self.add_to_history(self.lighthouse_main_room)
        self.show_story(f"{self.player_name}, through the telescope, you see a ghostly ship on the horizon.\n"
                        "A note beside it says: 'Signal them home.' What will you do?")
        self.create_buttons([
            ("Signal the ship", self.lighthouse_signal_ship),
            ("Ignore the note", self.lighthouse_ignore_note),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Looked through the telescope")

    def lighthouse_signal_ship(self):
        self.add_to_history(self.lighthouse_telescope)
        self.show_story(f"{self.player_name}, you flash the lighthouse beam. The ghostly ship fades with a sigh of relief.\n"
                        "The keeper’s spirit nods gratefully, and you leave safely at dawn.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Signaled the ship")

    def lighthouse_ignore_note(self):
        self.add_to_history(self.lighthouse_telescope)
        self.show_story(f"{self.player_name}, you step away from the telescope. The ship remains on the horizon.\n"
                        "You leave at dawn, feeling you missed a chance to help.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Ignored the note")

    def lighthouse_staircase(self):
        self.add_to_history(self.lighthouse_start)
        self.show_story(f"{self.player_name}, the spiral staircase creaks as you climb. At the top is the beacon room.\n"
                        "A dusty mirror reflects someone standing behind you… but you’re alone.")
        self.create_buttons([
            ("Look in the mirror", self.lighthouse_mirror),
            ("Ignore it", self.lighthouse_ignore_mirror),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Climbed the staircase")

    def lighthouse_mirror(self):
        self.add_to_history(self.lighthouse_staircase)
        self.show_story(f"{self.player_name}, the mirror shows the keeper’s face, smiling. He whispers:\n"
                        "'Thank you for coming.' He points to a safe exit, and you leave at dawn.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Looked in the mirror")

    def lighthouse_ignore_mirror(self):
        self.add_to_history(self.lighthouse_staircase)
        self.show_story(f"{self.player_name}, you avoid the mirror and head down. The lighthouse feels heavy with regret.\n"
                        "You leave at dawn, safe but unsettled.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Ignored the mirror")

    def lighthouse_quarters(self):
        self.add_to_history(self.lighthouse_start)
        self.show_story(f"{self.player_name}, the keeper’s quarters are cozy but cold. You find a music box on the desk.\n"
                        "It plays a haunting tune when you touch it.")
        self.create_buttons([
            ("Wind the music box", self.lighthouse_music_box),
            ("Leave it alone", self.lighthouse_leave_music_box),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Entered the keeper’s quarters")

    def lighthouse_music_box(self):
        self.add_to_history(self.lighthouse_quarters)
        self.show_story(f"{self.player_name}, the music box summons the keeper’s spirit. He shares his story of duty.\n"
                        "He opens a hidden door to safety, and you leave at dawn, enlightened.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Wound the music box")

    def lighthouse_leave_music_box(self):
        self.add_to_history(self.lighthouse_quarters)
        self.show_story(f"{self.player_name}, you leave the music box untouched. The room grows colder.\n"
                        "You hurry out at dawn, relieved but curious about the keeper’s tale.")
        self.create_buttons([
            ("Show choice report", self.show_choices_report),
            ("Play again", self.lighthouse_start),
            ("Pick another story", self.horror_stories),
            ("Stop", self.quit_game)
        ])
        self.choices.append("Left the music box")
    
    def game_over(self):
        """
        Handle the end of the game.
        """
        if messagebox.askyesno("Game Over", "Not the best Choice! Try again?"):
            self.title_screen()
        else:
            self.quit_game()
    

    def create_buttons(self, choices):
        """Create smaller buttons for the player's choices with white, thicker style"""
        # Clear existing buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Create new buttons
        for text, command in choices:
            button = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                width=50,  # Reduced width
                height=2,  # Height for thicker appearance
                fg="#1e1e1e",  # Fixed typo from #1ec1d6s
                bg="#FFFFFF",  # White background
                font=self.button_font,
                relief="raised",  # Raised for thicker, 3D look
                bd=3,  # Border width for thickness
                padx=10,
                pady=5
            )
            button.pack(pady=4, ipadx=5, ipady=2)

            # Hover effect
            button.bind("<Enter>", lambda e, b=button: b.config(fg="blue"))
            button.bind("<Leave>", lambda e, b=button: b.config(fg="#1e1e1e"))

        # Update the display
        self.button_frame.update_idletasks()

    # [All story methods unchanged: title_screen, adventure_stories, horror_stories, etc.]

    def show_story(self, text):
        """
        Update the story text on the screen.
        """
        self.story_text.config(text=text)

    def handle_qa(self):
        """
        Handle the player's question in the Q&A feature.
        """
        question = self.qa_entry.get().strip().lower()
        self.qa_entry.delete(0, tk.END)  # Clear the entry box

        # Input validation for Q&A
        if not question:
            messagebox.showwarning("Invalid Input", "Please enter a question.")
            return

        if "what should i do" in question:
            self.show_story(f"{self.player_name}, The buttons that you see below are options for you to progress in the story, carefully read the options \nto progress, or pick another story that you want to play!")
        elif "help" in question:
            self.show_story(f"{self.player_name}, The buttons that you see below are options for you to progress in the story, carefully read the options \nto progress, or pick another story that you want to play!")
        else:
            self.show_story(f"{self.player_name}, I'm not sure how to answer that. Try asking something like 'What should I do?'")

    def add_to_history(self, screen):
        """Add the current screen to the history for navigation."""
        self.history.append(screen)

    def go_back(self):
        """Navigate to the previous screen in the history."""
        if self.history:
            previous_screen = self.history.pop()
            previous_screen()

    def quit_game(self):
        """
        Quit the game.
        """
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()

    def show_choices_report(self):
        """
        Display a report of the player's choices.
        """
        report_window = tk.Toplevel(self.root)
        report_window.title("Choices Report")
        report_window.geometry("600x400")
        report_window.configure(bg="#1e1e1e")

        report_label = tk.Label(report_window, text="Your Choices:", font=self.title_font, fg="#b3b3b3", bg="#1e1e1e")
        report_label.pack(pady=20)

        report_text = tk.Text(report_window, wrap=tk.WORD, font=self.story_font, fg="#b3b3b3", bg="#1e1e1e", bd=0)
        report_text.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        for i, choice in enumerate(self.choices, 1):
            report_text.insert(tk.END, f"{i}. {choice}\n")

        report_text.config(state=tk.DISABLED)  # Make the text read-only

        close_button = tk.Button(report_window, text="Close", font=self.button_font, bg="#FFFFFF", fg="#1e1e1e", relief="raised", bd=3, command=report_window.destroy)
        close_button.pack(pady=20)


# Run the Tkinter application
root = tk.Tk()
game = PickYourJourney(root)
root.mainloop()