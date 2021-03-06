#!/usr/bin/python
import os
import sys

filename_base = sys.argv[1]

filename_rep = '%s.cls_rep.fa'%filename_base
if( not os.access(filename_rep,os.R_OK) ):
    print "%s is not accessible."%filename_rep
    sys.exit(1)

filename_member = '%s.cls_member.fa'%filename_base
if( not os.access(filename_member,os.R_OK) ):
    print "%s is not accessible."%filename_member
    sys.exit(1)

dir_name = '%s.cls'%filename_base
if( not os.access(dir_name,os.R_OK) ):
    print "Make %s directory .."%dir_name
    os.mkdir(dir_name)

h_rep = ''
rep_seq = dict()
f_rep = open(filename_rep,'r')
for line in f_rep:
    if( line.startswith('>') ):
        h_rep = line.strip().lstrip('>')
        rep_seq[h_rep] = f_rep.next().strip()
f_rep.close()

filename_out = dict()
cls_idx = 1
for h_rep in rep_seq.keys():
    filename_out[h_rep] = os.path.join(dir_name,'cls%07d.fa'%cls_idx)
    f_out = open(filename_out[h_rep],'a')
    f_out.write('>%s\n%s\n'%(h_rep,''.join(rep_seq[h_rep])))
    f_out.close()
    cls_idx += 1

h_member = ''
f_member = open(filename_member,'r')
for line in f_member:
    if( line.startswith('>') ):
        tokens = line.strip().split()
        h_member = tokens[0].lstrip('>')
        h_rep = tokens[1]
        seq_member = f_member.next().strip()
        if(  seq_member == rep_seq[h_rep] ):
            print "Same seq: %s - %s"%(h_member, h_rep)
            continue
        f_out = open(filename_out[h_rep],'a')
        f_out.write('>%s\n%s\n'%(h_member,seq_member))
        f_out.close()
f_member.close() 

