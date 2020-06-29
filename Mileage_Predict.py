import tkinter as tk
import pickle

# Opening the File
with open('mpg_model.pkl', 'rb') as fp:
    model = pickle.load(fp)
    fp.close()
print("Model Loaded Whats Next?? Lets gO.....")
# Here We Goo
root = tk.Tk()
hp = tk.DoubleVar()
w = tk.DoubleVar()
d = tk.DoubleVar()
def clear():
    hp.set('')
    w.set('')
    d.set('')
clear() 
f1 = tk.Frame(root)
l1 = tk.Label(f1, text="HorsePower".center(20)+" : ")
l1.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
l1.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e1 = tk.Entry(f1, textvariable=hp)
e1.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
e1.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
e1.focus()
f1.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

f2 = tk.Frame(root)
l2 = tk.Label(f2, text="Weight".center(20)+" : ")
l2.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
l2.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e2 = tk.Entry(f2, textvariable=w)
e2.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
e2.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
f2.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

f3 = tk.Frame(root)
l3 = tk.Label(f3, text="Displacement".center(20)+" : ")
l3.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
l3.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e3 = tk.Entry(f3, textvariable=d)
e3.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
e3.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
f3.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

b1 = tk.Button(root, text='Predict Mileage', command=lambda : predict())
b1.config(bg='white', fg='#b150b3', font=('monospace', 25, 'bold'))
b1.pack(fill=tk.X, expand=tk.YES)

b2 = tk.Button(root, text='Exit', command=lambda : root.quit())
b2.config(fg='white', bg='red', font=('monospace', 25, 'bold'))
b2.pack(fill=tk.X, expand=tk.YES)

def predict():
    a = hp.get()
    b = w.get()
    c = d.get()
    features = [ [ a,b,c] ]
    clear()
    mpg = model.predict(features)[0]
    win = tk.Toplevel(root)
    win.grab_set()
    text=f"The Mileage of the Vehicle is :{mpg:.2f}"
    
    msg = tk.Message(win, text=text)
    msg.config(bg='#000000', fg='#50b35a', font=('monospace', 25, 'bold'))
    msg.pack(fill=tk.BOTH, expand=tk.YES)
    eb = tk.Button(win, text='Exit', command=lambda : win.destroy())
    eb.config(fg='#000000', bg='red', font=('monospace', 25, 'bold'))
    eb.pack(fill=tk.X, expand=tk.YES)
    e1.focus()
    
  
root.title('Vehicle Mileage Prediction')
root.mainloop()
