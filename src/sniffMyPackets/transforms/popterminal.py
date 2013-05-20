#!/usr/bin/env python
import subprocess
from common.entities import RebuiltFile
from canari.maltego.message import Field
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Sniffmypackets Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]

#@superuser
@configure(
    label='Pop Open Terminal [pcap]',
    description='Opens a terminal to the folder location',
    uuids=[ 'sniffMyPackets.v2.opentermina_2_folderlocation' ],
    inputs=[ ( 'sniffMyPackets', RebuiltFile ) ],
    debug=False
)
def dotransform(request, response):

    folder = request.fields['tmpfolder']
    cmd_variable = '--working-directory=' + folder
    subprocess.Popen(['gnome-terminal',cmd_variable])
    return response