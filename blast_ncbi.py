#!/usr/bin/env python

import sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

if sys.argv[1] == '-h':
    print('Usage: blast_ncbi.py <fasta_file> <output_file>')
    sys.exit()

seq_record = SeqIO.read(sys.argv[1], format='fasta')
results_handle = NCBIWWW.qblast('blastn', 'nt', seq_record.format('fasta'),
                                expect=1e-10, hitlist_size=5, format_type='Text', megablast=True)

with open(sys.argv[2], 'w') as out_handle:
    out_handle.write(results_handle.read())
    out_handle.close()
