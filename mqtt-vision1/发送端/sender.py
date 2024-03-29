#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import sender_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    sender_support.set_Tk_var()
    top = Toplevel1(root)
    sender_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    sender_support.set_Tk_var()
    top = Toplevel1(w)
    sender_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("569x255+365+358")
        top.title("发送端")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.018, rely=0.039, relheight=0.922
                               , relwidth=0.422)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''连接初始化''')
        self.Labelframe1.configure(background="#d891a1")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=240)

        self.TLabel1 = ttk.Label(self.Labelframe1)
        self.TLabel1.place(relx=0.042, rely=0.128, height=21, width=64
                           , bordermode='ignore')
        self.TLabel1.configure(background="#383dd8")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''服务器地址''')

        self.TLabel2 = ttk.Label(self.Labelframe1)
        self.TLabel2.place(relx=0.042, rely=0.255, height=21, width=40
                           , bordermode='ignore')
        self.TLabel2.configure(background="#383dd8")
        self.TLabel2.configure(foreground="#ffffff")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''端口号''')

        self.TEntry_port = ttk.Entry(self.Labelframe1)
        self.TEntry_port.place(relx=0.333, rely=0.255, relheight=0.098
                               , relwidth=0.15, bordermode='ignore')
        self.TEntry_port.configure(textvariable=sender_support.vartext_port)
        self.TEntry_port.configure(takefocus="")
        self.TEntry_port.configure(cursor="ibeam")

        self.TEntry_username = ttk.Entry(self.Labelframe1)
        self.TEntry_username.place(relx=0.333, rely=0.553, relheight=0.098
                                   , relwidth=0.608, bordermode='ignore')
        self.TEntry_username.configure(textvariable=sender_support.vartext_username)
        self.TEntry_username.configure(takefocus="")
        self.TEntry_username.configure(cursor="ibeam")

        self.TEntry_password = ttk.Entry(self.Labelframe1)
        self.TEntry_password.place(relx=0.333, rely=0.681, relheight=0.098
                                   , relwidth=0.608, bordermode='ignore')
        self.TEntry_password.configure(show="*")
        self.TEntry_password.configure(textvariable=sender_support.vartext_password)
        self.TEntry_password.configure(takefocus="")
        self.TEntry_password.configure(cursor="ibeam")

        self.TLabel3 = ttk.Label(self.Labelframe1)
        self.TLabel3.place(relx=0.042, rely=0.553, height=21, width=40
                           , bordermode='ignore')
        self.TLabel3.configure(background="#5c4ed8")
        self.TLabel3.configure(foreground="#ffffff")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''用户名''')

        self.TLabel4 = ttk.Label(self.Labelframe1)
        self.TLabel4.place(relx=0.042, rely=0.681, height=21, width=28
                           , bordermode='ignore')
        self.TLabel4.configure(background="#6961d8")
        self.TLabel4.configure(foreground="#ffffff")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(text='''密码''')

        self.TButton_connect = ttk.Button(self.Labelframe1)
        self.TButton_connect.place(relx=0.042, rely=0.851, height=27, width=87
                                   , bordermode='ignore')
        self.TButton_connect.configure(command=sender_support.btn_开始订阅被单击)
        self.TButton_connect.configure(takefocus="")
        self.TButton_connect.configure(text='''连接服务器''')

        self.TButton_disconnect = ttk.Button(self.Labelframe1)
        self.TButton_disconnect.place(relx=0.542, rely=0.851, height=27, width=87
                                      , bordermode='ignore')
        self.TButton_disconnect.configure(command=sender_support.btn_停止订阅被单击)
        self.TButton_disconnect.configure(takefocus="")
        self.TButton_disconnect.configure(text='''断开连接''')

        self.TLabel5 = ttk.Label(self.Labelframe1)
        self.TLabel5.place(relx=0.042, rely=0.426, height=21, width=52
                           , bordermode='ignore')
        self.TLabel5.configure(background="#4641d8")
        self.TLabel5.configure(foreground="#ffffff")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(text='''服务质量''')

        self.TCombobox_qos = ttk.Combobox(self.Labelframe1)
        self.TCombobox_qos.place(relx=0.333, rely=0.426, relheight=0.098
                                 , relwidth=0.263, bordermode='ignore')
        self.value_list = [0, 1, 2, ]
        self.TCombobox_qos.configure(values=self.value_list)
        self.TCombobox_qos.configure(textvariable=sender_support.vartext_qos)
        self.TCombobox_qos.configure(takefocus="")

        self.TCombobox_ip = ttk.Combobox(self.Labelframe1)
        self.TCombobox_ip.place(relx=0.333, rely=0.128, relheight=0.098
                                , relwidth=0.596, bordermode='ignore')
        self.value_list = ['47.93.30.53', ]
        self.TCombobox_ip.configure(values=self.value_list)
        self.TCombobox_ip.configure(textvariable=sender_support.vartext_ip)
        self.TCombobox_ip.configure(takefocus="")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="settings")
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu1,
                                  activebackground="#ececec",
                                  activeforeground="#000000",
                                  background="#d9d9d9",
                                  font="TkMenuFont",
                                  foreground="#000000",
                                  label="language")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="English")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="中文")
        self.sub_menu12 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="about")
        self.sub_menu12.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=sender_support.btn_version,
            font="TkMenuFont",
            foreground="#000000",
            label="version")

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.439, rely=0.039, relheight=0.922
                               , relwidth=0.545)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''主题内容发送''')
        self.Labelframe2.configure(background="#84d89a")
        self.Labelframe2.configure(width=310)

        self.TLabel6 = ttk.Label(self.Labelframe2)
        self.TLabel6.place(relx=0.032, rely=0.851, height=21, width=52
                           , bordermode='ignore')
        self.TLabel6.configure(background="#6961d8")
        self.TLabel6.configure(foreground="#ffffff")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(text='''发送主题''')

        self.TCombobox_topic = ttk.Combobox(self.Labelframe2)
        self.TCombobox_topic.place(relx=0.226, rely=0.851, relheight=0.111
                                   , relwidth=0.461, bordermode='ignore')
        self.value_list = ['/data/message', '/data/alarm', '/data/notify', ]
        self.TCombobox_topic.configure(values=self.value_list)
        self.TCombobox_topic.configure(textvariable=sender_support.vartext_topic)
        self.TCombobox_topic.configure(takefocus="")

        self.Scrolledtext1 = ScrolledText(self.Labelframe2)
        self.Scrolledtext1.place(relx=0.0, rely=0.17, relheight=0.574
                                 , relwidth=0.971, bordermode='ignore')
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap="none")

        self.TSeparator1 = ttk.Separator(self.Labelframe2)
        self.TSeparator1.place(relx=0.016, rely=0.149, relwidth=0.935
                               , bordermode='ignore')

        self.TButton_send = ttk.Button(self.Labelframe2)
        self.TButton_send.place(relx=0.742, rely=0.851, height=27, width=57
                                , bordermode='ignore')
        self.TButton_send.configure(command=sender_support.btn_send)
        self.TButton_send.configure(takefocus="")
        self.TButton_send.configure(text='''发送消息''')
        self.TButton_send.configure(width=57)

        self.TSeparator2 = ttk.Separator(self.Labelframe2)
        self.TSeparator2.place(relx=-0.032, rely=0.809, relwidth=0.968
                               , bordermode='ignore')

        self.Button_back = tk.Button(self.Labelframe2)
        self.Button_back.place(relx=0.71, rely=0.043, height=28, width=33
                               , bordermode='ignore')
        self.Button_back.configure(activebackground="#ececec")
        self.Button_back.configure(activeforeground="#000000")
        self.Button_back.configure(background="#d8b48a")
        self.Button_back.configure(command=sender_support.btn_back)
        self.Button_back.configure(disabledforeground="#a3a3a3")
        self.Button_back.configure(foreground="#ffffff")
        self.Button_back.configure(highlightbackground="#d9d9d9")
        self.Button_back.configure(highlightcolor="black")
        self.Button_back.configure(pady="0")
        self.Button_back.configure(text='''←''')
        self.Button_back.configure(width=33)

        self.Button_clear = tk.Button(self.Labelframe2)
        self.Button_clear.place(relx=0.871, rely=0.043, height=28, width=29
                                , bordermode='ignore')
        self.Button_clear.configure(activebackground="#ececec")
        self.Button_clear.configure(activeforeground="#000000")
        self.Button_clear.configure(background="#d8b48a")
        self.Button_clear.configure(command=sender_support.btn_clear)
        self.Button_clear.configure(disabledforeground="#a3a3a3")
        self.Button_clear.configure(foreground="#ffffff")
        self.Button_clear.configure(highlightbackground="#d9d9d9")
        self.Button_clear.configure(highlightcolor="black")
        self.Button_clear.configure(pady="0")
        self.Button_clear.configure(text='''X''')
        self.Button_clear.configure(width=29)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
