# -*- coding: utf-8 -*-
"""Wrapper around Poppler pdftotext.
Parameters
----------
path : str
    path of electronic invoice in PDF

Returns
-------
out : str
    returns extracted text from pdf

Raises
------
EnvironmentError:
    If pdftotext library is not found

PermissionError:
    If pdf is encrypted
"""
def to_text(path):
    from subprocess import Popen, PIPE
    from distutils import spawn #py2 compat

    if spawn.find_executable("pdftotext"): #shutil.which('pdftotext'):
        process = Popen(["pdftotext", '-layout', '-enc', 'UTF-8', path, '-'], stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        if process.returncode == 3:
            raise PermissionError(process.returncode, err)
        else:
            return out
    else:
        raise EnvironmentError('pdftotext not installed. Can be downloaded from https://poppler.freedesktop.org/')
