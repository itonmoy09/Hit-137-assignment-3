import tkinter as tk
from tkinter import messagebox

# Base class for videos demonstrating polymorphism
class Video:
    def play(self):
        pass  # Placeholder method to be overridden

# Subclass representing a tutorial video, overriding the play method
class Tutorial(Video):
    def play(self):
        print("Playing tutorial video...")  # Overriding play method from Video class

# Subclass representing a movie, overriding the play method
class Movie(Video):
    def play(self):
        print("Playing movie...")  # Overriding play method from Video class

# Class for logging messages
class Logger:
    def log(self, message):
        print(f"LOG: {message}")

# Class to manage liked videos, using multiple inheritance to inherit Logger
class LikedVideos(Logger):
    def __init__(self):
        self.liked_videos = []

    def add_liked_video(self, video_title):
        self.liked_videos.append(video_title)
        self.log(f"Added {video_title} to liked videos.")  # Using log method from Logger class

# User class demonstrating encapsulation with private attributes
class User:
    def __init__(self, username):
        self.__username = username  # private variable

    def get_username(self):
        return self.__username  # Public method to access private variable

# Main application class inheriting from Tkinter's Tk and LikedVideos
class YouTubeApp(tk.Tk, LikedVideos):  # Multiple inheritance
    def __init__(self):
        super().__init__()  # Initializing Tk class
        LikedVideos.__init__(self)  # Explicitly call LikedVideos' initializer
        self.title("YouTube Like Interface")
        self.geometry("400x300")

        # Button creation using a decorator
        @self.button_decorator
        def create_buttons():
            tk.Button(self, text="Play Tutorial", command=self.play_tutorial).pack(pady=10)
            tk.Button(self, text="Play Movie", command=self.play_movie).pack(pady=10)
            tk.Button(self, text="Like Video", command=self.like_video).pack(pady=10)

        create_buttons()

        # Display logged-in user using encapsulation
        self.__user = User("JohnDoe")
        tk.Label(self, text=f"Logged in as: {self.__user.get_username()}").pack(pady=10)

    # Decorator to add extra functionality when creating buttons
    def button_decorator(self, func):
        def wrapper():
            print("Creating buttons...")  # Additional logic before button creation
            func()
            print("Buttons created.")  # Additional logic after button creation
        return wrapper

    # Method to play tutorial video, demonstrating method overriding
    def play_tutorial(self):
        tutorial = Tutorial()
        self.play_video(tutorial)  # Polymorphic behavior

    # Method to play movie, demonstrating method overriding
    def play_movie(self):
        movie = Movie()
        self.play_video(movie)  # Polymorphic behavior

    # Method demonstrating polymorphism: can accept any subclass of Video
    def play_video(self, video):
        video.play()  # Calls overridden play method of passed video object
        messagebox.showinfo("Playing Video", f"{video.__class__.__name__} is now playing!")

    # Method overriding: change the base class method to include a message box
    def add_liked_video(self, video_title):
        super().add_liked_video(video_title)  # Calling the method from the parent class
        messagebox.showinfo("Liked Video", f"{video_title} added to your liked videos!")

    # Method to handle liking a video
    def like_video(self):
        self.add_liked_video("Sample Video")

if __name__ == "__main__":
    app = YouTubeApp()
    app.mainloop()
 #https://github.com/Mohammad-karazi/HIT137-project-.git