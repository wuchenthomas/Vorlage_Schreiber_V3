from py_sub_class.Jinja2_basic2PDF import Jinja2_basic
import os


class LaTeXAng_Stdpr(Jinja2_basic):
    def __init__(self, root_dir, out_dir, **pars_dic):
        super().__init__(root_dir, out_dir, **pars_dic)
        self.AngInfo = None
        self.Absender = None
        self.KdInfo = None
        #self.set_source_dir(os.path.join(root_dir, "sourcefolder/Angebot"))
        #self.set_template_dir(r"./py_sub_class/sourcefolder/Angebot/RFFE_Angebot.tex")
        self.set_template_dir(r"sourcefolder/LB/RFFE_LB.tex")
        self.set_output_name("TEST ANGEBOT NAME")
        self.set_compile_mode("lualatex")
        print(type(self.template))

    def write_pars(self):
        self.AngInfo = self.pars_dic['AngInfo']
        self.set_output_name(self.AngInfo['Nr'] + "_Ang")
        self.KdInfo = self.pars_dic['kdInfo']
        self.Absender = self.pars_dic['Absender']
        self.tex_output = self.template.render(kd=self.KdInfo, Ang=self.AngInfo, Absender=self.Absender)
