# -*- coding: utf-8 -*-

from nltk.stem import SnowballStemmer
import string

stemmer = SnowballStemmer('english')

fin = open('idiom_blacklist.src.zh.txt', 'r')
zh_src_lines = fin.readlines()
fin.close()
fin = open('idiom_blacklist.ref.en.txt', 'r')
en_ref_lines = fin.readlines()
fin.close()
fin = open('idiom_blacklist.trans.en.txt', 'r')
en_trans_lines = fin.readlines()
fin.close()
fin = open('idiom_blacklist.blacklist.en.txt', 'r')
blk_lines = fin.readlines()
fin.close()

fin = open('list_idiom_blacklist.txt', 'r')
idiom_lines = fin.readlines()
fin.close()

# Maintain a list for each idiom; may duplicate if a sentence has more than one idiom
trig_pair_lists = []		# Triggered
ntrig_pair_lists = [] 		# Not triggered

del_punc_dict = dict((ord(c), None) for c in string.punctuation)

def check_and_reg_pair(u_src, u_ref, u_trans, u_blk):
	# Check the translation
	w_list = u_trans.translate(del_punc_dict).lower().split(' ')
	blacklist = [stemmer.stem(w) for w in u_blk.split(' ')]
	trigger = False
	for j in range(len(w_list)):
		if stemmer.stem(w_list[j]) in blacklist:
			trigger = True
			break

	if trigger:
		trig_pair_lists.append( (u_src, u_ref, u_trans, u_blk) )
	else:
		ntrig_pair_lists.append( (u_src, u_ref, u_trans, u_blk) )

# Filter and write to output
for l_id in range(0, len(zh_src_lines)):
	u_src = zh_src_lines[l_id].decode('utf-8').strip()
	u_ref = en_ref_lines[l_id].decode('utf-8').strip()
	u_trans = en_trans_lines[l_id].decode('utf-8').strip()
	u_blk = blk_lines[l_id].decode('utf-8').strip()

	check_and_reg_pair(u_src, u_ref, u_trans, u_blk)

fo_trig_pairs = open('idiom_blacklist.trig.pairs.txt', 'w')
fo_ntrig_pairs = open('idiom_blacklist.nontrig.pairs.txt', 'w')

print 'Triggered = %d\nNot triggered = %d\n' % (len(trig_pair_lists), len(ntrig_pair_lists))
for (u_src, u_ref, u_trans, u_blk) in trig_pair_lists:
	fo_trig_pairs.write('SRC: %s\n' % u_src.encode('utf-8'))
	fo_trig_pairs.write('REF: %s\n' % u_ref.encode('utf-8'))
	fo_trig_pairs.write('TRANS: %s\n' % u_trans.encode('utf-8'))
	fo_trig_pairs.write('BLACKLIST: %s\n\n' % u_blk.encode('utf-8'))

for (u_src, u_ref, u_trans, u_blk) in ntrig_pair_lists:
	fo_ntrig_pairs.write('SRC: %s\n' % u_src.encode('utf-8'))
	fo_ntrig_pairs.write('REF: %s\n' % u_ref.encode('utf-8'))
	fo_ntrig_pairs.write('TRANS: %s\n' % u_trans.encode('utf-8'))
	fo_ntrig_pairs.write('BLACKLIST: %s\n\n' % u_blk.encode('utf-8'))

fo_trig_pairs.close()
fo_ntrig_pairs.close()


