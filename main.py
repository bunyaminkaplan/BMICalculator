from tkinter import *
window = Tk()
window.title("bmi calculator")
window.minsize(width=200 , height=60)

mass_label = Label(text= "enter your mass please")
mass_label.pack()

mass_entry = Entry()
mass_entry.pack()

height_label = Label(text= "enter your height please")
height_label.pack()

height_entry = Entry()
height_entry.pack()

final_label = Label(text= "...")
final_label.pack()

def calculate_selected():

	type_of_input = type(height_entry.get())
	print(type_of_input)

	try:
		float_input_height = float(height_entry.get())
		float_input_mass = float(mass_entry.get())
	except:
		final_label.config(text="please use numbers")
		print("please use numbers")

	if len(height_entry.get()) == 0  or len(mass_entry.get()) == 0:

		print("error")
	else:
		height = float(height_entry.get()) / 100
		calculated_height = height*height
		mass = float(mass_entry.get())
		final = mass / calculated_height

		if final <= 18.4:
			final_label.config(text="you are underweight")

		elif final >= 18.5 and final <= 24.9:
			final_label.config(text="you good")

		elif final >= 25.0 and final <= 39.9:
			final_label.config(text="you are overweight")

		elif final >= 40.0 :
			final_label.config(text="you are obese :(")

calculate_button = Button(text= "calculate" , command=calculate_selected)
calculate_button.pack()

window.mainloop()