from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *



class Maze:
    def __init__ (self,tk,maze=None,name=''):
        Main.clear_scr()
        self.tk=tk
        if maze==None:self.new=True
        else:self.new=False
        if not maze and name=='':self.make_()
        elif not maze and not name=='':self.make_(name=name)
        else:self.open_(maze)
    def make_(self,open_=False,name=''):
        self.able=0
        if not open_:
            self.c_w,self.name_,self.c_h=0,'',0
            self.start_pos,self.end_pos=(0,0),(1,0)
            self.current_tile,self.maze='none',{}
        else:self.current_tile='none'
        if not name=='':self.name_=name
        self.start_poses=[]
        self.arr_fill=[[],[]]
        self.solve_lines=[]
        self.a_b_c_di=PhotoImage(file='img/maze/a_b_c_d.gif')
        self.a_b_ci=PhotoImage(file='img/maze/a_b_c.gif')
        self.a_b_di=PhotoImage(file='img/maze/a_b_d.gif')
        self.a_c_di=PhotoImage(file='img/maze/a_c_d.gif')
        self.b_c_di=PhotoImage(file='img/maze/b_c_d.gif')
        self.a_bi=PhotoImage(file='img/maze/a_b.gif')
        self.b_ci=PhotoImage(file='img/maze/b_c.gif')
        self.c_di=PhotoImage(file='img/maze/c_d.gif')
        self.d_ai=PhotoImage(file='img/maze/a_d.gif')
        self.a_ci=PhotoImage(file='img/maze/a_c.gif')
        self.b_di=PhotoImage(file='img/maze/b_d.gif')
        self.ai=PhotoImage(file='img/maze/a.gif')
        self.bi=PhotoImage(file='img/maze/b.gif')
        self.ci=PhotoImage(file='img/maze/c.gif')
        self.di=PhotoImage(file='img/maze/d.gif')
        self.nonei=PhotoImage(file='img/maze/none.gif')
        self.img_d={'abcd':self.a_b_c_di,'abc':self.a_b_ci,'abd':self.a_b_di,'acd':self.a_c_di,'bcd':self.b_c_di,'ab':self.a_bi,'bc':self.b_ci,'cd':self.c_di,'da':self.d_ai,'ac':self.a_ci,'bd':self.b_di,'a':self.ai,'b':self.bi,'c':self.ci,'d':self.di,'none':self.nonei}
        self.endi=PhotoImage(file='img/maze/end.gif')
        self.starti=PhotoImage(file='img/maze/start.gif')
        self.fr1=Frame(self.tk,bg='black')
        self.fr2=Frame(self.tk,bg='black')
        self.fr=Frame(self.tk,bg='black')
        self.canvas=Canvas(self.fr1,bg='black',width=10,height=10)
        self.btn_next=Button(self.fr,bg='black',fg='white',text='next',command=self.pack_)
        self.btn_next2=Button(self.fr2,bg='black',fg='white',text='next',command=self.set_s)
        self.btn_next3=Button(self.fr2,bg='black',fg='white',text='next',command=self.set_e)
        self.btn_m_screen=Button(self.fr2,bg='black',fg='white',text='end',command=self.fn)
        self.width_=Spinbox(self.fr,from_=2,to=37,bg='black',fg='white')
        self.height_=Spinbox(self.fr,from_=2,to=20,bg='black',fg='white')
        self.tile_=Menubutton(self.fr2,image=self.nonei,bg='black',fg='white',text='tile')
        self.menu=Menu(self.tile_,bg='black',fg='white')
        self.menu.add_command(label='top, right, bottom, left',image=self.a_b_c_di,compound='left',command=self.abcd)
        self.menu.add_command(label='top, right, bottom',image=self.a_b_ci,compound='left',command=self.abc)
        self.menu.add_command(label='top, right, left',image=self.a_b_di,compound='left',command=self.abd)
        self.menu.add_command(label='top, bottom, left',image=self.a_c_di,compound='left',command=self.acd)
        self.menu.add_command(label='right, bottom, left',image=self.b_c_di,compound='left',command=self.bcd)
        self.menu.add_command(label='top, right',image=self.a_bi,compound='left',command=self.ab)
        self.menu.add_command(label='right, bottom',image=self.b_ci,compound='left',command=self.bc)
        self.menu.add_command(label='bottom, left',image=self.c_di,compound='left',command=self.cd)
        self.menu.add_command(label='top, left',image=self.d_ai,compound='left',command=self.da)
        self.menu.add_command(label='top, bottom',image=self.a_ci,compound='left',command=self.ac)
        self.menu.add_command(label='right, left',image=self.b_di,compound='left',command=self.bd)
        self.menu.add_command(label='top',image=self.ai,compound='left',command=self.a)
        self.menu.add_command(label='right,',image=self.bi,compound='left',command=self.b)
        self.menu.add_command(label='bottom',image=self.ci,compound='left',command=self.c)
        self.menu.add_command(label='left',image=self.di,compound='left',command=self.d)
        self.menu.add_command(label='none',image=self.nonei,compound='left',command=self.none)
        self.tile_['menu']=self.menu
        self.canvas.bind_all('<Button-3>',func=self.place_tile)
        self.canvas.bind_all('<space>',func=self.fill)
        Main.add_guis([self.canvas,self.btn_next,self.btn_next2,self.btn_next3,self.btn_m_screen,self.fr,self.fr1,self.fr2,self.tile_,self.width_,self.height_])
        if not open_:
            self.height_.grid(row=0,column=0)
            self.width_.grid(row=1,column=0)
            self.btn_next.grid(row=2,column=0)
            self.fr.grid(row=0,column=0)
        else:
            self.pack_(open_=True)
    def pack_(self,open_=False):
        if not open_:
            c_h,c_w=int(self.height_.get()),int(self.width_.get())
            if c_h<2:c_h=2
            if c_h>15:c_h=15
            if c_w<2:c_w=2
            if c_w>20:c_w=20
            self.btn_next.grid_forget()
            self.height_.grid_forget()
            self.width_.grid_forget()
            self.fr.grid_forget()
            self.c_h,self.c_w=c_h,c_w
        else:c_w,c_h=self.c_w,self.c_h
        self.fr1.grid(row=0,column=0)
        self.canvas.pack(padx=0,pady=0)
        self.canvas['height']=(c_h*50)
        self.canvas['width']=(c_w*50)
        self.fr2.grid(row=0,column=1)
        self.tile_.grid(row=0,column=0)
        self.btn_next2.grid(row=1,column=0)
        for y in range(c_h):
            for x in range(c_w):
                if not open_:
                    self.canvas.create_image((x*50)+25,(y*50)+25,image=self.nonei)
                    self.maze[(x,y)]='none'
                else:
                    try:self.canvas.create_image((x*50)+25,(y*50)+25,image=self.img_d[self.maze[(x,y)]])
                    except:
                        self.canvas.create_image((x*50)+25,(y*50)+25,image=self.img_d['none'])
                        self.maze[(x,y)]='none'
                self.start_poses.append((x,y))
    def abcd(self):
        self.current_tile='abcd'
        self.tile_['image']=self.a_b_c_di
    def abc(self):
        self.current_tile='abc'
        self.tile_['image']=self.a_b_ci
    def abd(self):
        self.current_tile='abd'
        self.tile_['image']=self.a_b_di
    def acd(self):
        self.current_tile='acd'
        self.tile_['image']=self.a_c_di
    def bcd(self):
        self.current_tile='bcd'
        self.tile_['image']=self.b_c_di
    def ab(self):
        self.current_tile='ab'
        self.tile_['image']=self.a_bi
    def bc(self):
        self.current_tile='bc'
        self.tile_['image']=self.b_ci
    def cd(self):
        self.current_tile='cd'
        self.tile_['image']=self.c_di
    def da(self):
        self.current_tile='da'
        self.tile_['image']=self.d_ai
    def ac(self):
        self.current_tile='ac'
        self.tile_['image']=self.a_ci
    def bd(self):
        self.current_tile='bd'
        self.tile_['image']=self.b_di
    def a(self):
        self.current_tile='a'
        self.tile_['image']=self.ai
    def b(self):
        self.current_tile='b'
        self.tile_['image']=self.bi
    def c(self):
        self.current_tile='c'
        self.tile_['image']=self.ci
    def d(self):
        self.current_tile='d'
        self.tile_['image']=self.di
    def none(self):
        self.current_tile='none'
        self.tile_['image']=self.nonei
    def place_tile(self,arg):
        self.arr_fill=[[],[]]
        x,y,x_,y_=0,0,-1,-1
        for xp in range(self.c_w):
            if xp<(arg.x/50)<(xp+1):
                x=(xp*50)+25
                x_=xp
        for yp in range(self.c_h):
            if yp<(arg.y/50)<(yp+1):
                y=(yp*50)+25
                y_=yp
        if x_>-1 and y_>-1:
            if self.able==0:
                self.canvas.create_image(x,y,image=self.img_d[self.current_tile])
                self.maze[(x_,y_)]=self.current_tile
            elif self.able==1:
                self.canvas.delete(self.start_p)
                self.start_p=self.canvas.create_image(x,y,image=self.starti)
                self.start_pos=(x_,y_)
            elif self.able==2:
                if(x_,y_)!=self.start_pos:
                    self.canvas.delete(self.end_p)
                    self.end_p=self.canvas.create_image(x,y,image=self.endi)
                    self.end_pos=(x_,y_)
                    self.solve()
    def fill(self,arg):
        x,y,x_,y_=0,0,-1,-1
        for xp in range(self.c_w):
            if xp<(arg.x/50)<(xp+1):
                x=(xp*50)+25
                x_=xp
        for yp in range(self.c_h):
            if yp<(arg.y/50)<(yp+1):
                y=(yp*50)+25
                y_=yp
        if x_>-1 and y_>-1 and self.able==0:
            if self.arr_fill[0]==[]:
                self.arr_fill[0]=[x_,y_]
            else:
                self.arr_fill[1]=[x_,y_]
                if self.arr_fill[0][0]>self.arr_fill[1][0]:
                    self.arr_fill[0][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                    self.arr_fill[1][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                    self.arr_fill[0][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                if self.arr_fill[0][1]>self.arr_fill[1][1]:
                    self.arr_fill[0][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                    self.arr_fill[1][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                    self.arr_fill[0][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                for _x in range(self.arr_fill[0][0],self.arr_fill[1][0]+1):
                    for _y in range(self.arr_fill[0][1],self.arr_fill[1][1]+1):
                        self.canvas.create_image((_x*50)+25,(_y*50)+25,image=self.img_d[self.current_tile])
                        self.maze[(_x,_y)]=self.current_tile
                self.arr_fill=[[],[]]
    def set_s(self):
        self.optimize()
        for y in range(self.c_h):
            for x in range(self.c_w):
                self.canvas.create_image((x*50)+25,(y*50)+25,image=self.img_d[self.maze[(x,y)]])
        self.start_p=self.canvas.create_image((self.start_pos[0]*50)+25,(self.start_pos[1]*50)+25,image=self.starti)
        self.tile_.grid_forget()
        self.btn_next2.grid_forget()
        self.btn_next3.grid(row=1,column=0)
        self.able=1
    def set_e(self):
        self.end_p=self.canvas.create_image((self.end_pos[0]*50)+25,(self.end_pos[1]*50)+25,image=self.endi)
        self.btn_next3.grid_forget()
        self.start_poses.remove(self.start_pos)
        self.able=2
        self.solve()
    def solve(self):
        for ln in self.solve_lines:self.canvas.delete(ln)
        try:
            self.solve_lines=[]
            pos=list(self.start_pos)
            pos[0]*=50
            pos[0]+=25
            pos[1]*=50
            pos[1]+=25
            pos2=[0,0]
            for key in self.find_path():
                if key=='s':pos2=[pos[0],pos[1]-50]
                if key=='e':pos2=[pos[0]+50,pos[1]]
                if key=='n':pos2=[pos[0],pos[1]+50]
                if key=='w':pos2=[pos[0]-50,pos[1]]
                ln=self.canvas.create_line(pos[0],pos[1],pos2[0],pos2[1],fill='#00A9D8',width=3)
                self.solve_lines.append(ln)
                pos=pos2
                del pos2
        except:
            pass
        self.btn_m_screen.grid(row=1,column=0)
    def format_to_save(self):
        maze,file=self.maze,'#maze\n%s\n%sx%s\n%s,%s %s,%s\n'%(self.name_,self.c_w,self.c_h,self.start_pos[0],self.start_pos[1],self.end_pos[0],self.end_pos[1])
        for coords in maze.keys():
            if coords[0]>-1 and coords[1]>-1:
                tile=maze[coords]
                if not tile=='none':file+='%s,%s %s\n'%(coords[0],coords[1],tile)
        return file
    def optimize(self):
        maze=self.maze
        for y in range(self.c_h):
            for x in range(self.c_w):
                if not maze[(x,y)]=='none':
                    for char in maze[(x,y)]:
                        if char=='a' and y==0:maze[(x,y)]=maze[(x,y)].replace('a','')
                        elif char=='b' and x==self.c_w-1:maze[(x,y)]=maze[(x,y)].replace('b','')
                        elif char=='c' and y==self.c_h-1:maze[(x,y)]=maze[(x,y)].replace('c','')
                        elif char=='d' and x==0:maze[(x,y)]=maze[(x,y)].replace('d','')
                    if maze[(x,y)]=='':maze[(x,y)]='none'
                    elif maze[(x,y)]=='ad':maze[(x,y)]='da'
                for char in maze[(x,y)]:
                    try:
                        if char=='a' and not('c' in maze[(x,y-1)]):maze[(x,y)]=maze[(x,y)].replace('a','')
                        elif char=='b' and not('d' in maze[(x+1,y)]):maze[(x,y)]=maze[(x,y)].replace('b','')
                        elif char=='c' and not('a' in maze[(x,y+1)]):maze[(x,y)]=maze[(x,y)].replace('c','')
                        elif char=='d' and not('b' in maze[(x-1,y)]):maze[(x,y)]=maze[(x,y)].replace('d','')
                    except:
                        pass
                if maze[(x,y)]=='':maze[(x,y)]='none'
                elif maze[(x,y)]=='ad':maze[(x,y)]='da'
        return maze
    def fn(self):
        Main.update_file(self.format_to_save(),self.name_)
        if self.new:Main.add_tab_elem(self.name_,self.format_to_add_tab(self.format_to_save()))
        else:Main.auto_save(None,mn=True)
        self.canvas.pack_forget()
        self.btn_m_screen.grid_forget()
    def find_path(self):
        from heapq import heappop, heappush
        map_,coords,size=self.maze,[self.start_pos,self.end_pos],[self.c_w,self.c_h]
        def pos(cell,goal):return abs(cell[0]-end[0])+abs(cell[1]-end[1])
        def to_list(path):
            for d in path:moves.append(d)
            return moves
        def convert(maze,size):
            graph={}
            for x in range(size[0]):
                for y in range(size[1]):
                    graph[(x,y)]=[]
            for x,y in graph.keys():
                if 'a' in maze[(x,y)]:graph[(x,y)].append(('s',(x,y-1)))
                if 'b' in maze[(x,y)]:graph[(x,y)].append(('e',(x+1,y)))
                if 'c' in maze[(x,y)]:graph[(x,y)].append(('n',(x,y+1)))
                if 'd' in maze[(x,y)]:graph[(x,y)].append(('w',(x-1,y)))
            return graph
        pr_queue,moves,graph,visited,start,end=[],[],convert(map_,size),set(),coords[0],coords[1]
        heappush(pr_queue,(0+pos(start,end),0,"",start))
        while pr_queue:
            _,cost,path,current=heappop(pr_queue)
            if current==end:return to_list(path)
            if current in visited:continue
            visited.add(current)
            for direction,neighbour in graph[current]:heappush(pr_queue,(cost+pos(neighbour,end),cost+1,path+direction,neighbour))
        return []
    def open_(self,maze):
        self.name_,self.c_w,self.c_h,self.start_pos,self.end_pos,self.maze=maze['name'],maze['w'],maze['h'],maze['s_pos'],maze['e_pos'],maze['maze']
        self.make_(open_=True)
    def format_to_add_tab(self,seq):
        seq=seq[6:].split('\n')
        name_=seq[0]
        seq.remove(seq[0])
        all_={'type':'maze','name':name_,'w':int(seq[0].split('x')[0]),'h':int(seq[0].split('x')[1]),'s_pos':(int(seq[1].split(' ')[0].split(',')[0]),int(seq[1].split(' ')[0].split(',')[1])),'e_pos':(int(seq[1].split(' ')[1].split(',')[0]),int(seq[1].split(' ')[1].split(',')[1])),'maze':{}}
        seq.remove(seq[0])
        seq.remove(seq[0])
        try:
            seq.remove('')
        except:
            pass
        for t in seq:all_['maze'][(int(t.split(' ')[0].split(',')[0]),int(t.split(' ')[0].split(',')[1]))]=t.split(' ')[1]
        return all_
class Main(Maze):
    def __init__(self):
        global mn_self
        self.tk=Tk()
        self.tk.title('Game maker')
        self.tk['background']='black'
        self.tk.resizable(0,0)
        self.tk.minsize(width=100,height=100)
        self.tk.geometry('1905x1005+0+0')
        self.mbar=Menu(self.tk,bg='black')
        self.mbar.add_cascade(menu=self.make_menu_file(self.mbar),label='file')
        self.tk['menu']=self.mbar
        self.mazei=PhotoImage(file='img/icons/maze.gif')
        self.add_elementi=PhotoImage(file='img/icons/add_element.gif')
        self.delete_elementi=PhotoImage(file='img/icons/delete_element.gif')
        self.dict_img={'maze':self.mazei,'add_element':self.add_elementi,'delete_element':self.delete_elementi}
        mn_self=self
    def make_menu_file(self,master):
        self.menu_f=Menu(master,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        self.menu_f.add_command(label='new',command=self.new_gm)
        self.menu_f.add_command(label='open',command=self.get_file)
        self.menu_f.add_command(label='save',command=self.auto_save)
        self.menu_f.add_command(label='save as',command=self.save)
        self.menu_f.add_command(label='close GameMaker',command=self.tk.destroy)
        return self.menu_f
    def decode_file(self,file):
        global file_save,all_elems_obj,name_list
        elems=file.split(';\n')
        elems.remove(elems[0])
        all_obj=[]
        for obj in elems:
            all_={}
            if obj.startswith('#maze'):
                all__=str(obj)
                seq=obj[6:].split('\n')
                name_=seq[0]
                name_list.append(name_)
                seq.remove(seq[0])
                all_={'type':'maze','name':name_,'w':int(seq[0].split('x')[0]),'h':int(seq[0].split('x')[1]),'s_pos':(int(seq[1].split(' ')[0].split(',')[0]),int(seq[1].split(' ')[0].split(',')[1])),'e_pos':(int(seq[1].split(' ')[1].split(',')[0]),int(seq[1].split(' ')[1].split(',')[1])),'maze':{}}
                file_save[name_]=all__
                seq.remove(seq[0])
                seq.remove(seq[0])
                try:
                    seq.remove('')
                except:
                    pass
                for t in seq:all_['maze'][(int(t.split(' ')[0].split(',')[0]),int(t.split(' ')[0].split(',')[1]))]=t.split(' ')[1]
                all_obj.append(all_)
        self.mbar=Menu(self.tk,bg='black')
        menu=Menu(self.mbar,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        menu.add_command(label='      add element',image=self.dict_img['add_element'],compound='left',command=self.add_element)
        menu.add_command(label='      delete element',image=self.dict_img['delete_element'],compound='left',command=self.delete_element)
        for obj in all_obj:
            all_elems_obj.append(obj)
            def element(obj=obj):Maze(self.tk,maze=obj)
            menu.add_command(label='      '+obj['name'],image=self.dict_img[obj['type']],compound='left',command=element)
        self.mbar.add_cascade(menu=menu,label='elements')
        self.mbar.add_cascade(menu=self.make_menu_file(self.mbar),label='file')
        self.tk['menu']=self.mbar
    def add_guis(guis):
        global items
        for gui in guis:items.append(gui)
    def clear_scr():
        global items
        for gui in items:
            gui.grid_forget()
            gui.pack_forget()
    def get_file(self):
        global open_file
        self.save_project()
        f=askopenfilename(filetypes=[('GameMaker files','.txt')])
        if not f=='':
            open_file=str(f)
            f=open(f,'r')
            self.decode_file(str(f.read()))
            f.close()
    def save(self):
        global file_save,open_file,new_pr
        if (new_pr or not open_file==''):
            f=asksaveasfilename(filetypes=[('GameMaker files','.txt')])
            if not f=='':
                open_file=str(f)
                f=open(f,'w')
                f.write(Main.convert_(file_save))
                f.close()
    def auto_save(self,mn=True):
        global open_file,file_save,new_pr
        if (new_pr or not open_file==''):
            if open_file=='' and mn:Main.save(None)
            elif not open_file=='':
                f=open(open_file,'w')
                f.write(Main.convert_(file_save))
                f.close()
    def convert_(f):return ';\n'+';\n'.join(f.values())
    def save_project(self):
        global open_file,new_pr
        if (new_pr or not open_file==''):
            if askyesno('Save','Save project before closing?')==1:self.auto_save()
    def update_file(f,name):
        global file_save
        file_save[name]=f
    def add_element(self):
        Main.clear_scr()
        self.elem_select='maze'
        self.elem=Menubutton(self.tk,image=self.mazei,bg='black',fg='white',text='element')
        mn=Menu(self.elem,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        mn.add_command(label='      maze',image=self.mazei,compound='left',command=self.maze)
        self.elem['menu']=mn
        self.elem_select_btn=Button(self.tk,text='next',command=self.call_new_element,bg='black',fg='white')
        self.elem_name=Entry(self.tk,bg='black',fg='white')
        self.elem_name.insert('end','name')
        self.elem.grid(row=0,column=0)
        self.elem_select_btn.grid(row=0,column=1)
        self.elem_name.grid(row=1,column=0)
    def new_gm(self):
        global new_pr
        self.save_project()
        new_pr=True
        self.mbar=Menu(self.tk,bg='black')
        menu=Menu(self.mbar,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        menu.add_command(label='      add element',image=self.dict_img['add_element'],compound='left',command=self.add_element)
        menu.add_command(label='      delete element',image=self.dict_img['delete_element'],compound='left',command=self.delete_element)
        self.mbar.add_cascade(menu=menu,label='elements')
        self.mbar.add_cascade(menu=self.make_menu_file(self.mbar),label='file')
        self.tk['menu']=self.mbar
    def maze(self):
        self.elem['image']=self.mazei
        self.elem_select='maze'
    def call_new_element(self):
        global name_list
        name_=self.elem_name.get()
        while name_ in name_list:name_+='_'
        name_list+=name_
        if self.elem_select=='maze':Maze(self.tk,name=name_)
        self.elem.grid_forget()
        self.elem_select_btn.grid_forget()
        self.elem_name.grid_forget()
    def add_tab_elem(name_,obj_):
        global file_save,all_elems_obj,mn_self
        self=mn_self
        all_elems_obj.append(obj_)
        self.mbar=Menu(self.tk,bg='black')
        menu=Menu(self.mbar,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        menu.add_command(label='      add element',image=self.dict_img['add_element'],compound='left',command=self.add_element)
        menu.add_command(label='      delete element',image=self.dict_img['delete_element'],compound='left',command=self.delete_element)
        for obj in all_elems_obj:
            def element(obj=obj):Maze(self.tk,maze=obj)
            menu.add_command(label='      '+obj['name'],image=self.dict_img[obj['type']],compound='left',command=element)
        self.mbar.add_cascade(menu=menu,label='elements')
        self.mbar.add_cascade(menu=self.make_menu_file(self.mbar),label='file')
        self.tk['menu']=self.mbar
        self.auto_save(mn=False)
    def delete_element(self):
        global all_elems_obj
        if not all_elems_obj==[]:
            self.auto_save(mn=False)
            Main.clear_scr()
            self.elem_select_del=all_elems_obj[0]['name']
            self.elem_del=Menubutton(self.tk,image=self.dict_img[all_elems_obj[0]['type']],bg='black',fg='white',text='element')
            mn=Menu(self.elem_del,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
            for obj in all_elems_obj:
                def rm_element(obj=obj):self.elem_select_del=obj['name']
                mn.add_command(label='      '+obj['name'],image=self.dict_img[obj['type']],compound='left',command=rm_element)
            self.elem_del['menu']=mn
            self.elem_select_btn_del=Button(self.tk,text='delete',command=self.call_delete_element,bg='black',fg='white')
            self.elem_del.grid(row=0,column=0)
            self.elem_select_btn_del.grid(row=0,column=1)
    def call_delete_element(self):
        global all_elems_obj,name_list
        all_=[]
        self.elem_del.grid_forget()
        self.elem_select_btn_del.grid_forget()
        for obj in all_elems_obj:
            if not obj['name']==self.elem_select_del:all_.append(obj)
        all_elems_obj=list(all_)
        name_list.remove(self.elem_select_del)
        self.mbar=Menu(self.tk,bg='black')
        menu=Menu(self.mbar,bg='black',fg='white',activebackground='black',activeborderwidth=0,activeforeground='green')
        menu.add_command(label='      add element',image=self.dict_img['add_element'],compound='left',command=self.add_element)
        menu.add_command(label='      delete element',image=self.dict_img['delete_element'],compound='left',command=self.delete_element)
        for obj in all_elems_obj:
            def element(obj=obj):Maze(self.tk,maze=obj)
            menu.add_command(label='      '+obj['name'],image=self.dict_img[obj['type']],compound='left',command=element)
        self.mbar.add_cascade(menu=menu,label='elements')
        self.mbar.add_cascade(menu=self.make_menu_file(self.mbar),label='file')
        self.tk['menu']=self.mbar
        self.auto_save(mn=False)

global items,file_save,open_file,new_pr,all_elems_obj,mn_self,name_list
items,file_save,open_file,new_pr,all_elems_obj,mn_self,name_list=[],{},'',False,[],None,[]
Main()
