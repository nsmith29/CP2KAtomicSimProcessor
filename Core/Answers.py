import DataProcessing
# import Presentation

class UserArguments:
    PerfectSubdir = ''
    DefectSubdir = ''
    ChemicalPotSubdir = ''
    Exception = False
    Only = False
    NotDir = ''
    OnlyDir = ''

    def __init__(self, perf_subdir, def_subdir, chempot_subdir):
        self.perf_subdir = perf_subdir
        self.def_subdir = def_subdir
        self.chempot_subdir = chempot_subdir
        UserArguments.ArgumentsSaved(self.perf_subdir, self.def_subdir, self.chempot_subdir)

    @classmethod
    def ArgumentsSaved(cls, perf_subdir, def_subdir, chempot_subdir):
        UserArguments.PerfectSubdir = perf_subdir
        UserArguments.DefectSubdir = def_subdir
        UserArguments.ChemicalPotSubdir = chempot_subdir

    @classmethod
    def ExceptionStated(cls, expt):
        UserArguments.Exception = True
        UserArguments.NotDir = expt

    @classmethod
    def OnlyStated(cls, only):
        UserArguments.Only = True
        UserArguments.OnlyDir = only

class UserWants:
    AnalysisWants = ''
    DisplayWants = ''

    def __init__(self, analysis, display):
        self.analysis = analysis
        self.display = display
        UserWants.Save(self.analysis, self.display)

    @classmethod
    def Save(cls, analysis, display):
        UserWants.AnalysisWants = analysis
        UserWants.DisplayWants = display

class ProcessingControls:
    ProcessingWants = ''
    DefectType = ''
    DefectAtom = ''
    Process_wants = ''
    def __init__(self, f):
        self._f = f

    @classmethod
    def SavingOtherWants(cls, processing, typedefectQ):
        process_wants = []
        for want in list(processing):
            change = want.replace(' ', '_')
            process_wants.append(change)

        ProcessingControls.ProcessingWants = processing
        ProcessingControls.DefectType = typedefectQ[0]
        ProcessingControls.DefectAtom = typedefectQ[1:]
        ProcessingControls.Process_wants = process_wants





