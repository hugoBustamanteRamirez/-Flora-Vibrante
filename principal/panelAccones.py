import tkinter as tk

class PanelAcciones(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        
        acciones_frame = tk.Frame(self)
        acciones_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        
        boton_1 = tk.Button(acciones_frame, text="Acción 1", command=self.accion_1)
        boton_1.pack(side="left", padx=10)

        boton_2 = tk.Button(acciones_frame, text="Acción 2", command=self.accion_2)
        boton_2.pack(side="left", padx=10)

        boton_3 = tk.Button(acciones_frame, text="Acción 3", command=self.accion_3)
        boton_3.pack(side="left", padx=10)

    def accion_1(self):
        
        print("Acción 1 ejecutada")

    def accion_2(self):
        
        print("Acción 2 ejecutada")

    def accion_3(self):
        
        print("Acción 3 ejecutada")
