import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

class PrisonEscapeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Grand Prison Escape")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e1e")

        self.title_font = tkFont.Font(family="Helvetica", size=40, weight="bold")
        self.story_font = tkFont.Font(family="Helvetica", size=24)
        self.button_font = tkFont.Font(family="Helvetica", size=20, weight="bold")

        # Title
        self.title_label = tk.Label(root, text="Grand Prison Escape", font=self.title_font, fg="#b3b3b3", bg="#1e1e1e")
        self.title_label.pack(pady=30)

        # Story text
        self.story_text = tk.Label(root, text="", wraplength=1000, justify="center", font=self.story_font, fg="#b3b3b3", bg="#1e1e1e")
        self.story_text.pack(pady=40)

        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.pack()

        self.start_game()

    def start_game(self):
        self.show_story("Hello, prisoner. You have been put in this high-security prison for a crime you did not commit.\n"
                        "Oh, and if you get caught escaping, you’ll be sent to an isolated island. Good luck.")

        self.create_buttons([
            ("Wake up and look around", self.first_choice)
        ])

    def first_choice(self):
        self.show_story("You wake up after being knocked out. Three guards are standing on the other side of the bars.\n"
                        "What will you do?")
        self.create_buttons([
            ("Try to steal the keys", self.try_to_steal_keys),
            ("Try to fight the guards", self.try_to_fight),
            ("Wait and sit there", self.wait),
            ("End Game", self.quit_game)
        ])

    def try_to_steal_keys(self):
        self.show_story("You reach for the keys, but a guard notices and shoves you back into the corner.\n"
                        "You decide to wait for the shift change.")
        self.root.after(4000, self.guard_shift_change)

    def try_to_fight(self):
        self.show_story("You try to punch the leftmost guard but realize you are too weak.\n"
                        "The guard shoves you back into the corner. You wait for the shift change.")
        self.root.after(4000, self.guard_shift_change)

    def wait(self):
        self.show_story("You decide to sit and wait. The guards eventually change shifts, leaving only one sleepy guard.")
        self.root.after(4000, self.guard_shift_change)

    def guard_shift_change(self):
        self.show_story("After three hours, two guards leave for their shift change, leaving a sleepy guard standing watch.\n"
                        "Now is your chance to escape!")
        self.create_buttons([
            ("Try to steal the keys from the sleepy guard", self.steal_keys_success),
            ("Just sit and wait", self.excess_laziness),
            ("End Game", self.quit_game)
        ])

    def steal_keys_success(self):
        self.show_story("You carefully take the keys from the sleepy guard and unlock your cell. You are free!\n"
                        "What will you do next?")
        self.create_buttons([
            ("Hide behind a supply cart", self.sneak_around),
            ("Run for the exit", self.run_for_exit),
            ("End Game", self.quit_game)
        ])

    def sneak_around(self):
        self.show_story("You hide behind a supply cart as two guards walk past. You see a vent and a staircase leading to the exit.")
        self.create_buttons([
            ("Climb into the vent", self.vent_escape),
            ("Take the stairs", self.staircase_escape),
            ("End Game", self.quit_game)
        ])

    def run_for_exit(self):
        self.show_story("You try to run for the exit, but the noise alerts the guards. You are caught and sent to the isolated island.")
        self.game_over()

    def vent_escape(self):
        self.show_story("You crawl through the vent and reach the laundry room where prisoner uniforms are stored.")
        self.create_buttons([
            ("Steal a guard uniform", self.disguise_escape),
            ("Try to sneak past the workers", self.get_caught),
            ("End Game", self.quit_game)
        ])

    def disguise_escape(self):
        self.show_story("You put on a guard uniform and walk confidently through the prison, blending in.\n"
                        "You reach the main entrance and step outside into the cold night air. You've escaped!\n"
                        "Congratulations, you have successfully escaped the prison!")
        self.create_buttons([
            ("Play Again", self.start_game),
            ("Quit", self.quit_game)
        ])

    def staircase_escape(self):
        self.show_story("You take the stairs, but a guard spots you and sounds the alarm. You are captured and sent to the isolated island.")
        self.root.after(4000, self.game_over)

    def get_caught(self):
        self.show_story("You hesitate too long, and the guards eventually catch you. You are sent to the isolated island.")
        self.root.after(4000, self.game_over)

    def excess_laziness(self):
        self.show_story("Your will to be lazy has cost you. You decide to remain rotting in your cell for the rest of your life.")
        self.root.after(4000, self.game_over)

    def game_over(self):
        if messagebox.askyesno("Game Over", "You got caught! Try again?"):
            self.start_game()
        else:
            self.quit_game()

    def show_story(self, text):
        self.story_text.config(text=text)

    def create_buttons(self, choices):
        # Clear existing buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Create new buttons
        for text, command in choices:
            button = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                width=50,
                bg="#4CAF50",
                fg="#1e1e1e",
                font=self.button_font,
                relief="flat",
                bd=0,
                padx=20,
                pady=10
            )
            button.pack(pady=15, padx=20, ipady=10)

            # Hover effect - changing background color
            button.bind("<Enter>", lambda e, b=button: b.config(bg="#45a049", fg="blue")) #Hover
            button.bind("<Leave>", lambda e, b=button: b.config(bg="#4CAF50", fg="#1e1e1e")) #Reset

    def quit_game(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()

# Run the Tkinter application
root = tk.Tk()
game = PrisonEscapeGame(root)
root.mainloop()
