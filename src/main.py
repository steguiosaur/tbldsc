from tkinter import Tk, PhotoImage
from PIL import Image
from customtkinter import (
    CTkImage,
    CTkLabel,
    CTkButton,
    CTkFrame,
    CTkOptionMenu,
    CTkTextbox,
    CTkCheckBox,
    set_appearance_mode,
    set_default_color_theme,
    set_widget_scaling,
)
from utils.pathing import Pathing


class Main(Tk):
    def __init__(self):
        super().__init__()

        self.configure(bg="#222222")

        self.grid_rowconfigure((0, 5), weight=1)
        self.grid_columnconfigure((0, 2), weight=1)

        # show an image or textbox depending on filetype selected as input
        self.frame_input = CTkFrame(master=self, fg_color="#2e2e2e")
        self.frame_input.grid(
            row=0, column=0, rowspan=6, columnspan=3, padx=20, pady=20, sticky="nsew"
        )

        # show output and error messages
        self.textbox_output = CTkTextbox(
            master=self, height=100, fg_color="#2e2e2e", state="disabled"
        )
        self.textbox_output.grid(
            row=6, column=0, columnspan=3, padx=20, pady=(0, 20), sticky="nsew"
        )

        # logo image
        self.image_logo = CTkImage(
            light_image=Image.open(Pathing.asset_path("tbldsc_black.png")),
            dark_image=Image.open(Pathing.asset_path("tbldsc_white.png")),
            size=(138, 38),
        )
        self.label_logo = CTkLabel(self, text="", image=self.image_logo)
        self.label_logo.grid(row=0, column=4, padx=(0, 20), pady=20, sticky="n")

        # model selector
        self.option_model = CTkOptionMenu(self, values=["model1", "model2"])
        self.option_model.grid(row=1, column=4, padx=(0, 20), pady=20, sticky="")

        # reset button
        self.button_reset = CTkButton(self, text="Reset", command=self.button_callback)
        self.button_reset.grid(row=2, column=4, padx=(0, 20), pady=20, sticky="")

        # import table button
        self.check_import = CTkCheckBox(
            self, text="Import table", command=self.button_callback
        )
        self.check_import.grid(row=3, column=4, padx=(0, 20), pady=(20, 10), sticky="")

        # textual editor table button
        self.check_editor = CTkCheckBox(
            self, height=10, text="Table editor", command=self.button_callback
        )
        self.check_editor.grid(row=4, column=4, padx=(0, 20), pady=(10, 20), sticky="")

        # go button
        self.button_start = CTkButton(
            master=self, text="GO", command=self.button_callback
        )
        self.button_start.grid(
            row=6, column=4, padx=(0, 20), pady=(0, 20), sticky="nsew"
        )

    def show_splash_screen(self):
        self.splash_frame = CTkFrame(master=self, fg_color="#222222")
        self.splash_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.splash_image = CTkImage(
            light_image=Image.open(Pathing.asset_path("tbldsc_black.png")),
            dark_image=Image.open(Pathing.asset_path("tbldsc_white.png")),
            size=(276, 76),
        )
        self.splash_label = CTkLabel(
            self.splash_frame, text="", image=self.splash_image
        )
        self.splash_label.pack(expand=True)

        self.splash_frame.bind("<Button-1>", self.hide_splash_screen)
        self.splash_frame.focus_set()

    def hide_splash_screen(self, event=None):
        self.splash_frame.destroy()

    def button_callback(self):
        print("button clicked")


set_appearance_mode("Dark")
set_default_color_theme("blue")
set_widget_scaling(1)

app = Main()
app.withdraw()
app.title("tbldsc")
app.resizable(True, True)
width = 1024
height = 576
app.deiconify()
x = (app.winfo_screenwidth() // 2) - width // 2
y = (app.winfo_screenheight() // 2) - height // 2
app.geometry("%dx%d+%d+%d" % (width, height, x, y))
app.minsize(1024, 576)
app.iconphoto(True, PhotoImage(file=Pathing.asset_path("tbldsc_white_logo.png")))
app.show_splash_screen()
app.mainloop()
