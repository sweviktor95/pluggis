import glob, importlib.util, os
def load(subj):
    out={}
    for p in sorted(glob.glob(f'/tmp/figs/{subj}/*.py')):
        if os.path.basename(p).startswith('_'): continue
        spec=importlib.util.spec_from_file_location("fm_"+os.path.basename(p)[:-3],p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); out.update(m.FIGS)
    return out
