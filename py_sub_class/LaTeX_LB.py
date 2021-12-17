from Jinja2_basic2PDF import Jinja2_basic
import os


class LaTeX_LB(Jinja2_basic):

    def __init__(self, root_dir, out_dir, **pars_dic):
        super(LaTeX_LB, self).__init__(root_dir, out_dir, **pars_dic)
        self.AngInfo = None
        self.LBloc = None
        self.LBformat = None
        self.set_source_dir("sourcefolder/LB")
        self.set_output_name("TEST LB NAME")
        self.set_template_dir("sourcefolder/LB/RFFE_LB.tex")
        self.set_compile_mode("lualatex")

    def write_pars(self):
        print(self.pars_dic)
        self.AngInfo = self.pars_dic['AngInfo']
        self.LBloc = self.pars_dic['LBloc']
        self.LBformat = self.pars_dic['LBformat']
        self.set_output_name(self.AngInfo['Nr'] + "_LB")
        self.tex_output = self.template.render(Ang=self.AngInfo, LBloc=self.LBloc, LBformat=self.LBformat)
