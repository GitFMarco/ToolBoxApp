import tkinter as tk
from tkinter import filedialog, messagebox
from .base_frame import BaseFrame
from utils import create_odoo_module


class ModuleCreatorFrame(BaseFrame):

    KEY = "module_creator"

    def __init__(self, parent):
        super().__init__(parent)

        # -- FRAME GRID SETTING (REQUIRED TO CENTER FORM) -- #
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -- FORM FRAME -- #
        center_frame = self.create_subframe(self)
        center_frame.grid(row=1, column=0)
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        # Title
        self.create_label(center_frame, text="> Crea modulo Odoo", font_size=20).pack(pady=10)

        # Form
        form = self.create_subframe(center_frame)
        form.pack(pady=10)

        # Form fields
        # Technical name
        self.create_label(form, text="Nome tecnico", font_size=10, bold=True).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.technical_name = tk.Entry(form, width=30, font=self.theme.font(10))
        self.technical_name.grid(row=0, column=1, padx=5, pady=5)

        # Module name
        self.create_label(form, text="Nome modulo", font_size=10, bold=True).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.module_name = tk.Entry(form, width=30, font=self.theme.font(10))
        self.module_name.grid(row=1, column=1, padx=5, pady=5)

        # Module description
        self.create_label(form, text="Descrizione", font_size=10, bold=True).grid(row=2, column=0, sticky="ne", padx=5, pady=5)
        self.module_description = tk.Text(form, width=30, height=5, font=self.theme.font(10))
        self.module_description.grid(row=2, column=1, padx=5, pady=5)

        # Powered by
        self.create_label(form, text="Powered by", font_size=10, bold=True).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.powered_by = tk.Entry(form, width=30, font=self.theme.font(10))
        self.powered_by.grid(row=3, column=1, padx=5, pady=5)

        # Category
        self.create_label(form, text="Categoria", font_size=10, bold=True).grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.module_category = tk.Entry(form, width=30, font=self.theme.font(10))
        self.module_category.grid(row=4, column=1, padx=5, pady=5)

        # Module path destination
        self.create_label(form, text="Percorso", font_size=10, bold=True).grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(form, width=30, font=self.theme.font(10), textvariable=self.path_var)
        self.path_entry.grid(row=5, column=1, padx=5, pady=5)
        self.create_button(form, text="Sfoglia", command=self.browse_path).grid(row=5, column=2, padx=5)

        # Submit button
        self.create_button(center_frame, text="Crea Modulo", command=self.create_module).pack(pady=10)

    def browse_path(self) -> None:
        """Opens the directory selection window"""
        selected = filedialog.askdirectory()
        if selected:
            self.path_var.set(selected)

    def empty_fields(self) -> None:
        """Empty this frame's fields (except for the path)"""
        self.technical_name.delete(0, tk.END)
        self.module_name.delete(0, tk.END)
        self.module_description.delete("1.0", tk.END)
        self.module_category.delete(0, tk.END)
        self.powered_by.delete(0, tk.END)

    def create_module(self) -> None:
        """Creates the Odoo module"""
        # Module values
        technical_name: str = self.technical_name.get().strip()
        module_name: str = self.module_name.get().strip()
        module_description: str = self.module_description.get("1.0", "end-1c")
        module_category: str = self.module_category.get().strip()
        powered_by: str = self.powered_by.get().strip()
        # Module path creation
        path: str = self.path_var.get().strip()

        if not technical_name or not module_name or not path:
            messagebox.showerror("Campi obbligatori richiesti", "Per procedere è necessario inserire almeno il nome tecnico, il nome e il percorso del modulo.")
            return

        try:
            create_odoo_module(technical_name, module_name, path, module_description, module_category, powered_by)
        except FileExistsError:
            messagebox.showerror("Modulo già esistente", "Il modulo \"%s\" esiste già nel percorso \"%s\"" % (technical_name, path))
        except Exception as ex:
            messagebox.showerror("Errore sconosciuto", str(ex))
        else:
            messagebox.showinfo("Modulo creato", "Modulo %s creato con successo!" % technical_name)
            self.empty_fields()
