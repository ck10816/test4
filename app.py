import tkinter 
import pandas as pd
import tkinter as tk
import json
import jwt
#from py_jwt_validator import PyJwtValidator, PyJwtException
import clipboard
import pyperclip
from PIL import Image
from PIL import ImageTk
import time

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Scanner QR Data')
        
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        
        self.t3=Text()
        self.btn1 = Button(win, text='Get_Data')
        self.btn2=Button(win, text='New_Scan')
        self.btn3=Button(win, text='Result')
        #self.btn4=Button(win, text='BULK_SCAN')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50,height = 30, width = 300)
        
        self.b1=Button(win, text='Evaluate QR', command=self.Get_Data, bg='green', fg='black')
        self.b2=Button(win, text='New Scan', bg='brown', fg='white')
        #self.b3=Button(win, text='BULK SCAN', command=self.BULK_SCAN,bg='blue', fg='white')
        self.b2.bind('<Button-1>', self.New_Scan)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        #self.b3.place(x=300, y=150)
        self.t3.place(x=200, y=200,height = 400, width = 600)
    def Get_Data(self):
        try:
            keys=pd.read_excel(r"\\ant\dept-as\hyd-hydsharedservices\VIRAAT\OPERATIONS\ASHOK NIAJANAPURAM\Appario_BULK_QR\Decrypt_data.xlsx",sheetname="Keys")
            try:
                j=0
                pd.set_option("display.max_colwidth", 10000)
                stringed_data=''
                stringed_data= str(self.t1.get()).strip()
                #try:
                    #data_dict=jwt.decode(str(self.t1.get()).strip(),algorithms='RS256',verify=False)
                #except:
                    #data_dict=jwt.decode(str(self.t1.get()).strip().swapcase(),algorithms='RS256',verify=False)
                try:
                    res= json.loads(data_dict['data'])
                    res.items()
                    stringed_data= str(data_dict)+ '\n'+'\n'+pd.DataFrame(list(res.items()), columns=['column', 'Data']).to_csv(sep='\t', index=False)
                except:
                    stringed_data= str(data_dict)
            
                while j<len(keys):
                    try:
                        try:
                            str(jwt.decode(str(self.t1.get()).strip(),keys.iloc[j,0],algorithms='RS256',verify=True))
                            stringed_data=stringed_data +'\n'+'Key'+str(keys.iloc[j,1])+' Matched'
                        except:
                            str(jwt.decode(str(self.t1.get()).strip().swapcase(),keys.iloc[j,0],algorithms='RS256',verify=True))
                            stringed_data=stringed_data +'\n'+'Key'+str(keys.iloc[j,1])+' Matched'
                            
                    except:
                        stringed_data=stringed_data+'\n'+'Key'+str(keys.iloc[j,1])+' Not Matched'
                    j=j+1
            except:
                stringed_data='Invalid QR Format'
        except:
            #stringed_data='Unable to access keys'
            print('some')
          
        self.t3.insert(END, str(stringed_data))
        stringed_data=''
    def New_Scan(self, event):
        self.t1.delete(0, END)
        self.t3.delete(1.0, END)
    def BULK_SCAN(event):
        self.t1.delete(0, END)
        self.t3.delete(1.0, END)
        
        for i in range(len(data)) :
            try:
                try:
                    data_dict=jwt.decode(str(data.iloc[i,1]).strip(),algorithms='RS256',verify=False)
                except:
                    data_dict=jwt.decode(str(data.iloc[i,1]).strip().swapcase(),algorithms='RS256',verify=False)
                try:
                    res= json.loads(data_dict['data'])
                    data.iloc[i,3]=res['Irn']
                    res.items()
                    stringed_data= str(data_dict)+ '\n'+'\n'+pd.DataFrame(list(res.items()), columns=['column', 'Data']).to_csv(sep='\t', index=False)
                except:
                    stringed_data= str(data_dict)
            except:
                    stringed_data='Invalid QR Format'
        j=0
        while j<len(keys):
            try:
                try:
                    str(jwt.decode(str(data.iloc[i,1]).strip(),keys.iloc[j,0],algorithms='RS256',verify=True))
                    stringed_data=stringed_data +'\n'+'Key'+str(keys.iloc[j,1])+' Matched'    
                except:
                    str(jwt.decode(str(data.iloc[i,1]).strip().swapcase(),keys.iloc[j,0],algorithms='RS256',verify=True))
                    stringed_data=stringed_data +'\n'+'Key'+str(keys.iloc[j,1])+' Matched'    
            except:
                stringed_data=stringed_data+'\n'+'Key'+str(keys.iloc[j,1])+' Not Matched'
            j=j+1  
        data.iloc[i,2]=stringed_data

        stringed_data=''
        #stringed_data=r'File Location:\\ant\dept-as\hyd-hydsharedservices\Diamond\Operations\TESLAA\IRN_DATA_'+ str(time.time())+'.xlsx'
        #data.to_excel(r'\\ant\dept-as\hyd-hydsharedservices\Diamond\Operations\TESLAA\IRN_DATA_'+ str(time.time())+'.xlsx',sheet_name='sheet1')
        self.t3.insert(END, str(stringed_data))
        stringed_data=''
        
        AKIAXYSPDBPKXDCOVA0U

window=tk.Tk()

mywin=MyWindow(window)
window.title('QR Netra - v4.0 Powered by TESLAA-Appario QR Scan')
window.geometry("1910x1070+10+10")
window.mainloop()
