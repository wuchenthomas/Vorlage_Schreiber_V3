import glob
import os
import shutil
import jinja2


class Jinja2_basic:
    """
    This is the basic class for RFFE Vorschlage Schreiber
    in which the methods for loading latex template, writing parameter from GUI into latex template are defined.
    the specific template should inherit from this super-class.
    """

    def __init__(self, root_dir, out_dir, **pars_dic):
        """
        root_dir: where main.py is
        out_dir: output dir
        pars_dic: parameters written into latex template in dic form
        """
        self.root_dir = root_dir
        self.out_dir = out_dir
        self.source_dir = None
        self.template = None
        self.tex_output = None
        self.out_name = None
        self.compile_mode = "pdflatex"
        self.pars_dic = pars_dic
        self.latex_jinja_env = jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(root_dir)
        )

    def __repr__(self):
        class_info = """
        name: {class_name}
        sourcefolder: {sourcefolder}
        output_name: {out_name}
        compile mode: {compile_mode}
        """.format(class_name=self.__class__.__name__, sourcefolder=self.source_dir, out_name=self.out_name,
                   compile_mode=self.compile_mode)
        return class_info

    def set_template_dir(self, template_dir):
        try:
            print(template_dir)
            print(os.path.isfile(template_dir))
            self.template = self.latex_jinja_env.get_template(template_dir)
        except jinja2.exceptions.TemplateNotFound:
            print("Template Not Found")
            return

    def set_output_name(self, out_name):
        self.out_name = out_name

    def set_source_dir(self, source_dir):
        """root_dic: .cls and company logo dic """
        self.source_dir = source_dir

    def set_compile_mode(self, mode="pdflatex"):
        self.compile_mode = mode

    def copy_SF2out_dir(self):  # Copy the needed source files to the output folder
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)
            print("{} is created".format(self.out_dir))
        else:
            print("{} is existed".format(self.out_dir))

        for file in glob.glob(os.path.join(self.source_dir, "*")):
            shutil.copy2(file, self.out_dir)
            print("copy {} >>>>>>> {}".format(file, self.out_dir))

    def write_pars(self):
        pass

    def compile_PDF(self):
        self.copy_SF2out_dir()
        self.write_pars()
        mode = self.compile_mode
        with open(os.path.join(self.out_dir, self.out_name) + ".tex", "w") as tex:
            tex.write(self.tex_output)
        try:
            for i in range(2):  # It looks like compiling twice would avoid some strange problems...
                # Parameters sometimes cannot be written in
                os.chdir(self.out_dir)
                os.system("{} {}.tex".format(mode, self.out_name))
                os.chdir(self.root_dir)
        except os.error as e:
            print(e)
            pass
