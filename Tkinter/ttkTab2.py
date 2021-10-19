import tkinter
from tkinter import ttk
root = tkinter.Tk()
style = ttk.Style()
settings = {"TNotebook.Tab": {"configure": {"padding": [5, 1],
											"background": "#fdd57e"
											},
								"map": {"background": [("selected", "#C70039"),
														("active", "#fc9292")],
										"foreground": [("selected", "#ffffff"),
														("active", "#000000")]
										}
							}
			}
style.theme_create("mi_estilo", parent="alt", settings=settings)
style.theme_use("mi_estilo")
nb = ttk.Notebook(width=200, height=200)
nb.pressed_index = None
f1 = tkinter.Frame(nb)
f2 = tkinter.Frame(nb)
f3 = tkinter.Frame(nb)
nb.add(f1, text='Pestaña 1')
nb.add(f2, text='Pestaña 2')
nb.add(f3, text='Pestaña 3')
nb.pack(expand=1, fill='both')
root.mainloop()
