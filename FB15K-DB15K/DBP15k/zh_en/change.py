import random

entity2time_en = dict()
entity2time_zh = dict()
max_ = 0
with open('id2entity_zh.txt', 'r', encoding='utf-8') as f, open('ent_ids_1', 'w', encoding='utf-8') as out_file:
    strs = f.readlines()
    for str_ in strs:
        id_, entity = str_.strip().split('\t')
        max_ = int(id_)
        if entity in entity2time_zh:
            entity2time_zh[entity] += 1
        else:
            entity2time_zh[entity] = 1
        print(id_ + '\t' + entity + str(entity2time_zh[entity]), file=out_file)

max_ += 1
with open('id2entity_en.txt', 'r', encoding='utf-8') as f, open('ent_ids_2', 'w', encoding='utf-8') as out_file:
    strs = f.readlines()
    for str_ in strs:
        id_, entity = str_.strip().split('\t')
        id_ = str(int(id_) + max_)
        if entity in entity2time_en:
            entity2time_en[entity] += 1
        else:
            entity2time_en[entity] = 1
        print(id_ + '\t' + entity + str(entity2time_en[entity]), file=out_file)
with open('triples_zh.txt', 'r', encoding='utf-8') as f, open('rel_triples_1', 'w', encoding='utf-8')as out_file:
    for str_ in f.readlines():
        sr, tg, r = str_.strip().split('\t')
        print(sr + '\t' + r + '\t' + tg, file=out_file)

with open('triples_en.txt', 'r', encoding='utf-8') as f, open('rel_triples_2', 'w', encoding='utf-8')as out_file:
    for str_ in f.readlines():
        sr, tg, r = str_.strip().split('\t')
        sr = str(int(sr) + max_)
        tg = str(int(tg) + max_)
        print(sr + '\t' + r + '\t' + tg, file=out_file)

entity_seeds = []
with open('entity_seeds.txt', 'r', encoding='utf-8')as f, open('ent_links', 'w', encoding='utf-8')as  out_file:
    for str_ in f.readlines():
        sr, tg = str_.strip().split('\t')
        tg = str(int(tg) + max_)
        entity_seeds.append((sr, tg))
        print(sr + '\t' + tg, file=out_file)
random.shuffle(entity_seeds)
with open('822_folder/train_links', 'w', encoding='utf-8')as f:
    for sr, tg in entity_seeds[:int(0.5 * len(entity_seeds))]:
        print(sr + '\t' + tg, file=f)
with open('822_folder/test_links', 'w', encoding='utf-8')as f, open('822_folder/valid_links', 'w', encoding='utf-8')as f2:
    for sr, tg in entity_seeds[int(0.5 * len(entity_seeds)):]:
        print(sr + '\t' + tg, file=f)
        print(sr + '\t' + tg, file=f2)

cur_id = ''
values = []
id2values = dict()
with open('atts_properties_zh.txt', 'r', encoding='utf-8')as f, open('attr_triples_1', 'w',
                                                                     encoding='utf-8')as out_file:
    for str_ in f.readlines():
        print(str_, file=out_file)

with open('atts_properties_en.txt', 'r', encoding='utf-8')as f, open('attr_triples_2', 'w',
                                                                     encoding='utf-8')as out_file:
    for str_ in f.readlines():
        id_, att, value_ = str_.strip().split('\t')
        id_ = str(int(id_) + max_)
        print(id_ + '\t' + att + '\t' + value_, file=out_file)
