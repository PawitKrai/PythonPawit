#GUITranslator.py
from tkinter import * #จาก library: tkinter ให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk # ttk is theme of tk ซึ่งเป็นไฟล์ย่อย ซึ่งจะไม่อยู่ใน * จึงต้อง import มาเพิ่ม
###--------------Google Translate--------------
from googletrans import Translator

translator = Translator() #สร้างฟังก์ชันแปลภาษา
    


def printname():
    print('James Pawit')

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #ขนาด GUI: กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by Pawit') #ใส่ชื่อโปรแกรม

#-----config-----
FONT = ('Angsana New',15)

#----- Label -----

L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font = FONT)
L.pack()


#-------Entry (ช่องกรอกข้อความ)-------
v_vocab = StringVar() #เป็น class string เพื่อเป็นกล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40) #เก็บข้อความจาก entry เข้า v_vocab และให้ลักษณะเป็นดัง FONT
E1.pack(pady = 20)




#-------Button (ปุ่มแปล)------------
def Translate():
    vocab = v_vocab.get() #.get คือสั่งให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest = 'th')
    print(vocab + ' : '+meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : '+meaning.text) #set ค่าเอาไว้ เมื่อในวงเล็บมีการเปลี่ยนแปลง
    

B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่ม
B1.pack(ipadx=20,ipady=10) #show ปุ่มขึ้นมาวางจากบนลงล่าง

#----- Label -----

L = ttk.Label(GUI,text='คำแปล',font = FONT)
L.pack()


#----- Result -----
v_result = StringVar() #กล่องสำหรับเก็บคำแปล
R1 = ttk.Label(GUI,textvariable = v_result,font=FONT,foreground='green')
R1.pack()








GUI.mainloop() #ให้ GUI แสดงอยู่ตลอดเวลาจนกว่าจะปิด (บรรทัดสุดท้าย!!!)
