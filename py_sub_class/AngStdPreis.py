from Jinja2_basic2PDF import Jinja2_basic


class LaTeXAng_Stdpr(Jinja2_basic):
    def __init__(self, root_dir, out_dir, **pars_dic):
        super().__init__(root_dir, out_dir, **pars_dic)
        self.AngInfo = None
        self.Absender = None
        self.KdInfo = None
        self.set_source_dir("sourcefolder/Angebot")
        # self.set_template_dir("sourcefolder/Angebot/RFFE_Angebot.tex")
        self.set_template_dir("sourcefolder/Angebot/RFFE_Angebot.tex")
        # self.set_template_dir("sourcefolder/LB/RFFE_LB.tex")
        self.set_output_name("TEST ANGEBOT NAME")
        self.set_compile_mode("lualatex")
        print(type(self.template))

    def write_pars(self):
        self.AngInfo = self.pars_dic['AngInfo']
        self.set_output_name(self.AngInfo['Nr'] + "_Ang")
        self.KdInfo = self.pars_dic['KdInfo']
        self.Absender = self.pars_dic['Absender']
        self.tex_output = self.template.render(kd=self.KdInfo, Ang=self.AngInfo, Absender=self.Absender)


# root_dir = os.path.abspath('.')
# outdir = os.path.abspath(os.path.join(root_dir, "testfolder"))
#
# kdInfo = {
#     'VN': "MuVN",
#     'NN': "MusterNN",
#     'Geschl': 'F',
#     'FaA': "MusterFirmaname",
#     'FaNErg': "MusterfirmanameErgänzung",
#     'PLZ': '11001',
#     'Anschr': "Musterstr.11",
#     'St': "Musterstdt"
# }
#
# AngInfo = {
#     'Bez': "TestAngBezeichnung",
#     'Nr': "20210701",
#     'Dat': "01.01.2077",
#     'StdPr': "222,77",
#     'GesStd': "888",
#     'AblDat': "02.03.2088",
# }
# Absender = 'Absender'
# A = LaTeXAng_Stdpr(root_dir, outdir, AngInfo=AngInfo, KdInfo=kdInfo, Absender=Absender)
# A.compile_PDF()
